# Geocoding Suite Documentation
This Geocoding Suite provides many useful Geographical Conversions, including:

 * Addresses to zipcodes
 * Addresses to city, state
 * Business Names to Latitude and Longitude
 * Business Names and States to Latitude and Longitude
 * County Fips Codes to CBSA Codes
 * Lat and Long to County Data (Fips, County Name, state, and abbv. state)
 * Zipcode to CBSA codes

Note: 1 complimentary API key is hardcoded for demo purposes, please do not abuse!

##	Specific Modules
***

### Address to Zipcode
This module has two versions for the Geopy-Style address and Google Places style address.

Geopy Style address:

			US House of Representatives, Washington, District of Columbia, 20540, United States of America

Google Places style address:

			2115 US-92, Plant City, FL 33563, USA


Requirements:

* Python 3.x

To convert an address to a zipcode:

* identify the type of address and choose the appropriate module
* clear all lines of text from zipcode.txt
* copy all addresses into addresses.txt and end with one blank line
* run the appropriate module

***

### Address to City, State
This module has two versions for the Geopy-Style address and Google Places style address. See module above for address styles.

Requirements
* Python 3.x

To convert an address to a city, state substring:
* identify the type of address and choose the appropriate module
* clear all lines of text from city_state.txt
* copy all addresses into addresses.txt
 and end on one new line
* run the appropriate module

***

### Business Names to Latitude and Longitude
This module converts business names in the United States to geographical coordinates using Google Places API. If you wish to restrict results to states, use the Business Names and States to Latitude and Longitude described in the next section.

Requirements

* Python 3.x
* [requests](http://docs.python-requests.org/en/master/) (used to parse json data)

To convert a business name to Geographical Coordinates:
* clear all lines of text from output.txt
* copy all business names into companies.txt and end on one new line
* run the module

***

### Business Names And States to Latitude and Longitude
This module converts business names in a specific US state to geographical coordinates using Google Places API.

Requirements

* Python 3.x
* [requests](http://docs.python-requests.org/en/master/) (used to parse json data)

To convert a business name to Geographical Coordinates:
* clear all lines of text from output.txt
* copy all business names into companies.txt and end on one new line
* copy all states (can be abbreviated) into states.txt and end on one new line
* run the module

***

### County FIPS to CBSA
This module converts county FIPS codes to CBSA codes using a built-in dictionary.

Requirements

* Python 3.x

Important Note:
* CBSA.txt and FIPS.txt are dictionaries and should not be modified. The program will throw an error if the dictionary is corrupt.

To convert a FIPS county code to a CBSA code
* clear all lines of text from cbsa_out.txt
* copy all fips into fips_in.txt and end on one new line
* run the module

***

### Latitude and Longitude to Address - Geopy
This module converts geographical coordinates to addresses using Geopy API. This API is limited by requests per minute instead of total number of requests like Google Places API. To avoid rate limiting, the program fetches one address per four seconds. If a faster converter is needed, use the next module.

Requirements

* Python 3.x
* [geopy](https://pypi.python.org/pypi/geopy) (API to convert coordinates to addresses)

Important Note:
* This API is rate limited. if the limit is exceeded, geopy will return an error.  
* Latitude and Longitude inputs are seperated by tabs as defualt. If you wish to change this, change DELIMITER in the module

To convert a geographical coordinate to an Address
* clear all lines of text from addresses.txt
* copy all coordinates into latAndLong.txt and end on one new line
* run the module
*

***

### Latitude and Longitude to Address - Google Places API
This module converts geographical coordinates to addresses using Google Places API. This API is limited by total number of requests per day. To avoid rate limiting, multiple API keys are commented in the program.

Requirements

* Python 3.x
* [requests](http://docs.python-requests.org/en/master/) (used to parse json data)

Important Note:
* This API is rate limited to about 1,500 requests per key per day.
* To avoid null results, check links printed by the console and ensure the json output doesnt display "API key exceeded"
* API Keys can be changed by changing the value of KEY in the code.  
* Latitude and Longitude inputs ***must*** be seperated by commas

To convert a geographical coordinate to an Address
* clear all lines of text from addresses.txt
* copy all coordinates into latAndLong.txt and end on one new line
* run the module

***

### Latitude and Longitude to County Data - FCC Database
This module converts geographical coordinates to County Fips, County Names, State Name, State Abbreviation. This Database is not rate limited

Requirements

* Python 3.x
* [requests](http://docs.python-requests.org/en/master/) (used to parse json data)

Important Note:  
* Latitude and Longitude inputs are seperated by tabs by default. To change this, change DELIMITER in the module.

To convert a geographical coordinate to County Data
* clear all lines of text from county_Fips.txt
* copy all coordinates into latAndLong.txt and end on one new line
* run the module

***

### Zipcode To CBSA
This module converts zipcodes to CBSA codes by using a built in dictionary.

Requirements

* Python 3.x


Important Note:  
* CBSA.txt and ZIPS.txt are dictionaries and should not be edited. If the dictionary becomes invalid, the program will not execute correctly.

To convert a zipcode toa CBSA code
* clear all lines of text from cbsaout.txt
* copy all zipcodes into zipcode_in and end on one new line
* run the module

***
Learn more about [Geopy](https://geopy.readthedocs.io/en/1.10.0/) and [Google Places API](https://developers.google.com/places/web-service/search)
