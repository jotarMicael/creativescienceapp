
from django.db import models

# Create your models here.

class TimeRestriction(models.Model):
    name=models.CharField(blank=False,null=False,max_length=10)
    date_from=models.DateField(blank=True,null=True,max_length=10)
    date_to=models.DateField(blank=True,null=True,max_length=10)
    
    class Meta:
        verbose_name='TimeRestriction'
        verbose_name_plural="TimesRestrictions"
        db_table='time_restriction'

    def __str__(self):
        return f'{self.name},{self.dates}'  