###############################################################################
###############################################################################
###############################################################################

''' 
En este modulo se define todo lo referente a la clase barcode
'''

__author__      = "Nombre"                                               
__credits__     = ["Markel Picado Ortiz"]                                                         
__version__     = "0.0.1"                                                          
__maintainer__  = "Markel Picado Ortiz"                                         
__email__       = "mpicado001@gmail.com"                                          
__status__      = "Work In Progress"                                                   
__date__        = "20/08/2016"

###############################################################################
###############################################################################
###############################################################################

import os
import sys
import random

from utils import EAN_BARCODE_COUNTRIES
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'src')) # */FridgeCounter/src 

class Barcode(object):

    barcode = None

    @classmethod
    def validate(cls, barcode):
        raise NotImplementedError('Not Implemented Method')

    @classmethod
    def generate_barcode(cls, barcode):
        raise NotImplementedError('Not Implemented Method')

    def __str__(self):
        return "BARCODE: {barcode}".format(barcode=self.barcode)



class EAN13(Barcode):

    def __init__(self, barcode):
        self.barcode = barcode
        self.country_number = barcode[:3] if barcode else None
        self.company_number = barcode[3:7] if barcode else None
        self.serial_number = barcode[7:12] if barcode else None
        self.verification_number = barcode[12:] if barcode else None
        self.country = EAN_BARCODE_COUNTRIES[self.country_number] if barcode else None

    def to_DDBB(self):
        return None

    def to_dict(self):
        return {
            'country_number':           self.country_number,
            'company_number':           self.company_number,
            'serial_number':            self.serial_number,
            'verification_number':      self.verification_number,
            'country':                  self.country
        }

    @classmethod
    def validate(cls, barcode):
        if len(barcode) == 12 or len(barcode) == 13:
            if len(barcode) == 12:
                barcode = '0' + barcode

            if EAN_BARCODE_COUNTRIES.get(barcode[:3], None):
                return True

        return False

    @classmethod
    def generate_barcode(cls):
        country_number = '084'
        company_number = '0000'
        serial_number = ''.join(random.choice('0123456789') for _ in range(5)) 
        verification_number = '1'
        return country_number + company_number + serial_number + verification_number

    def __str__(self):
        return "BARCODE: {barcode} COUNTRY: {country} PRODUCT: {product_name}".format(barcode=self.barcode, country=self.country, product_name='PRUEBA')




