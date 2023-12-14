from django.db import models


class Customers(models.Model):
    ID = models.AutoField(primary_key=True)
    CustomerID = models.IntegerField()
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
