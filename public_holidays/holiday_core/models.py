"""
Models for Country / PublicHolidays
"""
# pylint: disable=missing-class-docstring

from django.db import models


class Country(models.Model):
    local_name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)


class PublicHoliday(models.Model):
    local_name = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200)
    holiday_date = models.DateTimeField('date of holiday')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        # pylint: disable=too-few-public-methods
        constraints = [
            models.UniqueConstraint(
                fields=['holiday_date', 'local_name'],
                name='unique holiday'
            )
        ]
