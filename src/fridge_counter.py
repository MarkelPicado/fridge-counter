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
from magnet.apple import Apple
from magnet.milk import Milk

FRIDGE = Fridge('NEVERA1', '110::00901')
PROMPT = 'fridge-counter'


def read_barcode():
	#Aqui vendria todo lo relacionado con la lectura del codigo de barras desde el lector
	return BarcodeGenerator('EAN13').generate_barcode()

def add_product(magnet_barcode, barcode):
	barcode = barcode
	product_name = FRIDGE.magnets[magnet_barcode].magnet_name
	product_description = raw_input('%s# ENTER PRODUCT DESCRIPTION: --> ' % PROMPT)
	product_type = FRIDGE.magnets[magnet_barcode].magnet_type
	product_used_by = raw_input('%s# ENTER PRODUCT USED BY (YYYY-MM-DD): --> ' % PROMPT)
	product_units = raw_input('%s# ENTER PRODUCT UNITS NUMBER (1 BY DEFAULT): --> ' % PROMPT)

	if not product_type in PRODUCT_TYPES:
		product_type = 'GENERIC'

	if product_units:
		product_units = int(product_units)
	else:
		product_units = 1

	if product_used_by:
		
		try:
			product_used_by = datetime.datetime.strptime(product_used_by, '%Y-%m-%d')
		except ValueError:
			product_used_by = datetime.date.today() + datetime.timedelta(10)

	else:
		product_used_by = datetime.date.today() + datetime.timedelta(10)

	product = Product(barcode=barcode, id=barcode[7:12], name=product_name, description=product_description, type=product_type, used_by=product_used_by, units= product_units )

	FRIDGE.add_product(magnet_barcode, product) 

def remove_product(magnet_barcode, barcode):		
	units = raw_input('%s# HOW MANY UNITS: ' % (PROMPT))
	units = int(units)

	if len(FRIDGE.kinds_of_product(magnet_barcode, barcode)) > 1:
		used_by = {}
		i = 1
		for p in FRIDGE.kinds_of_product(magnet_barcode, barcode):
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

		FRIDGE.remove_product(magnet_barcode, remove, units)

	elif len(FRIDGE.kinds_of_product(magnet_barcode, barcode)) == 1:
		FRIDGE.remove_product(magnet_barcode, barcode, units)

def is_magnet(barcode):
	if barcode in FRIDGE.magnets.keys():
		return True

	return False 

###############
#### MAIN #####
###############

magnet_apple = Apple()
magnet_milk = Milk()
FRIDGE.add_magnet(magnet_apple)
FRIDGE.add_magnet(magnet_milk)
print "MAGNET BARCODES:"
for magnet_key in FRIDGE.magnets:
	print '%s\t%s' % (magnet_key, FRIDGE.magnets[magnet_key].magnet_name)

while True:

	
	command = raw_input('%s# ' % PROMPT)




	if command == 'add':

		barcode_1 = raw_input('%s# READING BARCODE: ' % (PROMPT))
		magnet_barcode = barcode_1 if is_magnet(barcode_1) else None
		barcode = barcode_1 if not is_magnet(barcode_1) else None
		if magnet_barcode:
			barcode = raw_input('%s# READING BARCODE FOR %s: ' % (PROMPT, FRIDGE.magnets[magnet_barcode].magnet_name))
			
		else:
			magnet_barcode = raw_input('%s# PLEASE PASS THE MAGNET: ' % (PROMPT))


		res = raw_input('%s# BARCODE: %s | Do you want add this product? (s/n) ' % (PROMPT, barcode))

		if res == 's':
			if not is_magnet(barcode):
				add_product(magnet_barcode, barcode)
			else:
				print 'ERROR: THAT IS A MAGNET'

	elif command == 'del':

		barcode_1 = raw_input('%s# READING BARCODE TO DELETE: ' % (PROMPT))
		magnet_barcode = barcode_1 if is_magnet(barcode_1) else None
		barcode = barcode_1 if not is_magnet(barcode_1) else None

		if not magnet_barcode:

			magnet_barcode = FRIDGE.product_barcodes.get(barcode)

			if magnet_barcode:
				res = raw_input('%s# BARCODE: %s | Do you want delete this product? (s/n) ' % (PROMPT, barcode))

				if res == 's':

					remove_product(magnet_barcode, barcode)
			else:
				print 'ERROR: THERE IS NOT THE PRODUCT IN THE FRIDGE'


		else:
			print 'ERROR: THAT IS A MAGNET'


	elif command == 'show':
		print FRIDGE

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


