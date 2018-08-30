from django.db import models

# Create your models here.

class Money(models.Model):

    DakotaRiceSalary = models.CharField(max_length=10)
    MinervaHooperSalary = models.CharField(max_length=10)
