{
    'name': "Website Product",
    'version': '16.01.0.0   ',
    'depends': ['base', 'sale_management', 'website'],
    'author': "David Dazzil",
    'category': 'Category',
    'description': "website product check",
    'application': True,
    # data files always loaded at installation

    'assets': {
        'web.assets_frontend': [
            'website_product_check/static/src/js/product_check.js',
        ],
    },

    'data': [
        'view/product_check.xml',
        # 'view/credit_partner.xml',
        # 'security/ir.model.access.csv',
    ],
}