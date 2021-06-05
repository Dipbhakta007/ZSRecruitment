# Create tests for the state list API at /api/state/<str: coutntry_code>
#
# (c) 2021 Dip Bhakta, Uttara, Dhaka
# email bhaktadip@gmail.com
# phone +8801725652782
import pytest
import json

endpoint = '/api/states/'

@pytest.mark.django_db
def test_list(state_factory, api_client):
    """test the get request to view the list of states of a country identified by the country code in the url"""

    states = state_factory.create_batch(10)
    expected_length=0                                                   # expected length of the respone for the country code of the first state instance in the url
   

    for state_instance in states:                                       # Determine the expected lengths for the specific country code or check how many instances have the same country code as the first instance
        if state_instance.country.code == states[0].country.code:
            expected_length=expected_length+1
    


    
    url=endpoint + states[0].country.code+"/"                           # Get the url by adding country code to endpoint url
    response = api_client.get(url)

    assert response.status_code == 200

    actual_length=len(json.loads(response.content))
    assert actual_length == expected_length




@pytest.mark.django_db
def test_search(state_factory, api_client):
    """test the search option for name of the state"""
    states = state_factory.create_batch(10)
    
    expected_length_name=0                                              # expected length of the respone for the specific country and name of the first state instance
   
    for state_instance in states:                                       # Determine the expected lengths for the specific country and name or check how many instances have the same country code & name as the first instance
        if state_instance.country.code == states[0].country.code:
            if  state_instance.name == states[0].name:
                expected_length_name= expected_length_name+1
        
                                             
    url=endpoint+states[0].country.code+"/?name="+states[0].name        # Get the url by adding country code to endpoint url and adding state name as a search option
    response = api_client.get(url)
    actual_length_name=len(json.loads(response.content))
    assert actual_length_name == expected_length_name

    

    