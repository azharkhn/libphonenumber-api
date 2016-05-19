#!/usr/bin/env python

from flask import Flask, request, jsonify
from lib.phonenumber import NumberDetails

app = Flask(__name__)

objPhoneNumber = NumberDetails() 

@app.route('/phonenumber', methods = ['GET'])
def get_phonenumber():
    if 'number' in request.args:
        return objPhoneNumber.remove_chars_from_phonenumber(request.args['number'])
    else:
        return 'Invalid Key'
    
'''
    Operator Information
'''
   
@app.route('/operator', methods = ['GET'])
def get_operator():
    if 'number' in request.args:
        number = request.args['number']
        if(4 <= len(number) <= 20):
            objPhoneNumber.set_phonenumber(number)
            return jsonify({'valid-flag':objPhoneNumber.validate,'operator': objPhoneNumber.get_operator()})
        else:
            return jsonify({'status':404,'valid-flag':0,'operator': ''})
    else:
        return 'Invalid Key'
    
@app.route('/operator-en', methods = ['GET'])
def get_operator_en():
    if 'number' in request.args:
        number = request.args['number']
        if(4 <= len(number) <= 20):
            objPhoneNumber.set_phonenumber(number)
            return jsonify({'valid-flag':objPhoneNumber.validate,'operator': objPhoneNumber.get_en_operator()})
        else:
            return jsonify({'status':404,'valid-flag':0,'operator': ''})
    else:
        return 'Invalid Key'
    
@app.route('/operator-fr', methods = ['GET'])
def get_operator_fr():
    if 'number' in request.args:
        number = request.args['number']
        if(4 <= len(number) <= 20):
            objPhoneNumber.set_phonenumber(number)
            return jsonify({'valid-flag':objPhoneNumber.validate,'operator': objPhoneNumber.get_fr_operator()})
        else:
            return jsonify({'status':404,'valid-flag':0,'operator': ''})
    else:
        return 'Invalid Key'
    
@app.route('/operator-it', methods = ['GET'])
def get_operator_it():
    if 'number' in request.args:
        number = request.args['number']
        if(4 <= len(number) <= 20):
            objPhoneNumber.set_phonenumber(number)
            return jsonify({'valid-flag':objPhoneNumber.validate,'operator': objPhoneNumber.get_it_operator()})
        else:
            return jsonify({'status':404,'valid-flag':0,'operator': ''})
    else:
        return 'Invalid Key'
    
@app.route('/operator-de', methods = ['GET'])
def get_operator_de():
    if 'number' in request.args:
        number = request.args['number']
        if(4 <= len(number) <= 20):
            objPhoneNumber.set_phonenumber(number)
            return jsonify({'valid-flag':objPhoneNumber.validate,'operator': objPhoneNumber.get_de_operator()})
        else:
            return jsonify({'status':404,'valid-flag':0,'operator': ''})
    else:
        return 'Invalid Key'

'''
    National Significant Number Information
'''
    
@app.route('/nsn', methods = ['GET'])
def get_nsn():
    if 'number' in request.args:
        number = request.args['number']
        if(4 <= len(number) <= 20):
            objPhoneNumber.set_phonenumber(number)
            return jsonify({'valid-flag':objPhoneNumber.validate,'nsn':objPhoneNumber.get_nsn()})
        else:
            return jsonify({'status':404,'valid-flag':0,'nsn':''})
    else:
        return 'Invalid Key'
    
'''
   2 Digit ISO Information
'''

@app.route('/iso2', methods = ['GET'])
def get_iso2():
    if 'number' in request.args:
        number = request.args['number']
        if(4 <= len(number) <= 20):
            objPhoneNumber.set_phonenumber(number)
            return jsonify({'valid-flag':objPhoneNumber.validate,'iso2':objPhoneNumber.get_iso2()})
        else:
            return jsonify({'status':404,'valid-flag':0,'iso2':''})
    else:
        return 'Invalid Key'

