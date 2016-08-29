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
from magnet_errors import NotLinkedError



class Magnet(object):

	def __init__(self, barcode=None):

		self.barcode = barcode if barcode else BarcodeGenerator('EAN13').generate_barcode()
		self.linked_products = {}
		self.units = 0

	def link_product(self, p):
		p.type = self.magnet_type
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

				return self._unlink_product1(obj, units)

			else:

				raise NotLinkedError('The barcode %s is not linked in %s//%s magnet' % (obj.barcode.barcode, self.magnet_name, self.barcode))


		elif isinstance(obj, dict):

			return self._unlink_product2(obj, units)

		elif isinstance(obj, str):

			return self._unlink_product3(obj, units)


	def _unlink_product1(self, p, units):

		self.units -= units

		p.units -= units

		if p.units < 1:

			self.linked_products[p.barcode.barcode].remove(p)

			if len(self.linked_products[p.barcode.barcode]) < 1:

				self.linked_products.pop(p.barcode.barcode, None)

				return None

		return 1


	def _unlink_product2(self, dictt, units):

		barcode = dictt['barcode']

		used_by = dictt['used_by']

		if barcode in self.linked_products.keys():

				for product in self.linked_products[barcode]:

					if product.used_by == used_by:

						return self._unlink_product1(product, units)

		else:

			raise NotLinkedError('The barcode %s is not linked in %s//%s magnet' % (barcode, self.magnet_name, self.barcode))


	def _unlink_product3(self, barcode, units):

		if barcode in self.linked_products.keys():

			product = self.linked_products[barcode][0]

			return self._unlink_product1(product, units)

		else:

			raise NotLinkedError('The barcode %s is not linked in %s//%s magnet' % (barcode, self.magnet_name, self.barcode))



	def __str__(self):
		return 'Type:\t%s\tName:\t%s\tUnits:\t%s Barcode:\t%s' % (self.magnet_type, self.magnet_name, self.units, self.barcode)