# Create the models of adress_book app
# These models will be accessed through the REST API endpoints
#
# (c) 2021 Dip Bhakta, Uttara, Dhaka
# email bhaktadip@gmail.com
# phone +8801725652782

from django.db import models

class Country(models.Model):
    """Define a country"""

    name = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    code = models.CharField(max_length=2)                             # ISO code for the country. A list of comprehensive country iso codes canbe found here: https://countrycode.org/

    def __str__(self):
        return self.name



class State(models.Model):
    """Define a state of a country"""

    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)    # Associate each state with a country 

    def __str__(self):
        return self.name



class Address(models.Model):
    """Define the specific Address"""

    name = models.CharField(max_length=100)
    house_number = models.CharField(max_length=50)
    road_number = models.IntegerField()
    state= models.ForeignKey(State, on_delete=models.CASCADE)         # Associate each address with a state

    def __str__(self):
        return self.name