import re
from datetime import datetime, timedelta

import numpy as np

import module.config.server as server
from module.base.button import ButtonGrid
from module.base.decorator import cached_property
from module.base.timer import Timer
from module.base.utils import color_similarity_2d, crop
from module.config.utils import server_time_offset
from module.exception import GameStuckError
from module.logger import logger
from module.meowfficer.assets import MEOWFFICER_GET_CHECK, MEOWFFICER_TRAIN_CLICK_SAFE_AREA
from module.meowfficer.collect import SWITCH_LOCK
from module.ocr.ocr import Digit, Ocr
from module.shop.assets import SHOP_OCR_BALANCE, SHOP_OCR_OIL, SHOP_OCR_OIL_CHECK
from module.shop.shop_medal import ShopScroll
from module.shop_event.assets import *
from module.ui.navbar import Navbar
from module.ui.ui import UI

EVENT_SHOP_SCROLL = ShopScroll(
    EVENT_SHOP_SCROLL_AREA,
    color=(44, 48, 56),
    name="EVENT_SHOP_SCROLL"
)
EVENT_SHOP_SCROLL.drag_threshold = 0.08
EVENT_SHOP_SCROLL.edge_threshold = 0.1

if server.server == 'tw':
    EVENT_SHOP_DEADLINE_COLOR = (102, 204, 255)
else:
    EVENT_SHOP_DEADLINE_COLOR = (96, 162, 62)
OCR_EVENT_SHOP_DEADLINE = Ocr(SHOP_EVENT_DEADLINE, lang='cnocr', letter=EVENT_SHOP_DEADLINE_COLOR,
                              alphabet='0123456789.:~-', name="OCR_EVENT_SHOP_DEADLINE")

OCR_EVENT_SHOP_PT = Digit(SHOP_OCR_BALANCE, letter=(100, 100, 100), name='OCR_EVENT_SHOP_PT')
OCR_EVENT_SHOP_URPT = Digit(SHOP_OCR_BALANCE_SECOND, letter=(100, 100, 100), name='OCR_EVENT_SHOP_URPT')


EVENT_SHOP_TAB_AREA = (206, 92, 1092, 134)
EVENT_SHOP_TAB_GAP = 33
# Width of the icon in front of a balance
EVENT_SHOP_BALANCE_ICON = 29


def parse_event_shop_deadline(period, today):
    """
    Args:
        period (str): Period the event shop is open, as read from the screen.
            Like ":2026.8.13~2026.9.3", or without years like ":10.8-10.21" on EN.
        today (datetime): Date on the server.

    Returns:
        datetime | None: When the shop closes, None if the period can not be read.
    """
    try:
        dates = re.findall(r'(\d{4})\.(\d{1,2})\.(\d{1,2})', period)
        if len(dates) >= 2:
            y, m, d = dates[-1]
            return datetime(int(y), int(m), int(d)) + timedelta(days=1)

        dates = re.findall(r'(\d{1,2})\.(\d{1,2})', period)
        if len(dates) < 2:
            return None
        m, d = dates[-1]
        deadline = datetime(today.year, int(m), int(d)) + timedelta(days=1)
        # A shop that closes in January, seen in December
        if deadline < today - timedelta(days=180):
            deadline = datetime(today.year + 1, int(m), int(d)) + timedelta(days=1)
        return deadline
    except ValueError:
        # Not a date, like 13.45
        return None


