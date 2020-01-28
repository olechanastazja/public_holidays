from django.core.management.base import BaseCommand, CommandError
from holiday_core.models import PublicHoliday, Country
import urllib.request, json
from django.db import IntegrityError


class Command(BaseCommand):
    help = 'Gets data about public holidays'

    # def add_arguments(self, parser):
        # parser.add_argument('country_id', nargs='+', type=int)
        # parser.add_argument('year', nargs='+', type=int)

    def handle(self, *args, **options):
        year = '2020'
        country_code = 'PL'
        country = Country.objects.get(pk=1)
        with urllib.request.urlopen(f"https://date.nager.at/api/v2/PublicHolidays/{year}/{country_code}") as url:
            data = json.loads(url.read().decode())
            for holiday in data:
                holiday_data = {
                    'local_name': holiday.get('localName'),
                    'english_name': holiday.get('name'),
                    'holiday_date': holiday.get('date'),
                    'country': country
                }
                try:
                    PublicHoliday.objects.create(**holiday_data)
                except IntegrityError:
                    self.stdout.write(self.style.WARNING('That holiday already in database'))

            self.stdout.write(self.style.SUCCESS('Successfully obtained holiday data'))