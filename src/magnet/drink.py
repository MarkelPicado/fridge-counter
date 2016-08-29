###############################################################################
###############################################################################
###############################################################################

''' 
En este modulo se define todo lo referente a la clase fridge
'''

__author__      = "Nombre"                                               
__credits__     = ["Markel Picado Ortiz"]                                                         
__version__     = "0.0.1"                                                          
__maintainer__  = "Markel Picado Ortiz"                                         
__email__       = "mpicado001@gmail.com"                                          
__status__      = "Work In Progress"                                                   
__date__        = "22/08/2016"

###############################################################################
###############################################################################
###############################################################################

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'src')) # */FridgeCounter/src

import magnet

__m_type__ = 'DRINK'

class Drink(magnet.Magnet):
	
	magnet_type = __m_type__

	def __init__(self, magnet_name=__m_type__.capitalize(), barcode=None):

		super(Drink, self).__init__(barcode)
		
		self.magnet_name = magnet_name