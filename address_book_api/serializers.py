# Create Serializers for the API endpoints of address_book_api
# Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types
# Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data
#
# (c) 2021 Dip Bhakta, Uttara, Dhaka
# email bhaktadip@gmail.com
# phone +8801725652782


from rest_framework import serializers
from address_book.models import Country,State,Address


class CountrySerializer(serializers.ModelSerializer):
    """Create Serializer for the API to provide list of all countries"""

    class Meta:
        model = Country
        fields = '__all__'                                                   # Get all fields of the Country model 




class StateSerializer(serializers.ModelSerializer):
    """Create Serializer for the API to provide list of all states by countries"""

    class Meta:
        model = State
        fields = '__all__'                                                    # Get all fields of the State model




class AddressSerializer(serializers.ModelSerializer):
    """Create Serializer for the API to provide list of all addresses by states"""

    class Meta:
        model = Address
        fields = '__all__'                                                    # Get all fields of the Address model




class AddressDetailSerializer(serializers.ModelSerializer):
    """Create Serializer for the API to provide detailed view of a specific address"""

    class Meta:
        model = Address
        fields = ['id', 'name', 'house_number', 'road_number','state']
        depth=2                                                               # Set the depth of relationships that should be traversed to get the detaied state and country of the address


