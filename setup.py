from distutils.core import setup
setup(
  name = 'zipfeeder',
  packages = ['zipfeeder'], # this must be the same as the name above
  version = '0.1',
  description = 'Uses the Zipfeeder.us API to serve free United States Zip Code information, a ZipFeeder account '
                'is required',
  author = 'Paul Thompson',
  author_email = 'info@zipfeeder.us',
  url = 'https://github.com/rpupkin77/zipfeeder.py', # use the URL to the github repo
  download_url = 'https://github.com/rpupkin77/zipfeeder.py/archive/master.zip', # I'll explain this in a second
  keywords = ['zip code', 'us zip code', 'postal code', 'zip code api'], # arbitrary keywords
  classifiers = [],
)