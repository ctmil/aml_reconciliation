# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Account move line reconciliation',
    'version': '1.0',
    'category': 'Accounting',
    'depends': ['account','base'],
    'data': [
        'wizard/wizard_view.xml',
        'security/ir.model.access.csv',
        ],
    'demo': [
        ],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
