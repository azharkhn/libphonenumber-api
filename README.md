# Introduction
This is a python based API wrapped from Google libphonenumber library.
* These services are developed get updated details of phonenumbers.
* The result is in JSON and valid-flag signifies whether phonenumber is valid or not i.e. 1 or 0 respectively.
* Number can be provided in any format i.e. with spaces, characters etc.
* Phonenumber’s Length must be within range of 4 to 20.

# Dependencies
## Python 
```
# apt-get install python-pip
# pip install phonenumbers flask dicts
```
API Services can directly be run by following command:
```
# python libphonenumber-api/phonenumber/__init__.py &
```
## Apache
```
# apt-get install libapache2-mod-wsgi
```
# Apache Configuration
Create a Virtual host to access this API in apache
```
<VirtualHost *:80>
		ServerName example.com
		ServerAdmin support@example.com
		ServerAlias phonenumber.example.com
                WSGIScriptAlias / /home/example.com/libphonenumber-api/phonenumber.wsgi
		<Directory /home/example.com/libphonenumber-api/phonenumber/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error_phonenumber.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access_phonenumber.log combined
</VirtualHost>
```
# Services

## Getting Phonenumber’s Information
### Phone Number
```
# curl http://phonenumber.example.com/phonenumber?number=+45(3)216-0398
4532160398
```
### Phonenumber’s Type
```
# curl http://phonenumber.example.com/type?number=4532160398
{"type": "FIXED_LINE_OR_MOBILE", "valid-flag": 1}
```
### Phonenumber’s Country Code
```
# curl http://phonenumber.example.com/countrycode?number=4532160398
{"countrycode": "45", "valid-flag": 1}
```
### Phonenumber’s National Significant Number
```
# curl http://phonenumber.example.com/nsn?number=4532160398
{"nsn": "32160398", "valid-flag": 1}
```
## Phonenumber’s Country’s ISO Code

### ISO Code in 2 Alphabets
```
# curl http://phonenumber.example.com/iso2?number=4532160398
{"iso": "DK", "valid-flag": 1}
```
### ISO Code in 3 Alphabets
```
# curl http://phonenumber.example.com/iso3?number=4532160398
{"iso": "DNK", "valid-flag": 1}
```

## Phonenumber’s Regional Operator
```
# curl http://phonenumber.example.com/operator?number=4532160398
{"operator": "Telenor", "valid-flag": 1}
```
Note: Operator’s Names are available in different languages with param i.e. operator-en, operator-fr, operator-it, operator-de.

## Phonenumber’s Country
```
# curl http://phonenumber.example.com/country?number=4532160398
{"country": "Denmark", "valid-flag": 1}
```
## Phonenumber’s Location
```
# curl http://phonenumber.example.com/location?number=4532160398
{"country": "Denmark", "valid-flag": 1}
```
Note: Location Names are available in different languages with param i.e. location-en, location-fr, location-it, location-de.

## Phonenumber’s TimeZone
```
# curl http://phonenumber.example.com/timezone?number=4532160398
{"timezone": ["valid-flag": 1}
```
## All details in JSON
```
# curl http://phonenumber.example.com/details?number=004532160398
{
 "phonenumber": "4532160398",
 "code": "45",
 "nsn": "32160398",
 "typeid": "FIXED_LINE_OR_MOBILE",
 "operator": "Telenor",
 "iso3": "DNK",
 "iso2": "DK",
 "country": "Denmark",
 "timezone": ["Europe/Copenhagen"]("Europe/Copenhagen"],),
 "is_validnumber": true,
 "is_validnumberforRegion": true,
 "is_possiblenumber": true
 }
```
## Phone Number FORMATs
### E164 Format
```
# curl http://phonenumber.example.com/E164-format?number=4532160398
+4532160398
```
### Without E164 Format
```
# curl http://phonenumber.example.com/without-E164-format?number=004532160398
4532160398
```
### National Format
```
# curl http://phonenumber.example.com/national-format?number=004532160398
32 16 03 98
```
### International Format
```
# curl http://phonenumber.example.com/international-format?number=004532160398
+45 32 16 03 98
```
## Verifying Phonenumber
```
# curl http://phonenumber.example.com/validate?number=4532160398
{"valid-flag": 1}
```
