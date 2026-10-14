import re

import cv2
import numpy as np
from scipy import signal

import module.config.server as server
from module.base.button import ButtonGrid
from module.base.decorator import cached_property, del_cached_property
from module.base.timer import Timer
from module.base.utils import random_rectangle_point, rgb2gray
from module.logger import logger
from module.map_detection.utils import Points
from module.ocr.ocr import Digit, DigitYuv, Ocr
from module.shop.assets import *
from module.shop.base import FILTER, ShopItemGrid_250814
from module.shop.clerk import ShopClerk
from module.shop.shop_status import ShopStatus
from module.ui.scroll import Scroll, best_interval, best_window


class ShopScroll(Scroll):
    # Length of the button, known once the scroll has been seen at the top.
    # It depends on how much the shop has to sell, set it to None when a different shop is opened.
    button_length = None

    def match_color(self, main):
        """
        The scroll is translucent, so what it looks like depends on the page behind it.
        Where the page is about as dark as the scroll itself, a row of the button can not be told
        from a row of the background, and taking every row on its own finds pieces of button all over.

        The button is one piece, so take the continuous stretch of rows that looks most like it.
        An end of the button that lies on a dark part of the page is still a guess,
        and a button of the wrong length gives a wrong position and a wrong page size.
        At the top one end is known, so the length is measured there
        and from then on the button is the stretch of that length that fits best.

        Args:
            main (ModuleBase):

        Returns:
            np.ndarray: Shape (n,), dtype bool.
        """
        background_transparency = 0.2
        button_transparency = 0.5
        delta_x = 3
        area = (
            self.area[0] - delta_x,
            self.area[1],
            self.area[2] + delta_x,
            self.area[3]
        )
        image = main.image_crop(area, copy=False).astype(np.float32)
        baseline_color = np.mean(image[:, [0, -1], :], axis=1)
        masked_color = image[:, image.shape[1] // 2, :]
        background_mask = background_transparency * np.array(self.color) + (1 - background_transparency) * baseline_color
        button_mask = button_transparency * np.array(self.color) + (1 - button_transparency) * baseline_color
        err_background = np.sum((masked_color - background_mask) ** 2, axis=1)
        err_button = np.sum((masked_color - button_mask) ** 2, axis=1)
        # Positive where a row looks more like the button than like the background
        score = err_background - err_button
        start, end = best_interval(score)
        if end > start:
            if start == 0:
                # The button is shorter than it is while the list bounces back from the end
                self.button_length = max(end, self.button_length or 0)
                end = self.button_length
            elif self.button_length:
                start = best_window(score, self.button_length)
                end = start + self.button_length
        mask = np.zeros(score.shape, dtype=np.bool_)
        mask[start:end] = True
        self.length = np.sum(mask)
        return mask

    def drag_to_end(self, main):
        """
        Drag the button past the lower end of the scroll, however close to the end it already is.
        set_bottom() leaves it where it is within drag_threshold of the end.

        Args:
            main (ModuleBase):
        """
        logger.info(f'{self.name} drag to end')
        current = self.cal_position(main)
        p1 = random_rectangle_point(self.position_to_screen(current), n=1)
        p2 = random_rectangle_point(self.position_to_screen(1.0, random_range=self.edge_add), n=1)
        main.device.swipe(p1, p2, name=self.name, distance_check=False)

        # Wait until the list stopped moving
        previous = None
        for _ in main.loop(skip_first=False, timeout=3):
            current = self.cal_position(main)
            if current == previous:
                break
            previous = current


MEDAL_SHOP_SCROLL_250814 = ShopScroll(
    MEDAL_SHOP_SCROLL_AREA_250814.button,
    color=(44, 48, 56),
    name="MEDAL_SHOP_SCROLL_250814"
)
MEDAL_SHOP_SCROLL_250814.drag_threshold = 0.1
# A little bit larger than 0.1 to handle bottom
MEDAL_SHOP_SCROLL_250814.edge_threshold = 0.12


class ShopPriceOcr(DigitYuv):
    def after_process(self, result):
        result = Ocr.after_process(self, result)
        # '100' detected as '00' on retrofit blueprint
        if result == '00':
            result = '100'
        return Digit.after_process(self, result)


PRICE_OCR = ShopPriceOcr([], letter=(255, 223, 57), threshold=32, name='Price_ocr')
if server.server == 'jp':
    PRICE_OCR_250814 = Digit([], lang='cnocr', letter=(235, 235, 255), threshold=128, name='Price_ocr')
else:
    PRICE_OCR_250814 = Digit([], letter=(255, 255, 255), threshold=128, name='Price_ocr')
TEMPLATE_MEDAL_ICON = Template('./assets/shop/cost/Medal.png')
TEMPLATE_MEDAL_ICON_2 = Template('./assets/shop/cost/Medal_2.png')
TEMPLATE_MEDAL_ICON_3 = Template('./assets/shop/cost/Medal_3.png')


class MedalShop2_250814(ShopClerk, ShopStatus):
    @cached_property
    def shop_filter(self):
        """
        Returns:
            str:
        """
        return self.config.MedalShop2_Filter.strip()

    # New UI in 2025-08-14
    def _get_medals(self):
        """
        Returns:
            np.array: [[x1, y1], [x2, y2]], location of the medal icon upper-left corner.
        """
        area = (265, 317, 999, 635)
        # copy image because we gonna paint it
        image = self.image_crop(area, copy=True)
        medals = TEMPLATE_MEDAL_ICON_3.match_multi(image, similarity=0.5, threshold=5)
        medals = Points([(0., m.area[1]) for m in medals]).group(threshold=5)
        logger.attr('Medals_icon', len(medals))
        return medals

    def wait_until_medal_appear(self, skip_first_screenshot=True):
        """
        After entering medal shop page,
        items are not loaded that fast,
        wait until any medal icon appears
        """
        timeout = Timer(1, count=3).start()
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                self.device.screenshot()

            medals = self._get_medals()

            if timeout.reached():
                break
            if len(medals):
                break

    @cached_property
    def shop_grid(self):
        return self.shop_medal_grid()

    def shop_medal_grid(self):
        """
        Returns:
            ButtonGrid:
        """
        # (472, 348, 1170, 648)
        medals = self._get_medals()
        count = len(medals)
        if count == 0:
            logger.warning('Unable to find medal icon, assume item list is at top')
            origin_y = 228
            delta_y = 223
            row = 2
        elif count == 1:
            y_list = medals[:, 1]
            # +256, top of the crop area in _get_medals()
            # -125, from the top of medal icon to the top of shop item
            origin_y = y_list[0] + 317 - 126
            delta_y = 223
            row = 1
        elif count == 2:
            y_list = medals[:, 1]
            y1, y2 = y_list[0], y_list[1]
            origin_y = min(y1, y2) + 317 - 126
            delta_y = abs(y1 - y2)
            row = 2
        else:
            logger.warning(f'Unexpected medal icon match result: {[m for m in medals]}')
            origin_y = 228
            delta_y = 223
            row = 2

        # Make up a ButtonGrid
        # Original grid is:
        # shop_grid = ButtonGrid(
        #     origin=(476, 246), delta=(156, 213), button_shape=(98, 98), grid_shape=(5, 2), name='SHOP_GRID')
        shop_grid = ButtonGrid(
            origin=(265, origin_y), delta=(169, delta_y), button_shape=(64, 64), grid_shape=(5, row), name='SHOP_GRID')
        return shop_grid

    shop_template_folder = './assets/shop/medal'

    @cached_property
    def shop_medal_items(self):
        """
        Returns:
            ShopItemGrid_250814:
        """
        shop_grid = self.shop_grid
        shop_medal_items = ShopItemGrid_250814(
            shop_grid,
            templates={},
            amount_area=(60, 74, 96, 95),
            cost_area=(-12, 115, 60, 155),
            price_area=(14, 122, 85, 149),
        )
        shop_medal_items.load_template_folder(self.shop_template_folder)
        shop_medal_items.load_cost_template_folder('./assets/shop/cost')
        shop_medal_items.similarity = 0.85  # Lower the threshold for consistent matches of PR/DRBP
        shop_medal_items.cost_similarity = 0.5
        shop_medal_items.price_ocr = PRICE_OCR_250814
        return shop_medal_items

    def shop_items(self) -> ShopItemGrid_250814:
        """
        Shared alias name for all shops,
        so to use  @Config must define
        a unique alias as cover
        Overriding to add type hint to
        accommodate unique func,
        get_soldout_count in run()

        Returns:
            ShopItemGrid_250814:
        """
        return self.shop_medal_items

    def shop_currency(self):
        """
        Ocr shop medal currency
        Then return medal count

        Returns:
            int: medal amount
        """
        self._currency = self.status_get_medal()
        logger.info(f'Medal: {self._currency}')
        return self._currency

    def shop_is_first_choice(self, item):
        """
        Returns:
            bool: If the item is what the first selector of the filter asks for
        """
        first = re.sub(r'[ \t\r\n]', '', self.shop_filter).split('>')[0]
        return bool(first) and FILTER.apply_filter_to_obj(obj=item, filter=FILTER.parse_filter(first))

    def shop_spendable(self, item):
        """
        Medals in MedalShop2.Reserve are kept for the first item of the filter,
        like golden bulins that come back at the start of every month.

        Returns:
            int: Medals that can be spent on this item
        """
        reserve = max(int(self.config.MedalShop2_Reserve or 0), 0)
        if reserve and not self.shop_is_first_choice(item):
            return max(self._currency - reserve, 0)
        return self._currency

    def shop_check_item(self, item):
        return item.price <= self.shop_spendable(item)

    def shop_has_loaded(self, items):
        """
        If any item parsed with a default
        price of 5000; then shop cannot
        be safely bought from yet

        Returns:
            bool
        """
        for item in items:
            if int(item.price) == 5000:
                return False
        return True

    def shop_interval_clear(self):
        """
        Clear interval on select assets for
        shop_buy_handle
        """
        super().shop_interval_clear()
        self.interval_clear(SHOP_BUY_CONFIRM_SELECT)
        self.interval_clear(SHOP_BUY_CONFIRM_AMOUNT)

    def shop_buy_handle(self, item):
        """
        Handle shop_medal buy interface if detected

        Args:
            item: Item to handle

        Returns:
            bool: whether interface was detected and handled
        """
        if self.appear(SHOP_BUY_CONFIRM_SELECT, offset=(20, 20), interval=3):
            self.shop_buy_select_execute(item)
            self.interval_reset(SHOP_BUY_CONFIRM_SELECT)
            return True
        if self.appear(SHOP_BUY_CONFIRM_AMOUNT, offset=(20, 20), interval=3):
            self.shop_buy_amount_execute(item)
            self.interval_reset(SHOP_BUY_CONFIRM_AMOUNT)
            return True

        return False

    def run(self):
        """
        Run Medal Shop
        """
        # Base case; exit run if filter empty
        import time
        if not self.shop_filter:
            return

        # When called, expected to be in
        # correct Medal Shop interface
        logger.hr('Medal Shop', level=1)
        # Execute buy operations
        MEDAL_SHOP_SCROLL_250814.set_top(main=self)
        time.sleep(0.5)
        while 1:
            # sold items are auto sorted behind
            # if we find any soldout items, no need to check behind
            if self.shop_items().get_soldout_count(self.device.image):
                logger.info('Medal shop early stop')
                break

            self.shop_buy()

            if MEDAL_SHOP_SCROLL_250814.at_bottom(main=self):
                logger.info('Medal shop reach bottom, stop')
                break
            else:
                MEDAL_SHOP_SCROLL_250814.next_page(main=self, page=0.66)
                del_cached_property(self, 'shop_grid')
                del_cached_property(self, 'shop_medal_items')
                continue
