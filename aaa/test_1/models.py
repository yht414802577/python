from django.db import models

# Create your models here.
'''
class Many(models.Model):
    id = models.AutoField(primary_key=True)
    newcationn = models.CharField(max_length=10)
    acctive = models.CharField(max_length=4)
 '''
class Money(models.Model):
	'''
		一个类的编写就是一个表
	'''
	NewClients = models.CharField(max_length=10)
	TotalSales = models.CharField(max_length=10)
	TodayProfit = models.CharField(max_length=10)
	NewInvoice = models.CharField(max_length=10)

class people(models.Model):
    company = models.CharField(max_length=10)
    username = models.CharField(max_length=10)
    emailaddress = models.CharField(max_length=10)
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    address = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    postalcode = models.CharField(max_length=10)


    