@app.route('/iso3', methods = ['GET'])
def get_iso3():
    if 'number' in request.args:
        number = request.args['number']
        if(4 <= len(number) <= 20):
            objPhoneNumber.set_phonenumber(number)
            return jsonify({'valid-flag':objPhoneNumber.validate,'iso3':objPhoneNumber.get_iso3()})
        else:
            return jsonify({'status':404,'valid-flag':0,'iso3':''})
    else:
        return 'Invalid Key'

'''
   Country Information
'''
    
@app.route('/country', methods = ['GET'])
def get_country():
    if 'number' in request.args:
        number = request.args['number']
        if(4 <= len(number) <= 20):
            objPhoneNumber.set_phonenumber(number)
            return jsonify({'valid-flag':objPhoneNumber.validate,'country':objPhoneNumber.get_country()})
        else:
            return jsonify({'status':404,'valid-flag':0,'country':''})
    else:
        return 'Invalid Key'
    
'''
   Country Code
'''

@app.route('/countrycode', methods = ['GET'])
def get_countrycode():
    if 'number' in request.args:
        number = request.args['number']
        if(4 <= len(number) <= 20):
            objPhoneNumber.set_phonenumber(number)
            return jsonify({'valid-flag':objPhoneNumber.validate,'countrycode':objPhoneNumber.get_countrycode()})
        else:
            return jsonify({'status':404,'valid-flag':0,'countrycode':''})
    else:
        return 'Invalid Key'
    
'''
   Phone Number Types Information
'''

@app.route('/type', methods = ['GET'])
def get_typeid():
    if 'number' in request.args:
        number = request.args['number']
        if(4 <= len(number) <= 20):
            objPhoneNumber.set_phonenumber(number)
            return jsonify({'valid-flag':objPhoneNumber.validate,'type':objPhoneNumber.get_typeid()})
        else:
            return jsonify({'status':404,'valid-flag':0,'type':''})
    else:
        return 'Invalid Key'
    
'''
   Phone Number Validation Information
'''
    
@app.route('/validate', methods = ['GET'])
def get_validation():
    if 'number' in request.args:
        number = request.args['number']
        if(4 <= len(number) <= 20):
            objPhoneNumber.set_phonenumber(number)
            return jsonify({'valid-flag':objPhoneNumber.validate})
        else:
            return jsonify({'status':404,'valid-flag':0})
    else:
        return 'Invalid Key'
    
'''
   Number Details Information
'''
    
@app.route('/details', methods = ['GET'])
def get_numberdetails():
    if 'number' in request.args:
        number = request.args['number']
        if(4 <= len(number) <= 20):
            objPhoneNumber.set_phonenumber(number)
            return jsonify(objPhoneNumber.get_phoneNumberDetails())
        else:
            return jsonify({'status':404,'valid-flag':0})
    else:
        return 'Invalid Key'
    
'''
    Phone Number Formats
'''
    
@app.route('/E164-format', methods = ['GET'])
def get_E164Format():
    if 'number' in request.args:
        return objPhoneNumber.get_E164format(request.args['number'])
    else:
        return 'Invalid Key'

@app.route('/without-E164-format', methods = ['GET'])   
def get_withoutE164Format():
    if 'number' in request.args:
        return objPhoneNumber.get_WithoutE164format(request.args['number'])
    else:
        return 'Invalid Key'

@app.route('/national-format', methods = ['GET']) 
def get_nationalformat():
    if 'number' in request.args:
        number = request.args['number']
        if(4 <= len(number) <= 20):
            objPhoneNumber.set_phonenumber(number)
            return objPhoneNumber.get_NationalFormat()
        else:
            return objPhoneNumber.get_phonenumber()
    else:
        return 'Invalid Key'

@app.route('/international-format', methods = ['GET']) 
def get_internationalformat():
    if 'number' in request.args:
        number = request.args['number']
        if(4 <= len(number) <= 20):
            objPhoneNumber.set_phonenumber(number)
            return objPhoneNumber.get_InternationalFormat()
        else:
            return objPhoneNumber.get_phonenumber()
    else:
        return 'Invalid Key'


