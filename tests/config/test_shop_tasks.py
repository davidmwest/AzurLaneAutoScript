from module.config.config_updater import ConfigUpdater
from module.config.deep import deep_get


def test_settings_of_the_guild_and_monthly_shops_move_out_of_shop_once():
    old = {'ShopOnce': {
        'Scheduler': {'Enable': True},
        'GuildShop': {'Filter': 'PlateT4 > Chip', 'PLATE_T4': 'gun', 'Refresh': False},
        'MedalShop2': {'Filter': 'BulinT2'},
        'CoreShop': {'Filter': 'Chip'},
        'MeritShop': {'Filter': 'Cube'},
    }}

    new = ConfigUpdater().config_redirect(old, {})

    assert deep_get(new, 'ShopGuild.GuildShop') == {'Filter': 'PlateT4 > Chip', 'PLATE_T4': 'gun', 'Refresh': False}
    assert deep_get(new, 'ShopMonthly.MedalShop2.Filter') == 'BulinT2'
    assert deep_get(new, 'ShopMonthly.CoreShop.Filter') == 'Chip'
    assert deep_get(new, 'ShopGuild.Scheduler.Enable') is True
    assert deep_get(new, 'ShopMonthly.Scheduler.Enable') is True


def test_settings_already_moved_are_not_overwritten():
    old = {
        'ShopOnce': {'GuildShop': {'Filter': 'PlateT4 > Chip'}},
        'ShopGuild': {'GuildShop': {'Filter': 'PlateT4'}},
    }

    new = ConfigUpdater().config_redirect(old, {})

    assert deep_get(new, 'ShopGuild.GuildShop.Filter') is None

