# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{








    'name': 'customer sale relation ept',
    'version': '1.0',
    'category': 'Customer Sale',
    'sequence': 1,
    'summary': 'customer sale relation',
    'website': 'https://www.emiprotechnologies.com',
    'depends': ['base','sale','stock'],
    'author':'Emipro Technologies (P) Ltd.',
    
    'data': [
        
        'views/customer_sale_rel_ept_view.xml',
        'views/customer_sale_rel_ept_action.xml',
        'views/customer_sale_rel_ept_menu.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
    
    
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
