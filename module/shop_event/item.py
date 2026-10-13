import re

import cv2
import numpy as np

import module.config.server as server

from module.base.utils import color_similarity_2d, color_similar, crop, rgb2luma
from module.logger import logger
from module.ocr.ocr import Ocr, Digit
from module.shop_event.selector import FILTER_REGEX
from module.statistics.item import Item, ItemGrid

ITEM_SHAPE = (63, 63)
GRID_SHAPE = (152, 206)
DELTA_PRICE_BACKGROUND = (14, 164)
DELTA_ITEM = (45, 44, 45 + ITEM_SHAPE[0], 33 + ITEM_SHAPE[1])
DELTA_AMOUNT = (13, 144, 136, 160)
DELTA_PRICE = (28, 164, 128, 193)
DELTA_TAG = (108, 30, 155, 52)
COUNTER_COLOR = (106, 120, 131)
COUNTER_THRESHOLD = 150
# Ways to prepare a counter for reading: (white columns added on each side, letter threshold).
# A higher threshold makes the letters bolder.
COUNTER_READINGS = ((0, 128), (0, 160), (0, 192), (4, 128), (4, 160), (4, 192))
COUNTER_TOTALS = (500, 350, 100, 50, 40, 30, 20, 15, 10, 5, 4, 2, 1)
PRICE_THRESHOLD = 230
PRICE_BACKGROUND_COLOR = (61, 78, 91)
# Width of the text in front of the counter, "Limit:" on EN.
# Looked up when reading, the server is not known yet if this module is imported before the config is loaded.
COUNTER_LEFT_STRIP = {'jp': 54, 'en': 42}
COUNTER_LEFT_STRIP_DEFAULT = 70


class CounterOcr(Ocr):
    # White columns to add on each side of the counter
    margin = 0

    def __init__(self, buttons, lang='azur_lane', letter=(255, 255, 255), threshold=128,
                 alphabet='0123456789/IDSB', name=None):
        super().__init__(buttons, lang=lang, letter=letter, threshold=threshold, alphabet=alphabet, name=name)

    def pre_process(self, image):
        mask = color_similarity_2d(image, (255, 255, 255))
        brightness = np.min(mask, axis=0)
        match = np.where(brightness < COUNTER_THRESHOLD)[0]
        if len(match):
            left = match[0] + COUNTER_LEFT_STRIP.get(server.server, COUNTER_LEFT_STRIP_DEFAULT)
            total = mask.shape[1]
            if left < total:
                image = image[:, left:]
        image = super().pre_process(image)
        if self.margin:
            image = np.pad(image, [(0, 0), (self.margin, self.margin)], 'constant', constant_values=255)
        return image

    @staticmethod
    def count_glyphs(image):
        """
        Args:
            image (np.ndarray): Pre-processed counter, dark letters on white.

        Returns:
            int: Number of separate letters. Letters that touch each other count as one.
        """
        ink = np.concatenate(([False], np.min(image, axis=0) < 128, [False]))
        return int(np.count_nonzero(ink[1:] & ~ink[:-1]))

    def after_process(self, result):
        result = super().after_process(result)
        result = result.replace('I', '1').replace('D', '0').replace('S', '5')
        result = result.replace('B', '8')
        # fixup result like "55" -> "5/5", "2530" -> "25/30"
        if result.isdigit() and result not in [str(total) for total in COUNTER_TOTALS]:
            candidates = []
            for total in COUNTER_TOTALS:
                total_str = str(total)
                current_str = result[:-len(total_str)]
                if result.endswith(total_str) and current_str and int(current_str) <= total:
                    candidates.append(f'{current_str}/{total_str}')
            # For example, "1350" can be either "13/50" or "1/350".
            # Leave ambiguous results invalid so the shop scanner retries them.
            if len(candidates) == 1:
                result = candidates[0]
        return result

    @staticmethod
    def is_counter(result):
        """
        Returns:
            bool: If result is a counter like `14/15`.
        """
        parts = result.split('/') if result else []
        if len(parts) != 2 or not all(part.isdigit() for part in parts):
            return False
        current, total = [int(part) for part in parts]
        return 0 < total and current <= total

    @staticmethod
    def parse_result(result):
        parts = result.split('/') if result else []
        if len(parts) != 2 or not all(part.isdigit() for part in parts):
            logger.warning(f'Invalid counter format: {result}')
            return [0, 0]

        current, total = [int(part) for part in parts]
        if total <= 0 or current > total:
            logger.warning(f'Invalid counter value: {result}')
            return [0, 0]
        return [current, total]

    @classmethod
    def vote(cls, readings, glyphs=None):
        """
        Args:
            readings (list[str]): The same counter read in different ways.
            glyphs (int): Number of letters seen in the picture of the counter.

        Returns:
            str: The counter most readings agree on, the earlier reading on a tie.
                Readings with as many letters as the picture has go first.
                The first reading if none of them is a counter.
        """
        counters = [reading for reading in readings if cls.is_counter(reading)]
        if not counters:
            return readings[0]
        fitting = [reading for reading in counters if len(reading) == glyphs]
        if fitting:
            counters = fitting
        return max(counters, key=counters.count)

    def ocr(self, image, direct_ocr=False):
        """
        Do OCR on a counter, such as `14/15`, and returns 14, 15

        The model drops a thin "1" every now and then, "10/10" comes back as "0/10" or "10/0"
        and "100/100" as "00/100". Which counters it happens to depends on how the picture is prepared,
        and sometimes most ways of preparing it get the same counter wrong.
        So each counter is read in several ways, and the reading is taken that has as many letters
        as the picture has. If letters touch each other and can not be counted,
        it is the reading that most ways agree on.

        Args:
            image:
            direct_ocr:

        Returns:
            list[list[int]: [[current, total]].
        """
        counters = list(image) if direct_ocr else [crop(image, area) for area in self.buttons]
        glyphs = [self.count_glyphs(self.pre_process(counter)) for counter in counters]

        margin, threshold = self.margin, self.threshold
        readings = []
        try:
            for reading_margin, reading_threshold in COUNTER_READINGS:
                self.margin, self.threshold = reading_margin, reading_threshold
                reading = Ocr.ocr(self, counters, direct_ocr=True)
                readings.append(reading if isinstance(reading, list) else [reading])
        finally:
            self.margin, self.threshold = margin, threshold

        results = [self.parse_result(self.vote(list(texts), count)) for texts, count in zip(zip(*readings), glyphs)]
        if len(self.buttons) == 1:
            return results[0]
        return results


