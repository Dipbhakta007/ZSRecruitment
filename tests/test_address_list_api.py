# Create tests for the address list API at /api/state/<str: state_name>
#
# (c) 2021 Dip Bhakta, Uttara, Dhaka
# email bhaktadip@gmail.com
# phone +8801725652782
import pytest
import json

endpoint = '/api/addresses/'

@pytest.mark.django_db
def test_list_authenticated(address_factory, user_factory, api_client):
    """test the get request to view the list of addresses of a state identified by the state name in the url when authenticated"""

    user=user_factory.build()
    addresses = address_factory.create_batch(10)
    api_client.force_authenticate(user=user)
    expected_length=0                                                   # expected length of the respone for the state name of the first address instance in the url   

    for address_instance in addresses:                                  # Determine the expected lengths for the specific state name or check how many instances have the same state name as the first instance
        if address_instance.state.name == addresses[0].state.name:
            expected_length=expected_length+1
      
    url=endpoint + addresses[0].state.name+"/"                           # Get the url by adding state name to endpoint url
    response = api_client.get(url)
    actual_length=len(json.loads(response.content))

    assert response.status_code == 200
    assert actual_length == expected_length




@pytest.mark.django_db
def test_list_not_authenticated(address_factory, api_client):
    """test the get request to view the list of addresses of a state identified by the state name in the url when not authenticated"""

    addresses = address_factory.create_batch(10)   
    url=endpoint + addresses[0].state.name+"/"                           # Get the url by adding state name to endpoint url
    response = api_client.get(url)

    assert response.status_code == 403




@pytest.mark.django_db
@pytest.mark.parametrize('field',[('house_number'),('road_number')])
def test_search(address_factory, user_factory, api_client,field):
    """test the search option for house number and road number of the addresses"""

    user=user_factory.build()
    addresses = address_factory.create_batch(10)
    api_client.force_authenticate(user=user)
    
    expected_length_house_number=0                                       # expected length of the respone for the specific state and house number of the first state instance
    expected_length_road_number=0                                        # expected length of the respone for the specific state and road number of the first state instance

    for address_instance in addresses:                                   
        if address_instance.state.name == addresses[0].state.name:
            if  address_instance.house_number == addresses[0].house_number: # Determine the expected lengths for the specific state name and house number or check how many instances have the same state name & house number as the first instance
                expected_length_house_number= expected_length_house_number+1

            if  address_instance.road_number == addresses[0].road_number:   # Determine the expected lengths for the specific state name and road number or check how many instances have the same state name & road number as the first instance
                expected_length_road_number= expected_length_road_number+1


    if field == 'house_number':                                          # For house number, search by entering the house number in url. Same for road number
        url=endpoint+addresses[0].state.name+'/?house_number='+addresses[0].house_number
        response = api_client.get(url)
        actual_length_house_number=len(json.loads(response.content))
        assert response.status_code == 200
        assert actual_length_house_number == expected_length_house_number

    else:
        url=endpoint+addresses[0].state.name+'/?road_number='+str(addresses[0].road_number)
        response = api_client.get(url)
        actual_length_road_number=len(json.loads(response.content))
        assert response.status_code == 200
        assert actual_length_road_number == expected_length_road_number