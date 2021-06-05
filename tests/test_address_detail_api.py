# Create tests for the detailed view of a address with respective state and country API at /api/address-detail/<int: pk>
#
# (c) 2021 Dip Bhakta, Uttara, Dhaka
# email bhaktadip@gmail.com
# phone +8801725652782

import pytest
import json

endpoint = '/api/address-detail/'

@pytest.mark.django_db
def test_retrieve_authenticated(address_factory, user_factory, api_client):
    """test the get request to view a detailed address with respective state and country identified by its id when authenticated"""

    user=user_factory.build()
    address = address_factory.create()
    api_client.force_authenticate(user=user)

    expected_json= {
        'id': address.id,
        'name': address.name,
        'house_number': address.house_number,
        'road_number': address.road_number,
        'state': {
            'id': address.state.id,
            'name': address.state.name,
            'country': {
                'id': address.state.country.id,
                'name': address.state.country.name,
                'latitude': address.state.country.latitude,
                'longitude': address.state.country.longitude,
                'code': address.state.country.code
            }
        }
    }

    url=endpoint+str(address.id)+"/"
    response = api_client.get(url)
    actual_json=json.loads(response.content)  # Actual json sent by the API

    assert response.status_code == 200
    assert actual_json == expected_json




@pytest.mark.django_db
def test_retrieve_not_authenticated(address_factory, api_client):
    """test the get request to view a detailed address with respective state and country identified by its id when not authenticated"""

    address = address_factory.create()

    url=endpoint+str(address.id)+"/"
    response = api_client.get(url)
    
    assert response.status_code == 403
    