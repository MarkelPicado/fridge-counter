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

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'src')) # */FridgeCounter/src

from barcode import Barcode, EAN13
from barcode_errors import InvalidBarcode

BARCODE_TYPES = {
    EAN13
}

BARCODE_TYPESS = {
    'EAN13': EAN13
}

def BarcodeFactory(barcode):
    barcode_type = len(barcode)

    for b_type in BARCODE_TYPES:
        if b_type.validate(barcode):
            return b_type(barcode)

    raise InvalidBarcode('The barcode %s did not match with implemented barcode types %s' % (barcode, BARCODE_TYPESS.keys()))


class BarcodeGenerator(object):
    
    def __init__(self, type):

        if type in BARCODE_TYPESS:

            self.barcode_type = BARCODE_TYPESS[type]

        else:

            self.barcode_type = Barcode

    def generate_barcode(self):
        return self.barcode_type.generate_barcode()

