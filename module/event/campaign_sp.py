from module.campaign.stage import stage_names
from module.config.config import TaskEnd
from module.event.base import EventBase
from module.logger import logger


class CampaignSP(EventBase):
    def run(self, *args, **kwargs):
        if 'sp' not in stage_names(self.config.Campaign_Event):
            logger.info(f'{self.config.Campaign_Event} has no stage sp')
            logger.info(f'This event do not have SP, skip')
            self.config.Scheduler_Enable = False
            self.config.task_stop()

        try:
            super().run(name=self.config.Campaign_Name, folder=self.config.Campaign_Event, total=1)
        except TaskEnd:
            # Catch task switch
            pass
        if self.run_count > 0:
            self.config.task_delay(server_update=True)
        else:
            self.config.task_stop()
