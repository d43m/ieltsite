from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    cid = models.IntegerField()  # country id at council site #
    currency = models.CharField(max_length=10)
    last_seen = models.DateTimeField()

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    cid = models.CharField(max_length=100)  # city name at council site #
    last_seen = models.DateTimeField()

class Date(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateField()
    module = models.CharField(max_length=1)  # [A]cademic, [G]eneral Training #
    fee = models.DecimalField(max_digits=9, decimal_places=2)
    last_seen = models.DateTimeField()
    available = models.IntegerField()


