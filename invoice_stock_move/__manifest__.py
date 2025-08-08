{
    'name': "Stock Picking From Invoice",
    'version': '17.0',
    'category': 'Accounting',
    'summary': """Stock Picking From Customer/Supplier Invoice""",
    'description': """This Module Enables To Create Stocks Picking From 
     Customer/Supplier Invoice""",
    'depends': ['account', 'stock', 'payment'],
    'data': [
             'views/account_move_views.xml',
             'views/inherit_stock.xml',
             'views/stock_picking.xml',],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,

}
