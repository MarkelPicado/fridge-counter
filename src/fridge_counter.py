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
from magnet.fruit import Fruit
from magnet.meal import Meal
from magnet import MAGNET_TYPES, load_magnets

load_magnets('magnet')

FRIDGE = Fridge('NEVERA1', '110::00901')
PROMPT = 'fridge-counter'


def read_barcode():
	#Aqui vendria todo lo relacionado con la lectura del codigo de barras desde el lector
	return BarcodeGenerator('EAN13').generate_barcode()


def add_product(magnet_barcode, barcode):
	global FRIDGE

	barcode = barcode
	
	product_name = raw_input('%s# ENTER PRODUCT NAME: --> ' % PROMPT)
	
	product_description = 'Field to be deleted'
	
	product_used_by = raw_input('%s# ENTER PRODUCT USED BY (YYYYMMDD): --> ' % PROMPT)
	
	product_units = raw_input('%s# ENTER PRODUCT UNITS NUMBER (1 BY DEFAULT): --> ' % PROMPT)

	product = Product(barcode=barcode, id=barcode[7:12], name=product_name, description=product_description, used_by=product_used_by, units= product_units )

	FRIDGE.add_product(magnet_barcode, product) 


def remove_product(barcode):	

	global FRIDGE	

	units = raw_input('%s# HOW MANY UNITS: ' % (PROMPT))

	units = int(units)

	if FRIDGE.is_magnet(barcode):

		i = 1

		for bcode in FRIDGE.magnets[barcode].linked_products:

			products = {}
			
			for p in FRIDGE.get_product(bcode):
				products[i] = {
				'used_by': p.used_by,
				'barcode': p.barcode.barcode,
				'name':	   p.name
				}
				i += 1

			custom_print('Choose a product to delete for magnet: %s' % FRIDGE.magnets[barcode].magnet_name)
			
		for u in products:

			print '- %s ( %s )' % (u, products[u])

			selecction = raw_input('%s# YOUR CHOICE: ' % (PROMPT))

			remove = {
			'used_by': products[int(selecction)]['used_by'],
			'barcode': products[int(selecction)]['barcode']
			}

			FRIDGE.remove_product(remove, units)



	elif len(FRIDGE.get_product(barcode)) > 1:
		used_by = {}
		i = 1
		for p in FRIDGE.get_product(barcode):
			used_by[i] = p.used_by
			i += 1

		print '%s THERE ARE MORE THAN ONE PRODUCT WITH THE SAME BARCODE PLEASE SELECT ONE' % PROMPT
		
		for u in used_by:

			print '- %s USED BY: %s' % (u, used_by[u])

		selecction = raw_input('%s# YOUR CHOICE: ' % (PROMPT))
		remove = {
		'used_by': used_by[int(selecction)],
		'barcode': barcode
		}

		FRIDGE.remove_product(remove, units)

	elif len(FRIDGE.get_product(barcode)) == 1:

		FRIDGE.remove_product(barcode, units)


def custom_string(string):
	split_string = string.split('\n')

	to_print = '\n'.join('%s# %s' % (PROMPT, line) for line in split_string)

	return to_print

def custom_print(string):
	split_string = string.split('\n')

	to_print = '\n'.join('%s# %s' % (PROMPT, line) for line in split_string)

	print to_print

###############
#### MAIN #####
###############


print read_barcode()
print read_barcode()
print read_barcode()


while True:

	
	command = raw_input(custom_string(''))

	if command == 'add m':

		barcode_1 = raw_input(custom_string('Reading barcode: '))

		magnet_type = raw_input(custom_string('Choose magnet type: %s ' % MAGNET_TYPES.keys()))

		magnet_type_class = MAGNET_TYPES.get(magnet_type)

		if magnet_type_class:

			magnet_name = raw_input(custom_string('Enter the magnet name: '))

			m = magnet_type_class(magnet_name=magnet_name, barcode=barcode_1)

			FRIDGE.add_magnet(m)

		else:

			custom_print('There is not a %s magnet type ' % magnet_type)

	elif command == 'add p':

		barcode_1 = raw_input(custom_string('Reading barcode: '))

		magnet_barcode = barcode_1 if FRIDGE.is_magnet(barcode_1) else None

		barcode = barcode_1 if not FRIDGE.is_magnet(barcode_1) else None

		if magnet_barcode:

			barcode = raw_input(custom_string('Reading barcode for %s: ' % FRIDGE.magnets[magnet_barcode].magnet_name))
			
		else:

			magnet_barcode = raw_input(custom_string('Please pass the magnet barcode: '))

		res = raw_input(custom_string('Barcode: %s | Do you want add this product? (s/n) ' % barcode))

		if res == 's':

			add_product(magnet_barcode, barcode)


	elif command == 'del':

		barcode = raw_input(custom_string('Reading barcode: '))

		res = raw_input(custom_string('Barcode: %s | Do you want delete this product? (s/n) ' % barcode))

		if res == 's':

			remove_product(barcode)


	elif command == 'show':

		custom_print(str(FRIDGE))
		

	elif command == 'show m':

		for m_barcode in FRIDGE.magnets:

			custom_print(m_barcode + '\t' + FRIDGE.magnets[m_barcode].magnet_name + '\t' + FRIDGE.magnets[m_barcode].magnet_type)



	elif command == 'help':

		print 'FRIDGE-COUNTER COMMAND LIST				'
		print ''
		print ''
		print '		help								'
		print '		add 								'
		print '		del 								'
		print '		show 								'
		print '		exit								'


	elif command == 'exit':
		sys.exit(1)