class PriceOcr(Digit):
    def pre_process(self, image):
        mask = color_similarity_2d(image, PRICE_BACKGROUND_COLOR)
        brightness = np.min(mask, axis=0)
        match = np.where(brightness < PRICE_THRESHOLD)[0]
        if len(match):
            left = match[0] + 20
            total = mask.shape[1]
            if left < total:
                image = image[:, left:]
        image = super().pre_process(image)
        return image

PRICE_OCR = PriceOcr([], letter=(221, 221, 221), threshold=128, name='Price_ocr')


URPT_PRICE_IN_PT = 150  # 1 URpt costs 150 pt
COIN_PRICE_IN_URPT = 1  # 1 Coin costs 1 URpt
UR_SHIP_PRICES_IN_URPT = [200, 300]  # UR Ships cost 200 or 300 URpt


class EventShopItem(Item):
    IMAGE_SHAPE = ITEM_SHAPE

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_ship = False
        self._scroll_pos = None
        self.total_count = -1
        self.count = 1

    def __str__(self):
        name = f'{self.name}_x{self.amount}_{self.count}/{self.total_count}_{self.cost}_x{self.price}'

        if self.tag is not None:
            name = f'{name}_{self.tag}'

        return name

    def predict_valid(self):
        luma = rgb2luma(self.image)
        return np.mean(luma > 127) >= 0.2

    @property
    def scroll_pos(self):
        return self._scroll_pos

    @scroll_pos.setter
    def scroll_pos(self, value):
        self._scroll_pos = value

    def __eq__(self, other):
        return id(self) == id(other)

    def correct_name_and_cost(self):
        if self.price in UR_SHIP_PRICES_IN_URPT and self.total_count == 1:
            self.name = 'ShipUR'
            self.cost = 'URpt'
            self.is_ship = True
        elif self.price == COIN_PRICE_IN_URPT and self.total_count == 350:
            # URpt to Coin
            self.name = 'Coin'
            self.cost = 'URpt'
        else:
            self.cost = 'pt'
            if self.price == 135 and self.total_count == 15:
                self.name = 'EquipSSR'
            elif self.price == 2000:
                if self.total_count == 10:
                    self.name = 'SkinBox'
                elif self.total_count == 4:
                    self.name = 'Meta'
                else:
                    self.name = 'EquipSSR'
            elif self.price == 8000:
                self.name = 'ShipSSR'
                self.is_ship = True
            elif self.price == 10000:
                self.name = 'EquipUR'
            elif self.price == URPT_PRICE_IN_PT and self.total_count == 500:
                self.name = 'URpt'
            elif self.name.isdigit():
                logger.warning(f'Unrecognized item with price {self.price} and total count {self.total_count}, '
                               # f'defaulting to EquipSSR')
                               f'saving image for analysis.')
                import os
                from module.base.utils import save_image
                os.mkdir('assets/shop/event/new_templates/') if not os.path.exists('assets/shop/event/new_templates/') else None
                save_image(self.image, f'assets/shop/event/new_templates/{self.name}.png')
                # self.name = 'EquipSSR'

    def predict_genre(self):
        self.group, self.sub_genre, self.tier = None, None, None

        # Can use regular expression to quickly populate
        # the new attributes
        name = self.name.lower()
        result = re.search(FILTER_REGEX, name)
        if result:
            self.group, self.sub_genre, self.tier = \
            [group.lower()
             if group is not None else None
             for group in result.groups()]


