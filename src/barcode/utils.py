###############################################################################
###############################################################################
###############################################################################

''' 
En este modulo se define las variables y funciones necesarias para usar
en el modulo barcode
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

EAN_BARCODE_COUNTRIES = {
    '000': 'US/CA',
    '001': 'US/CA',
    '002': 'US/CA',
    '003': 'US/CA',
    '004': 'US/CA',
    '005': 'US/CA',
    '006': 'US/CA',
    '007': 'US/CA',
    '008': 'US/CA',
    '009': 'US/CA',
    '010': 'US/CA',
    '011': 'US/CA',
    '012': 'US/CA',
    '013': 'US/CA',
    '020': 'INTERNAL-USE',
    '021': 'INTERNAL-USE',
    '022': 'INTERNAL-USE',
    '023': 'INTERNAL-USE',
    '024': 'INTERNAL-USE',
    '025': 'INTERNAL-USE',
    '026': 'INTERNAL-USE',
    '027': 'INTERNAL-USE',
    '028': 'INTERNAL-USE',
    '029': 'INTERNAL-USE',
    '030': 'FR',
    '031': 'FR',
    '032': 'FR',
    '033': 'FR',
    '034': 'FR',
    '035': 'FR',
    '036': 'FR',
    '037': 'FR',
    '380': 'BG',
    '383': 'SI',
    '385': 'HR',
    '387': 'BA',
    '400': 'DE',
    '401': 'DE',
    '402': 'DE',
    '403': 'DE',
    '404': 'DE',
    '405': 'DE',
    '406': 'DE',
    '407': 'DE',
    '408': 'DE',
    '409': 'DE',
    '410': 'DE',
    '411': 'DE',
    '412': 'DE',
    '413': 'DE',
    '420': 'DE',
    '421': 'DE',
    '422': 'DE',
    '423': 'DE',
    '424': 'DE',
    '425': 'DE',
    '426': 'DE',
    '427': 'DE',
    '428': 'DE',
    '429': 'DE',
    '430': 'DE',
    '431': 'DE',
    '432': 'DE',
    '433': 'DE',
    '434': 'DE',
    '435': 'DE',
    '436': 'DE',
    '437': 'DE',
    '438': 'DE',
    '439': 'DE',
    '440': 'DE',
    '445': 'JA',
    '449': 'JA',
    '460': 'RU',
    '461': 'RU',
    '462': 'RU',
    '463': 'RU',
    '464': 'RU',
    '465': 'RU',
    '466': 'RU',
    '467': 'RU',
    '468': 'RU',
    '469': 'RU',
    '471': 'TW',
    '474': 'EE',
    '475': 'LV',
    '476': 'AZ',
    '477': 'LT',
    '478': 'UZ',
    '479': 'LK',
    '480': 'PH',
    '481': 'BY',
    '482': 'UA',
    '484': 'MD',
    '485': 'AM',
    '486': 'GE',
    '487': 'KZ',
    '489': 'HK',
    '050': 'GB',
    '520': 'GR',
    '528': 'LB',
    '529': 'CY',
    '531': 'MK',
    '535': 'MT',
    '539': 'IE',
    '054': 'BE/LU',
    '560': 'PT',
    '569': 'IS',
    '057': 'DK',
    '590': 'PL',
    '594': 'RO',
    '599': 'HU',
    '600': 'ZA',
    '601': 'ZA',
    '608': 'BH',
    '609': 'MU',
    '611': 'MA',
    '613': 'DZ',
    '616': 'KE',
    '619': 'TN',
    '621': 'SY',
    '622': 'EG',
    '624': 'LY',
    '625': 'JO',
    '626': 'IR',
    '627': 'KW',
    '628': 'SA',
    '629': 'AE',
    '064': 'FI',
    '690': 'CN',
    '695': 'CN',
    '070': 'NO',
    '729': 'IL',
    '073': 'SE',
    '740': 'GT',
    '741': 'SV',
    '742': 'HN',
    '743': 'NI',
    '744': 'CR',
    '745': 'PA',
    '746': 'DO',
    '750': 'MX',
    '759': 'VE',
    '076': 'CH',
    '770': 'CO',
    '773': 'UY',
    '775': 'PE',
    '777': 'BO',
    '779': 'AR',
    '780': 'CL',
    '784': 'PY',
    '786': 'EC',
    '789': 'BR',
    '790': 'BR',
    '080': 'IT',
    '081': 'IT',
    '082': 'IT',
    '083': 'IT',
    '084': 'ES',
    '850': 'CU',
    '858': 'SK',
    '859': 'CZ',
    '860': 'YU' ,
    '867': 'KP',
    '869': 'TR',
    '087': 'NL',
    '880': 'KR',
    '885': 'TH',
    '888': 'SG',
    '890': 'IN',
    '893': 'VN',
    '899': 'ID',
    '090': 'AT',
    '091': 'AT',
    '093': 'AU',
    '094': 'NZ',
    '955': 'MY',
    '958': 'MO',
    '977': 'ISSN',
    '978': 'ISBN',
    '979': 'ISBN',
    '980': 'RECEIPTS',
    '981': 'COMMON CURRENCY COUPONS',
    '982': 'COMMON CURRENCY COUPONS',
    '099':  'COUPONS'
}