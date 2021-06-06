# Create Factories
#
# (c) 2021 Dip Bhakta, Uttara, Dhaka
# email bhaktadip@gmail.com
# phone +8801725652782

import factory
from address_book.models import Country,State,Address
from faker import Faker
from django.contrib.auth.models import User

fake=Faker()

class CountryFactory(factory.django.DjangoModelFactory):
    """Factory for Country model of address_book"""
    class Meta:
        model = Country

    name = factory.LazyAttribute(lambda _: fake.country())
    latitude = -55.6821445
    longitude = 178.456887
    code = factory.LazyAttribute(lambda _: fake.country_code())




class StateFactory(factory.django.DjangoModelFactory):
    """Factory for State model of address_boook"""
    class Meta:
        model = State

    name = factory.LazyAttribute(lambda _: fake.pystr())
    country = factory.SubFactory(CountryFactory)




class AddressFactory(factory.django.DjangoModelFactory):
    """Factory for Address model of address_book"""
    class Meta:
        model = Address

    name = factory.LazyAttribute(lambda _: fake.name())
    house_number = factory.LazyAttribute(lambda _: fake.postcode())
    road_number = factory.LazyAttribute(lambda _: fake.random_digit_not_null())
    state = factory.SubFactory(StateFactory)




class UserFactory(factory.django.DjangoModelFactory):
    """Factory for django's User model"""
    class Meta:
        model = User

    username = 'abcd'
    password = 'abcd1234'
    is_superuser = False
    is_staff = False
    is_active = True