class EventShopItemGrid(ItemGrid):
    item_class = EventShopItem

    def __init__(self,
                 grids,
                 templates,
                 template_area=(0, 0, ITEM_SHAPE[0], ITEM_SHAPE[1]),
                 amount_area=(31, 50, ITEM_SHAPE[0], ITEM_SHAPE[1]),
                 cost_area=(DELTA_PRICE[0] - DELTA_ITEM[0], DELTA_PRICE[1] - DELTA_ITEM[1],
                            DELTA_PRICE[2] - DELTA_ITEM[0], DELTA_PRICE[3] - DELTA_ITEM[1]),
                 price_area=(DELTA_PRICE[0] - DELTA_ITEM[0], DELTA_PRICE[1] - DELTA_ITEM[1],
                             DELTA_PRICE[2] - DELTA_ITEM[0], DELTA_PRICE[3] - DELTA_ITEM[1]),
                 tag_area=(DELTA_TAG[0] - DELTA_ITEM[0], DELTA_TAG[1] - DELTA_ITEM[1],
                           DELTA_TAG[2] - DELTA_ITEM[0], DELTA_TAG[3] - DELTA_ITEM[1]),
                 counter_area=(DELTA_AMOUNT[0] - DELTA_ITEM[0], DELTA_AMOUNT[1] - DELTA_ITEM[1],
                               DELTA_AMOUNT[2] - DELTA_ITEM[0], DELTA_AMOUNT[3] - DELTA_ITEM[1]),
                 ):
        super().__init__(grids, templates, template_area, amount_area, cost_area, price_area, tag_area)
        self.counter_ocr = CounterOcr([], letter=COUNTER_COLOR, name="CounterOcr")
        self.counter_area = counter_area
        self.price_ocr = PRICE_OCR

    def predict_tag(self, image):
        color = cv2.mean(np.array(image))[:3]
        if color_similar(color1=color, color2=(255, 72, 72), threshold=50):
            return 'unobtained'
        return None

    def predict(self, image, name=True, amount=True, cost=False, price=True, tag=True, counter=True, scroll_pos=None):
        super().predict(image, name=name, amount=amount, cost=cost, price=price, tag=tag)
        if counter and len(self.items):
            counter_list = [item.crop(self.counter_area) for item in self.items]
            counter_list = self.counter_ocr.ocr(counter_list, direct_ocr=True)
            for i, t in zip(self.items, counter_list):
                i.count, i.total_count = t

        if isinstance(scroll_pos, float) and len(self.items):
            for i in self.items:
                i.scroll_pos = scroll_pos

        for i in self.items:
            if not (i.count == 0 and i.total_count == 0):
                i.correct_name_and_cost()
            i.predict_genre()

        return self.items
