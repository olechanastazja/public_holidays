from django.shortcuts import render
from .models import PublicHoliday
from django.http import HttpResponse


def index(request):
    holidays = PublicHoliday.objects.all()
    context = {'holidays': holidays}
    return render(request, 'holiday_core/index.html', context)
