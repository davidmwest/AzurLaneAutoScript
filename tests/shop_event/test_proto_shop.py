import os
from types import SimpleNamespace
from unittest.mock import Mock

import cv2
import pytest

import module.config.server as server
from module.shop.shop_proto import OCR_PROTO_BALANCE, PROTO_CARDS, ProtoShop_250814, is_specialized_bulin

DATA = os.path.join(os.path.dirname(__file__), 'data')


@pytest.fixture(autouse=True)
def en():
    previous = server.server
    server.set_server('en')
    yield
    server.set_server(previous)


def load(name):
    """
    The Proto tab at 2560x1440 as Alas sees it, black except the names, prices and balance.
    """
    return cv2.cvtColor(cv2.imread(os.path.join(DATA, name)), cv2.COLOR_BGR2RGB)


@pytest.mark.parametrize('name, bulin', [
    ('becialized Buli', True),
    ('Specialized Bulin Custom MKIII', True),
    ('ecial Generall', False),
    ('attage Amplifi', False),
])
def test_specialized_bulin_by_its_name_cut_on_the_card(name, bulin):
    assert is_specialized_bulin(name) == bulin


def proto_shop(enabled=True):
    shop = ProtoShop_250814.__new__(ProtoShop_250814)
    shop.config = SimpleNamespace(ProtoShop_BuySpecializedBulin=enabled)
    shop.device = SimpleNamespace(image=load('proto_tab.png'))
    return shop


def test_specialized_bulin_is_found_on_the_proto_tab():
    shop = proto_shop()

    card, price = shop.proto_find_bulin()

    assert card is PROTO_CARDS[4]
    assert price == 4000
    assert OCR_PROTO_BALANCE.ocr(shop.device.image) == 34254


def test_nothing_is_bought_by_default():
    shop = proto_shop(enabled=False)
    shop.shop_buy_execute = Mock()
    shop.proto_wait_shop = Mock()

    shop.run()

    shop.shop_buy_execute.assert_not_called()
