# Define the fixture functions in this file to make them accessible across multiple test files
# Register the factories
#
# (c) 2021 Dip Bhakta, Uttara, Dhaka
# email bhaktadip@gmail.com
# phone +8801725652782


import pytest
from pytest_factoryboy import register
from tests.factories import CountryFactory, StateFactory, AddressFactory
from rest_framework.test import APIClient



register(CountryFactory)
register(StateFactory)
register(AddressFactory)



@pytest.fixture
def api_client():
    client = APIClient()  # Create an api client to access the api's
    return client