###############################################################################
###############################################################################
###############################################################################

''' 
En este modulo se define todo lo referente a la clase producto
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
import datetime

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'src')) # */FridgeCounter/src

from barcode import BarcodeFactory
from barcode.barcode import Barcode

class Product( object ):

	def __init__( self, barcode, id, name, description, type='GENERIC', used_by=None, units= 1 ):

		self.barcode = BarcodeFactory( barcode )
		self.type = type
		self.name = name
		self.description = description
		self.created_date = datetime.datetime.now()
		self.used_by = used_by
		self.units = units


	def set_barcode( self, barcode ):

		if isinstance( barcode, str ):

			self._set_barcode_1( barcode )

		elif isinstance( barcode, Barcode ):

			self._set_barcode_2(barcode)


	def _set_barcode_1( self, barcode ):

		self.barcode = BarcodeFactory( barcode )


	def _set_barcode_2( self, barcode ):

		self.barcode = barcode

	def to_dict( self ):

		return {
			'barcode': 			self.barcode,
			'type': 			self.type,
			'name': 			self.name,
			'description': 		self.description,	
			'created_date': 	self.created_date, 
			'used_by': 			self.used_by	
		}

	def __str__(self):
		return '%s(USED BY: %s) || %s :\n\t- %s' % (self.name, self.used_by.strftime('%Y-%m-%d'), self.barcode.barcode, self.description)

