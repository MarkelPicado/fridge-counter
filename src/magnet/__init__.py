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
import imp
import glob
from magnet import Magnet
from fruit import Fruit
from meal import Meal
            

MAGNET_TYPES = {}


def load_magnets(magnets_dir):
    global MAGNET_TYPES

    for candidate_file in glob.glob(os.path.join(magnets_dir, '*.py')):

        candidate_module_name = os.path.basename(candidate_file)[:-3]

        if candidate_module_name.startswith('__'):
            continue

        try:
            with open(candidate_file, "r") as magnet_file:
                candidate_module = imp.load_module(
                    candidate_module_name, magnet_file, candidate_file,
                    ('py', 'r', imp.PY_SOURCE)
                )
        except:
            print('Cannot import `%s`' %
                          os.path.basename(candidate_file))
            continue

        magnet_type = None

        try:

            magnet_type = getattr(candidate_module, '__m_type__')

        except:

            continue

        if magnet_type:

            for element in (getattr(candidate_module, name) for name in dir(candidate_module)):
                if type(element).__name__ == 'type':
                    if issubclass(element, Magnet) and not magnet_type in MAGNET_TYPES:
                        MAGNET_TYPES[magnet_type] = element
              
    return MAGNET_TYPES



