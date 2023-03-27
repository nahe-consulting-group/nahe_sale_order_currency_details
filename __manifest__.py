{
    'name': 'Nahe Sale Order Currency Details',
    'version': '15.0.0.1',
    'author': 'Nähe Consulting Group',
    'category': 'Sales',
    'summary': 'Add currency details to sale order report',
    'description': """
This module adds currency details and converted amounts to the sale order report.
""",
    'depends': ['base','sale','account'],
    'data': [
        'data/currency_data.xml',
        'views/sale_order_currency_details.xml',
        'views/account_move_currency_details.xml',
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'application': False,
}
