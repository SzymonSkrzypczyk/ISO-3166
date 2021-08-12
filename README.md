# ISO CODES
It's a simple, yet helpful module facilitating usage of <a href='https://en.wikipedia.org/wiki/ISO_3166-1'>ISO-3166</a> country codes

## Installation
ISO CODES is available on <a href='https://pypi.org/'>PYPI</a>

````
pip install iso_codes
````

## Usage

To show all the available coutry codes:
````python
from iso3166 import iso
iso = iso.ISO()
print(iso.codes)
````
To check whether a country code exists:
````python
from iso3166 import iso
iso = iso.ISO()
print(iso.check('CODE'))
````
To get country details by name:
````python
from iso3166 import iso
iso = iso.ISO()
print(iso.get_name('NAME'))
````
To get country details by code:
````python
from iso3166 import iso
iso = iso.ISO()
print(iso.find('CODE'))
````

To use cli app:
````bash
$iso
Usage: __main__.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  check           Checks if a provided code is correct
  find            Shows a country based on a country's code
  find-name       Shows a country based on a name
  show-countries  Shows a list of all(249) available countries

Process finished with exit code 0

````
