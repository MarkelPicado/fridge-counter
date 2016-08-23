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
from magnet import MAGNET_TYPES
from fridge_errors import RepeatedMagnetError, InvalidMagnetError, MagnetConflictError, InvalidProductError


class Fridge(object):

    def __init__(self, type, id):

        self.type = type

        self.id = id

        self.products_barcodes = {}

        self.magnets = {}


    def add_magnet(self, m):

        if not m.barcode in self.magnets.keys():

            self.magnets[m.barcode] = m
        else:

            raise RepeatedMagnetError('The magnet with barcode %s already exists as %s' % (m.barcode, self.magnets[m.barcode].magnet_name))


    def remove_magnet(self, obj):

        obj_type = type(obj)

        if isinstance(obj, str):

            if obj in self.magnets.keys():

                self.magnets.pop(obj)

        elif isinstance(obj, Magnet):

            if obj.barcode in self.magnets.keys():

                self.magnets.pop(obj.barcode)


    def add_product(self, magnet_barcode, p):
        if magnet_barcode in self.magnets.keys() and isinstance(p, Product):

            if p.barcode.barcode in self.products_barcodes:

                if magnet_barcode == self.products_barcodes[p.barcode.barcode]:

                    self.magnets[magnet_barcode].link_product(p)

                    self.products_barcodes[p.barcode.barcode] = magnet_barcode

                else:

                    raise MagnetConflictError('The product %s is recorded as %s' % (p.name, self.magnets[magnet_barcode].magnet_name))
            
            else:

                self.magnets[magnet_barcode].link_product(p)

                self.products_barcodes[p.barcode.barcode] = magnet_barcode


        elif magnet_barcode == p.barcode.barcode:

            raise InvalidProductError('This is a magnet')

        else:

            raise InvalidMagnetError('There is not linked the magnet whit barcode: %s' % magnet_barcode)


    def get_product(self, obj):


        if isinstance(obj, Product):

            if obj.barcode.barcode in self.products_barcodes.keys():

                magnet_barcode = self.products_barcodes[obj.barcode.barcode]

                products = self.magnets[magnet_barcode].linked_products[obj.barcode.barcode]

            else:

                raise InvalidMagnetError('The product whit barcode: %s is not in the fridge' % obj.barcode.barcode)


        elif isinstance(obj, str):

            if obj in self.products_barcodes.keys():

                magnet_barcode = self.products_barcodes[obj]

                products = self.magnets[magnet_barcode].linked_products[obj]

            else:

                raise InvalidMagnetError('The product whit barcode: %s is not in the fridge' % obj)


        elif isinstance(obj, dict):

            if obj['barcode'] in self.products_barcodes.keys():

                magnet_barcode = self.products_barcodes[obj['barcode']]

                products = self.magnets[magnet_barcode].linked_products[obj['barcode']]

            else:

                raise InvalidMagnetError('The product whit barcode: %s is not in the fridge' % obj)
        
        else:
            #TODO Change error type
            raise InvalidMagnetError('Unimplemented class to get product: %s' % magnet_barcode)


        return products


    def remove_product(self, barcode, units=1):
        product = self.get_product(barcode)[0]

        magnet_barcode = self.products_barcodes[product.barcode.barcode]

        self.magnets[magnet_barcode].unlink_product(product, units)

        if product.units < 1:
            self.products_barcodes.pop(barcode)



    def is_in(self, barcode):

        return barcode in self.products_barcodes

    def __str__(self):

        string = ''

        magnet_types = {}

        for t in MAGNET_TYPES:

            magnet_types[t] = []

        for m in self.magnets.values():

            for linked_products in m.linked_products.values():

                magnet_types[m.magnet_type].append(linked_products)

        for magnet_type in magnet_types:

            string += '[%s]\n' % magnet_type

            product_lists = magnet_types[magnet_type]

            for product_list in product_lists:

                for product in product_list:

                    string += '%s\t+ [%s] %s || %s: \n\t\t- %s\n\t\tAdded date - (%s)\n' % (product.barcode.barcode, product.units, product.name, product.used_by.strftime('%Y-%m-%d'), product.description, product.created_date.strftime('%Y-%m-%d'))

        if len(string):

            return string

        return 'EMPTY FRIGE'
