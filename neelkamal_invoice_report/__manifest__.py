# __manifest__.py

{
    'name': 'Invoice and Report',
    'version': '1.2', 
    'summary': 'Customized tax invoice and pro-forma invoice reports for Neelkamal Industries.',
    'category': 'Accounting/Reporting',
    'author': 'Pratham',
    'depends': [
        'account',
        'sale_management',
    ],
    'data': [
        'report/report.xml',
        'report/invoice_template.xml',
        'report/sale_report_template.xml',
        'views/account_move_view.xml',
        'views/product_template_view.xml',
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}