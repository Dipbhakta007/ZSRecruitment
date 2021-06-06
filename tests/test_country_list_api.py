# Create tests for the Country list API at /api/countries/
#
# (c) 2021 Dip Bhakta, Uttara, Dhaka
# email bhaktadip@gmail.com
# phone +8801725652782
import pytest
import json

endpoint = '/api/countries/'

@pytest.mark.django_db
def test_list_authenticated(country_factory, user_factory, api_client):
    """test the get request to view the list of countries when client is authenticated"""

    user = user_factory.build()
    country_factory.create_batch(10)
    api_client.force_authenticate(user=user)

    response = api_client.get(endpoint)

    assert response.status_code == 200
    assert len(json.loads(response.content)) == 10




@pytest.mark.django_db
def test_list_not_authenticated(country_factory, api_client):
    """test the get request to view the list of countries when client is not authenticated"""

    country_factory.create_batch(10)
    response = api_client.get(endpoint)
    assert response.status_code == 403
  



@pytest.mark.django_db
@pytest.mark.parametrize('field',[('name'),('code')])
def test_search(country_factory, user_factory, api_client, field):
    """test the search option for name and code of the country"""

    user = user_factory.build()
    countries = country_factory.create_batch(10)
    api_client.force_authenticate(user=user)

    expected_length_name=0                                      # expected length of the respone for the name of the first country instance
    expected_length_code=0                                      # expected length of the respone for the code of the first country instance

    for country_instance in countries:                          # Determine the expected lengths for name and code or check how many instances have the same name or code as the first instance
        if country_instance.name == countries[0].name:
            expected_length_name=expected_length_name+1
        
        if country_instance.code == countries[0].code:
             expected_length_code= expected_length_code+1


    if field == 'name':                                         # For name, search by entering the country name in url. Same for country code 
        url=endpoint+'?'+field+'='+countries[0].name
        response = api_client.get(url)
        actual_length_name=len(json.loads(response.content))
        assert response.status_code == 200
        assert actual_length_name == expected_length_name

    else:
        url=endpoint+'?'+field+'='+countries[0].code
        response = api_client.get(url)
        actual_length_code=len(json.loads(response.content))
        assert response.status_code == 200
        assert actual_length_code == expected_length_code

  


