## ZSRecruitment

This is a Python developer assignmet in the recruitment process of ZS Solutions Limited. This a project to provide some API's for stored adresses. Every address is associated with a state and every state is associated with a country.

### API Endpoints

**You must be authenticated to access the API's**

* **/api/countries/** - This API provides list all countries, with the option to filter countries by name and code. **Example Response**
*
* **/api/states/<<str:country_code>>/** - This API provides list of all states by countries, with the option to filter states by name. You have to place a country ISO code in place of <<str:country_code>> to get the list of all states of that country. ( **For example**, if there is a country named 'United States of America' and its ISO code is 'US', then to get the list of all states of 'United States of America', the endpoint will be **/api/states/US/** ) 
