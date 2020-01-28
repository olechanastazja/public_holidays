from django.db import models

'''
PublicHoliday (lokalna nazwa święta, angielska nazwa święta, data święta, id_country)
Country (lokalna nazwa kraju, angielska nazwa kraju, kod kraju)
'''


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
        constraints = [
            models.UniqueConstraint(fields=['holiday_date', 'local_name'], name='unique holiday')
        ]