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

from product.product import Product
from barcode.barcode import Barcode
from barcode import BarcodeGenerator
from product import GENERIC 

#MAGNET NAMES
APPLE = 														'APPLE'
GENERIC_FOOD = 													'GENERIC-FOOD'


class Magnet(object):

	magnet_type = GENERIC
	magnet_name = 'MAGNET'

	def __init__(self, barcode=None):

		self.barcode = barcode if barcode else BarcodeGenerator('EAN13').generate_barcode()
		self.linked_products = {}
		self.units = 0

	def link_product(self, p):
		if p.barcode.barcode in self.linked_products.keys():

			for product in self.linked_products[p.barcode.barcode]:

				if p.used_by == product.used_by:
					product.units += p.units
				else:
					self.linked_products[p.barcode.barcode].append(p)
					break

		else:

			self.linked_products[p.barcode.barcode] = [p]

		self.units += p.units

	def unlink_product(self, obj, units=1):

		obj_type = type(obj)

		if isinstance(obj, Product):

			if obj.barcode.barcode in self.linked_products.keys():
				self._unlink_product1(obj, units)

		elif isinstance(obj, dict):
			self._unlink_product2(obj, units)

		elif isinstance(obj, str):
			self._unlink_product3(obj, units)


	def _unlink_product1(self, p, units):
		self.units -= units
		p.units -= units

		if p.units < 1:

			self.linked_products[p.barcode.barcode].remove(p)

		if len(self.linked_products[p.barcode.barcode]) < 1:

			self.linked_products.pop(p.barcode.barcode, None)

	def _unlink_product2(self, dictt, units):
		barcode = dictt['barcode']
		used_by = dictt['used_by']

		if barcode in self.linked_products.keys():

				for product in self.linked_products[barcode]:

					if product.used_by == used_by:
						self._unlink_product1(product, units)

	def _unlink_product3(self, barcode, units):
		if barcode in self.linked_products.keys():
			product = self.linked_products[barcode][0]
			self._unlink_product1(product, units)



	def __str__(self):
		return 'Type:\t%s\tName:\t%s\tUnits:\t%s Barcode:\t%s' % (self.magnet_type, self.magnet_name, self.units, self.barcode)