"""
Generic views for holiday app
"""

# pylint: disable=no-member
from django.views.generic.list import ListView

from .models import (
    PublicHoliday,
    Country
)


class HolidaysCountryYear(ListView):
    # pylint: disable=too-many-ancestors
    """
    View delivers holiday list data
    accordingly to passed url parameters (path variables)
    """

    model = PublicHoliday
    template_name = 'holiday_core/index.html'
    context_object_name = 'holidays'

    def get_queryset(self):
        """
        Returns queryset filtered with url parameters
        """
        code = self.kwargs['code'].upper()
        year = self.kwargs['year']
        country_id = Country.objects.get(code=code).id
        query = PublicHoliday.objects.filter(
            country_id=country_id,
            holiday_date__year=year
        )
        return query

    def get_context_data(self, **kwargs):
        # pylint: disable=arguments-differ
        """
        Passes to template url kwargs
        When kwargs are not passed in url,
        context passes default values (see urls.py)
        """
        context = super().get_context_data(**kwargs)
        context['code'] = self.kwargs['code']
        context['year'] = self.kwargs['year']
        return context
