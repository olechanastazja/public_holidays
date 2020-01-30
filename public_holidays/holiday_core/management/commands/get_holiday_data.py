from django.core.management.base import BaseCommand, CommandError
from holiday_core.models import PublicHoliday, Country
import urllib.request, json
from django.db import IntegrityError
from django.conf import settings


class Command(BaseCommand):
    help = 'Gets data about public holidays'

    def handle(self, *args, **options):
        source_url = settings.HOLIDAY_API_URL
        years = settings.YEARS
        countries = Country.objects.all()
        all_urls = []
        for country in countries:
            country_code = country.code
            # [all_urls.append(f"{source_url}/{year}/{country_code}") for year in years]
            for year in years:
                with urllib.request.urlopen(f"{source_url}/{year}/{country_code}") as url:
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