'''
    Location Information
'''
    
@app.route('/location', methods = ['GET']) 
def get_location():
    if 'number' in request.args:
        number = request.args['number']
        if(4 <= len(number) <= 20):
            objPhoneNumber.set_phonenumber(number)
            return jsonify({'valid-flag':objPhoneNumber.validate,'location':objPhoneNumber.get_en_location()})
        else:
            return jsonify({'status':404,'valid-flag':0,'location':''})
    else:
        return 'Invalid Key'
        
@app.route('/location-en', methods = ['GET']) 
def get_location_en():
    if 'number' in request.args:
        number = request.args['number']
        if(4 <= len(number) <= 20):
            objPhoneNumber.set_phonenumber(number)
            return jsonify({'valid-flag':objPhoneNumber.validate,'location-en':objPhoneNumber.get_en_location()})
        else:
            return jsonify({'status':404,'valid-flag':0,'location-en':''})
    else:
        return 'Invalid Key'
    
@app.route('/location-fr', methods = ['GET']) 
def get_location_fr():
    if 'number' in request.args:
        number = request.args['number']
        if(4 <= len(number) <= 20):
            objPhoneNumber.set_phonenumber(number)
            return jsonify({'valid-flag':objPhoneNumber.validate,'location-fr':objPhoneNumber.get_fr_location()})
        else:
            return jsonify({'status':404,'valid-flag':0,'location-fr':''})
    else:
        return 'Invalid Key'
    
@app.route('/location-de', methods = ['GET']) 
def get_location_de():
    if 'number' in request.args:
        number = request.args['number']
        if(4 <= len(number) <= 20):
            objPhoneNumber.set_phonenumber(number)
            return jsonify({'valid-flag':objPhoneNumber.validate,'location-de':objPhoneNumber.get_de_location()})
        else:
            return jsonify({'status':404,'valid-flag':0,'location-de':''})
    else:
        return 'Invalid Key'
    
@app.route('/location-it', methods = ['GET']) 
def get_location_it():
    if 'number' in request.args:
        number = request.args['number']
        if(4 <= len(number) <= 20):
            objPhoneNumber.set_phonenumber(number)
            return jsonify({'valid-flag':objPhoneNumber.validate,'location-it':objPhoneNumber.get_it_location()})
        else:
            return jsonify({'status':404,'valid-flag':0,'location-it':''})
    else:
        return 'Invalid Key'

'''
    TimeZone Information
''' 
@app.route('/time-zone', methods = ['GET'])   
def get_timezone():
    if 'number' in request.args:
        number = request.args['number']
        if(4 <= len(number) <= 20):
            objPhoneNumber.set_phonenumber(number)
            return jsonify({'valid-flag':objPhoneNumber.validate,'timezone':objPhoneNumber.get_timezone()})
        else:
            return jsonify({'status':404,'valid-flag':0,'timezone':''})
    else:
        return 'Invalid Key'
    
@app.route('/portable-region', methods = ['GET'])   
def get_portable_region():
    if 'number' in request.args:
        number = request.args['number']
        if(4 <= len(number) <= 20):
            objPhoneNumber.set_phonenumber(number)
            return jsonify({'valid-flag':objPhoneNumber.validate,'is-portable-region':objPhoneNumber.get_PortableRegion()})
        else:
            return jsonify({'status':404,'valid-flag':0,'is-portable-region':''})
    else:
        return 'Invalid Key'
    
@app.route('/sample-numbers', methods = ['GET'])   
def get_sample_numbers():
    if 'iso' in request.args:
        iso = request.args['iso']
        if(len(iso) == 2):
            return jsonify(objPhoneNumber.get_Samples(iso))
        else:
            return jsonify({'status':404,'valid-flag':0,'is-portable-region':''})
    else:
        return 'Invalid Key'
    
if __name__ == '__main__':
    app.run()
    

