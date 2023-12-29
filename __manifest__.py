{
    'name' : 'Test Daniel',
    'version' : '1',
    'summary': 'Test Daniel ',
    'autor': 'Daniel Marchessi',
    'description': """
        Test Daniel
    """,
    'category': 'Sales',
    'depends': [
        'base','sale', 'stock', 'account'
    ],


    'data': [
        'data/sequence.xml',
        #Security
       'security/ir.model.access.csv',

        # VIEWS
        'views/canal_view.xml',
        'views/creditos_view.xml',
        'views/sale_order.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}