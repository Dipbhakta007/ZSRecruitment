# Set the url configurations of address_book_api app
# These urls will provide the API endpoints
#
# (c) 2021 Dip Bhakta, Uttara, Dhaka
# email bhaktadip@gmail.com
# phone +8801725652782

from django.urls import path
from .views import AddressDetail, CountryList, StateList, AddressList
from rest_framework.schemas import get_schema_view

app_name='address_book_api'

urlpatterns = [
    path('countries/', CountryList.as_view(), name='countrylistcreate'),                 # Url to get list of all countries
    path('states/<str:country_code>/', StateList.as_view(), name='statelistcreate'),     # Url to get list of all states of the country specified in the url by country ISO code (https://countrycode.org/)
    path('addresses/<str:state_name>/', AddressList.as_view(), name='addresslistcreate'),# Url to get list of addresses of the state specified in the url by the state name
    path('address-detail/<int:pk>/', AddressDetail.as_view(), name='addressdetailview'), # Url to get a detailed view of a specific address specified in the url by its id
    path('schema/', get_schema_view(title='ZSRecruitment', description='Project for ZS Solutions Recruitment Process', version='1.0.0'), name='openapi-schema')
]