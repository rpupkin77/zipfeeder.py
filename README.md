## Synopsis

This module connects your python application with ZipFeeder.us' zip code API. This API provides access to United Sates zip/postal code information. ZipFeeder.us offers a free tier where users can run 25,000 zip code lookups per month.

## Free Zipfeeder.us Account is Required
In order to use this module you must create an account with [ZipFeeder.us](https://zipfeeder.us).
ZipFeeder.us is a [json zip code api](https://zipfeeder.us/pricing) with free and paid account levels. The free level is suitable for most small applications and allows 25,000 zip code lookups each month.
To get started, create a [ZipFeeder.us account here](https://zipfeeder.us).

## Installation
The easiest way to install is though pypi ```pip install zipfeeder``` but you can also download the source or clone from the [git repository](https://github.com/rpupkin77/zipfeeder.py).
## Code Example

Once you have zipfeeder setup, you use it like so:

```
from zipfeeder import ZipFeeder

# replace with your key
zf = ZipFeeder('MY_ZF_KEY')

zip_code = zf.zipcode('01950')

# will output "Newburyport"
print zip_code.city
```

For a full list of API calls, visit the [ZipFeeder Documentation](https://zipfeeder.us/static/documentation/index.html).

## Motivation

This module exists to give Python developers a quick and easy way to integrate US Zip Code data into their applications. ZipFeeder.us provides a easy to use API that very developer friendly.


## Object Reference

This section covers the Class API of this python module for the actual "low level" REST API interface of Zipfeeder.us, please check out their [API documentation](https://zipfeeder.us/static/documentation/index.html). For detailed information on the ZipFeeder module, please take a look at the [source code](https://github.com/rpupkin77/zipfeeder.py)

#### Initializing the ZipFeeder Object

To initialize the ZipFeeder object, first import the ZipFeeder class ```from zipfeeder import ZipFeeder``` then in your code, create a ZipFeeder instance like so ```zf = ZipFeeder('mykey')``` where 'mykey' is the key you received when you signed you signed up for the service.

#### Object Method Reference
Once you have initialized an object you can begin calling the object methods like so (assumes your ZipFeeder object is 'zf'):

**zipcode(self, zip)** - This method will return data for the zip code submitted as 'zip'. The zip argument should be a string. Example Usage: ```zf.zip_code('01950')```

**zipcodes(self, zips)** Returns zipcode data for up to 5 zip codes passed as a list. Example Usage: ```zf.zip_codes(['01950, 02124'])```

**nearby_zips(self, zip, radius=10) (Premium accounts only)** Returns abridged zipcode for zipcodes within a provided radius of another zipcode: ```zf.nearby_zips('01950', 15)```

**zipcodes_startwith(self, zip_part) (Premium accounts only)** Returns Zip Codes that start with the provided string: ```zf.zipcodes_startwith('019')```

**zipcodes_by_state(self, state, city_filter=None) (Premium accounts only)** Returns zipcodes in a state, optionally filtered by a city string: ```zf.zipcodes_by_state('MA', 'newbury')```

## Tests

If you wish to submit a pull request or testa ny changes you have made locally, you can do so by running tests.py in the root of teh app. You will need to provide your own key for testing. 

## Contributors

If you wish to improve or fork this project, feel free, not all pull requests will be accepted.

## License

This software is licensed under the [Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0), for a brief overview of what this means in regards to this software - or if you are not a lawyer - please see [this link](https://tldrlegal.com/license/apache-license-2.0-(apache-2.0)).