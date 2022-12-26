{
    'name': "Inventory Dashboard",
    'version': '16.01.0.0   ',
    'depends': ['base', 'sale_management', 'project', 'stock', 'hr'],
    'author': "David Dazzil",
    'category': 'Category',
    'description': "Inventory Dashboard",
    'application': True,
    # data files always loaded at installation

    'assets': {
        'web.assets_backend': [
            'inventory_dashboard/static/src/js/inventory_dashboard.js',
            'inventory_dashboard/static/src/xml/inventory_dashboard.xml',
            'inventory_dashboard/static/src/css/inventory_dashboard.css',
            'https://www.gstatic.com/charts/loader.js'
        ],
    },

    'data': [
        'view/inventory_dashboard_menu.xml',
        # 'view/credit_partner.xml',
        # 'security/ir.model.access.csv',
    ],
}
