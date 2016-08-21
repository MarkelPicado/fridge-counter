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
__date__        = "20/08/2016"

###############################################################################
###############################################################################
###############################################################################

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'src')) # */FridgeCounter/src

from product import PRODUCT_TYPES
from product.product import Product

class Fridge(object):

	def __init__(self, type, id, products_collection={}):

		self.type = type,
		self.id = id
		self.products_collection = {}
		self.barcodes = []

		for product_type in PRODUCT_TYPES:
			self.products_collection[product_type] = []

		for product_type in products_collection:
			for product in products_collection[product_type]:
				self.barcodes.append(product.barcode.barcode)
				self.products_collection[product_type].append(product)


	def add_product(self, p):
		added = False

		products = self.products_collection[p.type]

		if p.barcode.barcode in self.barcodes:
			added = True

		if not added:

			self.barcodes.append(p.barcode.barcode)
			self.products_collection[p.type].append(p)
			return True

		return False

	def remove_product(self, obj, units=1, remove_all=False):

		obj_type = type(obj)

		if isinstance(obj, str):

			if obj in self.barcodes:
				self._remove_product_1(obj, units=units, remove_all=remove_all)

		elif isinstance(obj, Product):
			self._remove_product_2(obj, units=units, remove_all=remove_all)

	def _remove_product_1(self, barcode, units, remove_all):

		if remove_all:

			for product_type in self.products_collection:
				for product in self.products_collection[product_type]:

					if product.barcode.barcode == barcode:

							self.products_collection[product_type].remove(product)
							self.barcodes.remove(barcode)

		else:

			for product_type in self.products_collection:
				for product in self.products_collection[product_type]:

					if product.barcode.barcode == barcode:

						product.units -= units

						if product.units < 1:

							self.products_collection[product_type].remove(product)
							self.barcodes.remove(barcode)

							

	def _remove_product_2(self, p, units, remove_all):

		if remove_all:

			for product in self.products_collection[p.type]:

				if product.barcode.barcode == p.barcode.barcode:

						self.products_collection[p.type].remove(p)
						self.barcodes.remove(p.barcode.barcode)


		else:

			for product in self.products_collection[p.type]:

				if product.barcode.barcode == p.barcode.barcode:

					product.units -= units

					if product.units < 1:

						self.products_collection[p.type].remove(p)
						self.barcodes.remove(p.barcode.barcode)


	def is_in(self, barcode):
		return barcode in self.barcodes

	def __str__(self):
		string = ''
		for product_type in self.products_collection:

			string += '[%s]\n' % product_type

			for product in self.products_collection[product_type]:

				string += '\t+ [%s] %s || %s: \n\t\t- %s\n\t\tAdded date - (%s)\n' % (product.units, product.name, product.used_by.strftime('%Y-%m-%d'), product.description, product.created_date.strftime('%Y-%m-%d'))

		if len(string):
			return string

		return 'EMPTY FRIGE'
