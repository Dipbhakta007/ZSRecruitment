# Create API endpoints which allow clients to access the models created in address_book app
#
# (c) 2021 Dip Bhakta, Uttara, Dhaka
# email bhaktadip@gmail.com
# phone +8801725652782

from rest_framework import generics
from address_book.models import Country,State,Address
from .serializers import AddressDetailSerializer, AddressSerializer, CountrySerializer, StateSerializer
from django_filters.rest_framework import DjangoFilterBackend



class CountryList(generics.ListAPIView):
    """View list of all countries"""

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'code']                                    # Provide option for filtering countries by country name and country ISO code




class StateList(generics.ListAPIView):
    """View list of all states of a country"""

    serializer_class = StateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']                                             # Provide option for filtering states by state name

    def get_queryset(self):
        """Return list of all states of a specific country"""

        country_code=self.kwargs['country_code']                                 # Get the country code from the url
        queryset = State.objects.filter(country__code__exact=country_code)
        return queryset




class AddressList(generics.ListAPIView):
    """View list of all addresses of a state"""

    serializer_class = AddressSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['house_number','road_number']                        # Provide option for filtering addresses by house number and road number

    def get_queryset(self):
        """Return list of all addresses of specific state"""

        state_name=self.kwargs['state_name']                                      # Get the state name from the url
        queryset = Address.objects.filter(state__name__exact=state_name)
        return queryset




class AddressDetail(generics.RetrieveAPIView):
    """View a detailed address"""

    queryset = Address.objects.all()
    serializer_class= AddressDetailSerializer

