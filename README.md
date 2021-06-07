## ZSRecruitment

This is a Python developer assignmet in the recruitment process of ZS Solutions Limited. This a project to provide some API's for stored adresses. Every address is associated with a state and every state is associated with a country.

### API Endpoints

**You must be authenticated to access the API's**. You can check the API schema at **/api/schema/**

* **/api/countries/** - This API provides list all countries, with the option to filter countries by name and code.<br/> <br/>**Example Response**
![coutry_list_api](https://github.com/Dipbhakta007/ZSRecruitment/blob/main/api_screenshots/country_list_api.JPG)
* **/api/states/{country_code}/** - This API provides list of all states by countries, with the option to filter states by name. You have to place a country ISO code in place of {country_code} to get the list of all states of that country. ( **For example**, if there is a country named 'United States of America' and its ISO code is 'US', then to get the list of all states of 'United States of America', the endpoint will be **/api/states/US/** ) <br/> <br/>**Example Response**
![state_list_api](https://github.com/Dipbhakta007/ZSRecruitment/blob/main/api_screenshots/state_list_api.JPG)
* **/api/addresses/{state_name}/** - This API provides list of all addresses of states, with the option to filter addresses by house_number and road_number. You have to place a state name in place of {state_name} to get the list of all addresses of that state. ( **For example**, if there is a state named 'California', then to get the list of all addresses of 'California', the endpoint will be **/api/states/California/** ) <br/> <br/>**Example Response**
![address_list_api](https://github.com/Dipbhakta007/ZSRecruitment/blob/main/api_screenshots/address_list_api.JPG)
* **/api/address-detail/{address_id}/** - This API provides detailed view of an address with it’s respective state and country identified by its id. ( **For example**, if there is an address which has id 1, then to get detailed view of that address, the endpoint will be **/api/address-detail/1/** ) <br/> <br/>**Example Response**
![address_detail_api](https://github.com/Dipbhakta007/ZSRecruitment/blob/main/api_screenshots/address_detail_api.JPG)

### Test Case Scenarios

* Test the GET request to view the list of all countries when client is authenticated
* Test the GET request to view the list of all countries when client is not authenticated
* Test the search by name of a country in the GET request to view the list of all countries
* Test the search by code of a country in the GET request to view the list of all countries
* Test the GET request to view the list of all states of a country when client is authenticated
* Test the GET request to view the list of all states of a country when client is not authenticated
* Test the search by name of a state in the GET request to view the list of all states of a country
* Test the GET request to view the list of all addresses of a state when client is authenticated
* Test the GET request to view the list of all addresses of a state when client is not authenticated
* Test the search by house number in the GET request to view the list of all addresses of a state
* Test the search by road number in the GET request to view the list of all addresses of a state
* Test the GET request to view a detailed address when client is authenticated
* Test the GET request to view a detailed address when client is not authenticated

### Run The Project (For Windows)

1. First, clone this repository:
    - `git clone https://github.com/Dipbhakta007/ZSRecruitment.git`
    - `cd ZSRecruitment`
2. Create a Python virtual environment:
    - `py -m venv venv`
3. Activate the virtual environment.
    - `venv\Scripts\activate`
4. Install requirements:
    - `pip install -r requirements.txt`
5. Migrate the models:
    - `py manage.py migrate`
6. To run the project:
    - `py manage.py runserver`
7. To run the tests:
    - `pytest`
