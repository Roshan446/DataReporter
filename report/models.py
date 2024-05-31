from django.db import models


# Create your models here.


class Report(models.Model):
    date = models.DateField()
    accno = models.CharField(max_length = 100)
    cust_state = models.CharField(max_length=100)
    cust_pin = models.CharField(max_length = 100)
    dpd = models.IntegerField()


class ExcelFile(models.Model):
    file = models.FileField(upload_to="file")


