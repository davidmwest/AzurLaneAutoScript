"""
Proto tab of the monthly shops.
Its Specialized Bulin Custom MKIII limit breaks any Ultra Rare ship. It has no limit and each one takes a place in
the dock, so it is only bought if ProtoShop.BuySpecializedBulin is on, then as many as the currency allows.
"""
from module.base.button import Button
from module.base.template import Template
from module.base.timer import Timer
from module.base.utils import crop
from module.logger import logger
from module.ocr.ocr import Digit
from module.shop.assets import SHOP_OCR_BALANCE
from module.shop.clerk import ShopClerk
from module.ui.assets import SHOP_BACK_ARROW

# Cards of the shop, 5 per row: x of their middle, then top and price of each row
CARD_CENTERS = [297, 466, 635, 804, 972]
CARD_ROWS = [(196, 362), (420, 586)]
# A run buys this many at most
PROTO_BUY_MAX = 20


def _buttons(name, x1, y1, x2, y2, row_y):
    buttons = []
    for row, ys in enumerate(CARD_ROWS):
        for col, x in enumerate(CARD_CENTERS):
            area = (x + x1, ys[row_y] + y1, x + x2, ys[row_y] + y2)
            buttons.append(Button(area=area, color=(), button=area, name=f'{name}_{row * 5 + col}'))
    return buttons


PROTO_CARDS = _buttons('PROTO_CARD', -40, 30, 40, 100, row_y=0)
# Around the icon of each card. The item is told by its icon, as long names scroll on their card
# and a screenshot shows any part of them, 'n Custom MKIII' may be the name of another item.
PROTO_ICONS = _buttons('PROTO_ICON', -45, 30, 45, 120, row_y=0)
OCR_PROTO_PRICES = Digit(_buttons('PROTO_PRICE', -20, 0, 56, 24, row_y=1), letter=(255, 255, 255), threshold=128,
                         name='OCR_PROTO_PRICES')
OCR_PROTO_BALANCE = Digit(SHOP_OCR_BALANCE, letter=(100, 100, 100), name='OCR_PROTO_BALANCE')
TEMPLATE_SPECIALIZED_BULIN = Template('./assets/shop/proto/SpecializedBulin.png')


class ProtoShop_250814(ShopClerk):
    def proto_wait_shop(self):
        """
        Wait until the shop shows with nothing over it, like the ship just bought.
        """
        timer = Timer(1.5, count=3).start()
        for _ in self.loop():
            if self.shop_obstruct_handle():
                timer.reset()
                continue
            if self.appear(SHOP_BACK_ARROW, offset=(30, 30)):
                if timer.reached():
                    break
            else:
                timer.reset()

    def shop_buy_handle(self, item):
        """
        The Info popup of the proto shop sits a few pixels aside of the other popups,
        its Cancel button is not found with the offset of handle_popup_confirm().
        """
        return self.handle_popup_confirm('PROTO_BUY', offset=(10, 30))

    def proto_find_bulin(self):
        """
        Returns:
            tuple[Button, int]: Card of the Specialized Bulin and its price, (None, 0) if not on the shop.
        """
        for index, icon in enumerate(PROTO_ICONS):
            if TEMPLATE_SPECIALIZED_BULIN.match(crop(self.device.image, icon.area)):
                return PROTO_CARDS[index], OCR_PROTO_PRICES.ocr(self.device.image)[index]
        return None, 0

    def run(self):
        """
        Pages:
            in: the Proto tab of the monthly shops
        """
        if not self.config.ProtoShop_BuySpecializedBulin:
            return
        logger.hr('Proto shop', level=1)
        bought = 0
        for _ in range(PROTO_BUY_MAX):
            self.proto_wait_shop()
            card, price = self.proto_find_bulin()
            balance = OCR_PROTO_BALANCE.ocr(self.device.image)
            if card is None:
                logger.info('No Specialized Bulin on the proto shop')
                break
            if not price or price > balance:
                logger.info(f'Specialized Bulin costs {price}, {balance} left')
                break
            logger.info(f'Buy a Specialized Bulin for {price}, {balance} before')
            self.shop_buy_execute(card)
            bought += 1
        logger.info(f'Specialized Bulin bought: {bought}')
