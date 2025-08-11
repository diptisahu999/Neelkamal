{
    'name': 'Neelkamal Invoice Report',
    'version': '17.0',
    'summary': 'Custom Invoice Format for Neelkamal Industries',
    'depends': ['account', 'base', 'stock', 'l10n_in'],
    'data': [
    'report/report.xml',
    'report/invoice_template.xml',
    'views/product_template_view.xml',
    'views/account_move_view.xml',
],
    'installable': True,
    'application': False,
    'auto_install': False,
}



