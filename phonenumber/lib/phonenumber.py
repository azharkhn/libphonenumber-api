#!/usr/bin/env python

import phonenumbers
from phonenumbers import carrier, timezone
from phonenumbers.geocoder import country_name_for_number, description_for_number
import dicts

class NumberDetails(object):
    phonenumber = ''
    phonenumber_object = ''
    phonenumber_details = {}
    validate = False
    
    def remove_chars_from_phonenumber(self,phonenumber):
        return filter(type(phonenumber).isdigit, phonenumber)
    
    def set_phonenumber(self,phonenumber):
        self.phonenumber = self.get_WithoutE164format(phonenumber.replace(' ', ''))
        self.phonenumber_object = phonenumbers.parse(self.get_E164format(self.phonenumber))
        self.validate = self.validatePhoneNumber()
    
    def get_phonenumber(self):
        self.phonenumber_details['phonenumber'] = self.phonenumber
        return self.phonenumber_details['phonenumber']
    
    def get_nsn(self):
        self.phonenumber_details['nsn'] = phonenumbers.national_significant_number(self.phonenumber_object)
        return self.phonenumber_details['nsn']
    
    def get_operator(self):
        self.phonenumber_details['operator'] = carrier.name_for_number(self.phonenumber_object, "en")
        return self.phonenumber_details['operator']
    
    def get_en_operator(self):
        self.phonenumber_details['operator'] = carrier.name_for_number(self.phonenumber_object, "en")
        return self.phonenumber_details['operator']
    
    def get_it_operator(self):
        self.phonenumber_details['operator'] = carrier.name_for_number(self.phonenumber_object, "it")
        return self.phonenumber_details['operator']
    
    def get_fr_operator(self):
        self.phonenumber_details['operator'] = carrier.name_for_number(self.phonenumber_object, "fr")
        return self.phonenumber_details['operator']
    
    def get_de_operator(self):
        self.phonenumber_details['operator'] = carrier.name_for_number(self.phonenumber_object, "de")
        return self.phonenumber_details['operator']
    
    def get_country(self):
        self.phonenumber_details['country'] = country_name_for_number(self.phonenumber_object, "en")
        return self.phonenumber_details['country']
    
    def get_iso2(self):
        self.phonenumber_details['iso2'] = phonenumbers.region_code_for_number(phonenumbers.parse(self.get_E164format(self.phonenumber)))
        return self.phonenumber_details['iso2']
    
    def get_iso3(self):
        self.phonenumber_details['iso3'] = dicts.country_iso2to3.get(phonenumbers.region_code_for_number(phonenumbers.parse(self.get_E164format(self.phonenumber))))
        return self.phonenumber_details['iso3']
    
    def get_countrycode(self):
        self.phonenumber_details['code'] =self.phonenumber[:len(self.phonenumber)-len(str(phonenumbers.national_significant_number(self.phonenumber_object)))]
        return self.phonenumber_details['code']
    
    def get_typeid(self):
        self.phonenumber_details['typeid'] = dicts.phonenumber_types.get(phonenumbers.number_type(self.phonenumber_object))
        return self.phonenumber_details['typeid']

    def get_en_location(self):
        return phonenumbers.geocoder.description_for_number(self.phonenumber_object, "en")

    def get_de_location(self):
        return phonenumbers.geocoder.description_for_number(self.phonenumber_object, "de")
    
    def get_fr_location(self):
        return phonenumbers.geocoder.description_for_number(self.phonenumber_object, "fr")
    
    def get_it_location(self):
        return phonenumbers.geocoder.description_for_number(self.phonenumber_object, "it")
        
    def get_timezone(self):
        self.phonenumber_details['timezone'] = timezone.time_zones_for_number(self.phonenumber_object)
        return self.phonenumber_details['timezone']
                            
    def get_phoneNumberDetails(self):
        self.get_phonenumber()
        self.get_nsn()
        self.get_operator()
        self.get_country()
        self.get_iso2()
        self.get_iso3()
        self.get_countrycode()
        self.get_typeid()
        self.get_timezone()
        self.get_PortableRegion()
        self.phonenumber_details['E164-format'] = self.get_E164format(self.get_phonenumber())
        self.phonenumber_details['National-format'] = self.get_NationalFormat()
        self.phonenumber_details['International-format'] = self.get_InternationalFormat()
        self.phonenumber_details['RFC3966-format'] = self.get_RFC3966Format()
        return self.phonenumber_details
        
    def validatePhoneNumber(self):
        self.phonenumber_details['is_validnumber'] = phonenumbers.is_valid_number(self.phonenumber_object)
        self.phonenumber_details['is_possiblenumber'] = phonenumbers.is_possible_number(self.phonenumber_object)
        self.phonenumber_details['is_validnumberforRegion'] = phonenumbers.is_valid_number_for_region(self.phonenumber_object,self.get_iso2())
        return self.phonenumber_details['is_validnumber'] * self.phonenumber_details['is_possiblenumber'] * self.phonenumber_details['is_validnumberforRegion']

    def get_E164format(self, phonenumber):
        phonenumber = self.remove_chars_from_phonenumber(phonenumber)
        if(phonenumber[:2] == '00'):
            return '+'+phonenumber[2:]
        else:
            return '+'+phonenumber  
        
    
    def get_WithoutE164format(self,phonenumber):
        phonenumber = self.remove_chars_from_phonenumber(phonenumber)
        if(phonenumber[:2] == '00'):
            return phonenumber[2:]
        else:
            return phonenumber
        
    def get_NationalFormat(self):
        return phonenumbers.format_number(self.phonenumber_object, phonenumbers.PhoneNumberFormat.NATIONAL)
        
    def get_InternationalFormat(self):
        return phonenumbers.format_number(self.phonenumber_object, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    
    def get_RFC3966Format(self):
        return phonenumbers.format_number(self.phonenumber_object, phonenumbers.PhoneNumberFormat.RFC3966)
    
    def get_PortableRegion(self):
        self.phonenumber_details['is_portable_region'] = phonenumbers.is_mobile_number_portable_region(self.get_iso2())
        return self.phonenumber_details['is_portable_region']
    
    def get_SampleNumber(self,iso,typeid):
        sample = phonenumbers.example_number_for_type(iso, typeid)
        if(sample != None):
            return phonenumbers.format_number(sample, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        else:
            return ''
    
    def get_Samples(self,iso):
        if(dicts.country_iso2to3.get(iso) != None):
            samples = dict()
            types = dicts.phonenumber_types
            for index in range(len(types)-1):
                samples[types.get(index)] = self.get_SampleNumber(iso, index)
            return samples
        else:
            return 'Invalid ISO Code'   
        


