###############################################################################
###############################################################################
###############################################################################

''' 
De momento modulo de pruebas, en un futuro sera quien gestione los productos
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

from fridge.fridge import Fridge
from barcode import BarcodeGenerator
from product.product import Product
from product import PRODUCT_TYPES

FRIDGE = Fridge('NEVERA1', '110::00901')
PROMPT = 'fridge-counter'


def read_barcode():
	#Aqui vendria todo lo relacionado con la lectura del codigo de barras desde el lector
	return BarcodeGenerator('EAN13').generate_barcode()

def add_product(barcode):
	barcode = barcode
	product_name = raw_input('%s# ENTER PRODUCT NAME: --> ' % PROMPT)
	product_description = raw_input('%s# ENTER PRODUCT DESCRIPTION: --> ' % PROMPT)
	product_type = raw_input('%s# ENTER PRODUCT TYPE ("GENERIC" BY DEFAULT): \n%s# PRODUCT TYPES: %s --> ' % (PROMPT, PROMPT, PRODUCT_TYPES))
	product_used_by = raw_input('%s# ENTER PRODUCT USED BY (YYYY-MM-DD): --> ' % PROMPT)
	product_units = raw_input('%s# ENTER PRODUCT UNITS NUMBER (1 BY DEFAULT): --> ' % PROMPT)

	if not product_type in PRODUCT_TYPES:
		product_type = 'GENERIC'

	if product_units:
		product_units = int(product_units)

	if product_used_by:
		
		try:
			product_used_by = datetime.datetime.strptime(product_used_by, '%Y-%m-%d')
		except ValueError:
			product_used_by = datetime.date.today() + datetime.timedelta(10)

	else:
		product_used_by = datetime.date.today() + datetime.timedelta(10)

	product = Product(barcode=barcode, id=barcode[7:12], name=product_name, description=product_description, type=product_type, used_by=product_used_by, units= product_units )

	FRIDGE.add_product(product) 

def remove_product(barcode):

	units = raw_input('%s# BARCODE: %s | How many units of this product do you want remove? ' % (PROMPT, barcode))

	if units:
		units = int(units)

	FRIDGE.remove_product(barcode, units=units)

###############
#### MAIN #####
###############

while True:

	
	command = raw_input('%s# ' % PROMPT)

	if command == 'del':
		barcode = raw_input('%s# ENTER BARCODE TO BE DELETED ' % PROMPT)
		if FRIDGE.is_in(barcode):
			remove_product(barcode)

	elif command == 'read':

		barcode = read_barcode()

		if FRIDGE.is_in(barcode):

			res = raw_input('%s# BARCODE: %s | Do you want remove this product? (s/n) ' % (PROMPT, barcode))

			if res == 's':
				remove_product(barcode)

		else:

			res = raw_input('%s# BARCODE: %s | Do you want add this product? (s/n) ' % (PROMPT, barcode))

			if res == 's':
				add_product(barcode)

	elif command == 'show':
		print FRIDGE

	elif command == 'help':

		print 'FRIDGE-COUNTER COMMAND LIST				'
		print '		    								'
		print '		    								'
		print '		help								'
		print '		read								'
		print '		del 								'
		print '		show 								'
		print '		exit								'


	elif command == 'exit':
		sys.exit(1)


