from django.shortcuts import render
from django.shortcuts import redirect
from .models import PublicHoliday, Country
from django.views.generic.list import ListView
from django.conf import settings


def index(request):
    default_country = Country.objects.get(code=settings.DEFAULT_COUNTRY)
    default_year = settings.DEFAULT_YEAR
    return redirect('main_view', country_id=default_country.id, year=default_year)


class HolidaysCountryYear(ListView):

    model = PublicHoliday
    template_name = 'holiday_core/index.html'
    context_object_name = 'holidays'

    def get_queryset(self):
        country_id = self.kwargs['country_id']
        year = self.kwargs['year']
        qs = PublicHoliday.objects.filter(
            country_id=country_id,
            holiday_date__year=year
        )
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country_id'] = self.kwargs['country_id']
        context['year'] = self.kwargs['year']
        return context