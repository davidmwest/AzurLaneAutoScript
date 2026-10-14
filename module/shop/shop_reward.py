from module.shop.assets import *
from module.shop.shop_core import CoreShop_250814
from module.shop.shop_general import GeneralShop_250814
from module.shop.shop_guild import GuildShop_250814
from module.shop.shop_medal import MedalShop2_250814
from module.shop.shop_merit import MeritShop_250814
from module.shop.ui import ShopUI


class RewardShop(ShopUI):
    def run_frequent(self):
        """
        Task ShopFrequent, the supply shop, that restocks a few times a day.
        """
        self.ui_goto_shop()
        self.device.click_record_clear()
        self.shop_nav_250814.set(NAV_GENERAL, main=self)
        self.shop_tab_250814.set(TAB_GENERAL, main=self)
        GeneralShop_250814(self.config, self.device).run()

        self.config.task_delay(server_update=True)

    def run_guild(self):
        """
        Task ShopGuild, the guild shop. It may be refreshed once and bought from again, see GuildShop.Refresh.
        """
        self.ui_goto_shop()
        self.device.click_record_clear()
        self.shop_nav_250814.set(NAV_GENERAL, main=self)
        self.shop_tab_250814.set(TAB_GUILD, main=self)
        GuildShop_250814(self.config, self.device).run()

        self.config.task_delay(server_update=True)

    def run_monthly(self):
        """
        Task ShopMonthly, the shops of the monthly tab that restock every month: core data and medals.
        """
        self.ui_goto_shop()
        self.device.click_record_clear()
        self.shop_nav_250814.set(NAV_MONTHLY, main=self)
        self.shop_tab_250814.set(TAB_CORE_MONTHLY, main=self)
        CoreShop_250814(self.config, self.device).run()

        self.device.click_record_clear()
        self.shop_nav_250814.set(NAV_MONTHLY, main=self)
        self.shop_tab_250814.set(TAB_MEDAL, main=self)
        MedalShop2_250814(self.config, self.device).run()

        self.config.task_delay(server_update=True)

    def run_once(self):
        """
        Task ShopOnce, the merit shop.
        """
        self.ui_goto_shop()
        self.device.click_record_clear()
        self.shop_nav_250814.set(NAV_GENERAL, main=self)
        self.shop_tab_250814.set(TAB_MERIT, main=self)
        MeritShop_250814(self.config, self.device).run()

        self.config.task_delay(server_update=True)


if __name__ == '__main__':
    self = RewardShop('alas')
    self.device.screenshot()
    self.run_once()
