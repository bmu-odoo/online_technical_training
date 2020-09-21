# -*- coding: utf-8 -*-
{
    'name': 'Odoo Academy',

    'summary': """Academy app to manage training""",

    'description': """
        Academy Module to manage training:
        - courses
        - sessions
        - attendees
    """,

    'author': 'Odoo',
    'website': 'https://www.odoo.com',

    'category': 'Training',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitem.xml',
        'views/academy_views.xml',
    ],

    'demo': [
        'demo/academy_demo.xml',
    ],

}