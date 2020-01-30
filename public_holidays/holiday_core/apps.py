from django.apps import AppConfig
from django.core.management import call_command


class HolidayCoreConfig(AppConfig):
    name = 'holiday_core'

    def ready(self):
        call_command('get_holiday_data')