class EventShopUI(UI):
    def event_shop_tab_count(self):
        """
        Returns:
            int: Number of tabs in the event shop, from the width of the active tab.
        """
        area, gap_x = EVENT_SHOP_TAB_AREA, EVENT_SHOP_TAB_GAP
        image = crop(self.device.image, area)
        tab = color_similarity_2d(image, color=(232, 238, 240))
        index = np.where(np.average(tab > 221, axis=0) > 0.5)[0]
        return (area[2] - area[0] + gap_x) // (len(index) + gap_x)

    @cached_property
    def event_shop_tab_count_and_navbar(self):
        area, gap_x = EVENT_SHOP_TAB_AREA, EVENT_SHOP_TAB_GAP
        # The tabs fade in when the shop opens, and a tab that is not fully shown yet looks narrower,
        # like one of several. So wait until two screenshots in a row give the same count.
        count = 0
        for _ in self.loop(timeout=3):
            previous, count = count, self.event_shop_tab_count()
            if count == previous:
                break
        else:
            logger.warning('Event shop tab count is not stable, using the last one')
        logger.info(f"Event shop tab count: {count}")
        delta_x = (area[2] - area[0] + gap_x) // count - gap_x
        grid = ButtonGrid((206, 92), (delta_x + gap_x, 44),
                          (delta_x, 44), (count, 1),
                          "EVENT_SHOP_TAB_GRID")
        navbar = Navbar(grids=grid,
                        active_color=(232, 238, 240), inactive_color=(127, 141, 151),
                        active_count=delta_x * (area[3] - area[1]) // 2,
                        inactive_count=delta_x * (area[3] - area[1]) // 2)
        return count, navbar

    @cached_property
    def event_shop_has_urpt(self):
        if self.image_color_count(SHOP_OCR_BALANCE_SECOND, OCR_EVENT_SHOP_URPT.letter, threshold=95, count=30):
            logger.info("Event shop has urpt.")
            return True
        else:
            logger.info("Event shop has no urpt.")
            return False

    def _get_event_deadline(self):
        """
        Get event deadline in server timezone

        Returns:
            datetime | None:
        """
        period = OCR_EVENT_SHOP_DEADLINE.ocr(self.device.image)
        # OCR result is like ":2026.8.13~2026.9.323:59:59", remove "23:59:59"
        period, _, _ = period.partition('23:59:59')
        deadline = parse_event_shop_deadline(period, today=datetime.now() - server_time_offset())
        if deadline is None:
            logger.warning(f"Failed to read event deadline: {period}")
        return deadline

    @cached_property
    def is_event_ended(self):
        if self.config.EVENT_SHOP_IGNORE_DEADLINE:
            return True

        for _ in self.loop(timeout=2):
            deadline = self._get_event_deadline()
            if deadline is not None:
                break
        else:
            logger.error('Failed to get event deadline')
            return False

        server_now = datetime.now() - server_time_offset()
        return (deadline - server_now).days < 7

    def event_shop_load_ensure(self):
        ensure_timeout = Timer(3, count=6).start()
        for _ in self.loop():
            if self.image_color_count(SHOP_OCR_BALANCE, OCR_EVENT_SHOP_PT.letter, threshold=95, count=30):
                logger.info("Event shop loaded.")
                break
            if ensure_timeout.reached():
                raise GameStuckError('Waiting too long for EventShop to appear.')
        return True

    def is_ur_voucher_balance(self, button):
        """
        Args:
            button (Button): Area of the digits of a balance in the event shop.

        Returns:
            bool: If the icon in front of the balance is the UR voucher, a light blue orb.
                The icon of the event points is another one in every event.
        """
        x1, y1, x2, y2 = button.area
        icon = self.image_crop((x1 - EVENT_SHOP_BALANCE_ICON, y1, x1, y2), copy=False).astype(np.int16)
        blue = icon[:, :, 2] - icon[:, :, 0] > 25
        return bool(np.mean(blue) > 0.25)

    @cached_property
    def is_pt_reversed(self):
        """
        Returns:
            bool: If the event points are the left balance and the UR vouchers the right one.
        """
        left = self.is_ur_voucher_balance(SHOP_OCR_BALANCE_SECOND)
        right = self.is_ur_voucher_balance(SHOP_OCR_BALANCE)
        if left != right:
            return right
        # Can not tell by the icons, go by the events known to have it this way
        blacklist = [
            SHOP_EVENT_20240521
        ]
        return self.ui_process_check_button(check_button=blacklist)

    def event_shop_get_pt(self):
        if self.is_pt_reversed:
            pt = OCR_EVENT_SHOP_URPT.ocr(self.device.image)
        else:
            pt = OCR_EVENT_SHOP_PT.ocr(self.device.image)
        return pt

    def event_shop_get_urpt(self):
        if self.is_pt_reversed:
            urpt = OCR_EVENT_SHOP_PT.ocr(self.device.image)
        else:
            urpt = OCR_EVENT_SHOP_URPT.ocr(self.device.image)
        return urpt

    def get_oil(self, skip_first_screenshot=True):
        """
        Returns:
            int: Oil amount
        """
        amount = 0
        timeout = Timer(1, count=2).start()
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                self.device.screenshot()

            if timeout.reached():
                logger.warning('Get oil timeout')
                break

            if not self.appear(SHOP_OCR_OIL_CHECK, offset=(10, 2)):
                logger.info('No oil icon')
                continue
            ocr = Digit(SHOP_OCR_OIL, name='OCR_OIL', letter=(247, 247, 247), threshold=128)
            amount = ocr.ocr(self.device.image)
            if amount >= 100:
                break

        return amount

    def handle_get_meowfficer(self):
        if self.appear(MEOWFFICER_GET_CHECK, offset=(40, 40), interval=3):
            logger.info(f'Getting Meowfficer rewards.')
            SWITCH_LOCK.set('lock', main=self)
            # Wait until info bar disappears
            self.ensure_no_info_bar(timeout=1)
            self.device.click(MEOWFFICER_TRAIN_CLICK_SAFE_AREA)
            return True
        return False
