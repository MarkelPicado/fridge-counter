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

class Fridge(object):

    def __init__(self, type, id):

        self.type = type,
        self.id = id
        self.product_barcodes = {}
        self.magnets = {}

    def add_magnet(self, m):
        if not m.barcode in self.magnets.keys():
            self.magnets[m.barcode] = m

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
            if p.barcode.barcode in self.product_barcodes:
                if magnet_barcode == self.product_barcodes[p.barcode.barcode]:
                    self.magnets[magnet_barcode].link_product(p)
                    self.product_barcodes[p.barcode.barcode] = magnet_barcode
                else:
                    print 'ERROR: THERE IS A %s IT IS NOT A %s' % (self.magnets[magnet_barcode].magnet_name, self.magnets[self.product_barcodes[p.barcode.barcode]].magnet_name)
            else:
                self.magnets[magnet_barcode].link_product(p)
                self.product_barcodes[p.barcode.barcode] = magnet_barcode

    def kinds_of_product(self, magnet_barcode, obj):
        if magnet_barcode in self.magnets.keys():
            if isinstance(obj, Product):
                    if self.magnets[magnet_barcode].linked_products.get(obj.barcode.barcode):
                        products = self.magnets[magnet_barcode].linked_products.get(obj.barcode.barcode)


            if isinstance(obj, str):
                if self.magnets[magnet_barcode].linked_products.get(obj):
                    products = self.magnets[magnet_barcode].linked_products.get(obj)

        return products

    def remove_product(self, magnet_barcode, obj, units=1):
        if magnet_barcode in self.magnets.keys():
            self.magnets[magnet_barcode].unlink_product(obj, units)


    def is_in(self, barcode):
        return barcode in self.product_barcodes

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
