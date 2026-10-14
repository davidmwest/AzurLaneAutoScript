from types import SimpleNamespace

from module.shop.shop_medal import MedalShop2_250814


def medal_shop(medals, reserve, filter_string='BulinT2 > DR > BulinT1'):
    shop = MedalShop2_250814.__new__(MedalShop2_250814)
    shop.config = SimpleNamespace(MedalShop2_Filter=filter_string, MedalShop2_Reserve=reserve)
    shop._currency = medals
    return shop


def item(group, tier=None, price=20, sub_genre=None):
    return SimpleNamespace(group=group, sub_genre=sub_genre, tier=tier, price=price)


GOLDEN_BULIN = item('bulin', 't2', price=80)
BLUEPRINT = item('dr', 's2', price=20)


def test_golden_bulins_may_spend_the_medals_kept_for_them():
    shop = medal_shop(medals=100, reserve=160)

    assert shop.shop_check_item(GOLDEN_BULIN)
    assert shop.shop_spendable(GOLDEN_BULIN) == 100


def test_other_items_only_spend_what_is_above_the_reserve():
    shop = medal_shop(medals=200, reserve=160)

    assert shop.shop_check_item(BLUEPRINT)
    # 40 above the reserve, 2 blueprints at most
    assert shop.shop_spendable(BLUEPRINT) // BLUEPRINT.price == 2
    assert not medal_shop(medals=170, reserve=160).shop_check_item(BLUEPRINT)


def test_no_reserve_spends_everything():
    shop = medal_shop(medals=30, reserve=0)

    assert shop.shop_check_item(BLUEPRINT)
    assert shop.shop_spendable(BLUEPRINT) == 30
