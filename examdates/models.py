from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    cid = models.IntegerField()  # country id at council site #
    currency = models.CharField(max_length=10)
    last_seen = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    venue = models.CharField(null=True, max_length=300)
    cid = models.CharField(max_length=100)  # city name at council site #
    last_seen = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class Date(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateField()
    module = models.CharField(max_length=1)  # [A]cademic, [G]eneral Training #
    fee = models.DecimalField(max_digits=9, decimal_places=2)
    last_seen = models.DateTimeField(null=True)
    available = models.IntegerField()

    def __str__(self):
        return "{0.country.name:s} / {0.city.name:s} {0.date:%Y-%m-%d}".format(
            self)
