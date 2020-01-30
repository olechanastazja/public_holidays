from django.core.management.base import BaseCommand
from holiday_core.models import PublicHoliday, Country
import urllib.request, json
from django.db import IntegrityError
from django.conf import settings
import itertools


class Command(BaseCommand):
    help = 'Gets data about public holidays'

    def handle(self, *args, **kwargs):
        """
        Command downloads from url holiday data,
        organize data to dictionary,
        creates model and uploads to db
        """
        source_url = getattr(settings, 'HOLIDAY_API_URL')
        years = getattr(settings, 'YEARS', [2020, 2021, 2022])
        countries = Country.objects.all()

        for country, year in itertools.product(countries, years):
            country_code = country.code

            with urllib.request.urlopen(
                    f'{source_url}/{year}/{country_code}') as url:
                data = json.loads(url.read().decode())

                for holiday in data:
                    holiday_data = create_holiday_dict(holiday, country)
                    try:
                        PublicHoliday.objects.create(**holiday_data)
                    except IntegrityError:
                        pass

        self.stdout.write(
            self.style.SUCCESS('Successfully obtained holiday data')
        )


def create_holiday_dict(holiday, country):
    holiday_data = {
        'local_name': holiday.get('localName'),
        'english_name': holiday.get('name'),
        'holiday_date': holiday.get('date'),
        'country': country
    }
    return holiday_data
