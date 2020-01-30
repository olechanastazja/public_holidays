from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from holiday_core import views


CODE = getattr(settings, 'DEFAULT_COUNTRY', 'PL')
YEAR = getattr(settings, 'DEFAULT_YEAR', 2020)

urlpatterns = [
    path('admin/', admin.site.urls),

    path(route='',
         view=views.HolidaysCountryYear.as_view(),
         kwargs={'code': CODE, 'year': YEAR},  # pass defaults when no kwargs
         name='main_view'),

    path(route='<str:code>/<int:year>/',
         view=views.HolidaysCountryYear.as_view(),
         name='main_view'),
]

# serve static files in templates
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )