# -*- encoding: utf-8 -*-

#
# Este es el modulo de Topke
#
# Status 1.0 - tested on Open ERP 6.1.1
#

{
    'name' : 'albaran_analitico',
    'version' : '1.0',
    'category': 'Custom',
    'description': """Agrega cuenta analitica a los movimientos contables de un albaran""",
    'author': 'Rodrigo Fernandez',
    'website': 'http://solucionesprisma.com/',
    'depends' : [ 'stock_account' ],
    'demo' : [ ],
    'data' : [ 'stock_view.xml' ],
    'installable': True,
    'certificate': '',
}
