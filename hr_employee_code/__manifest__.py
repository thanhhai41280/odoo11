# -*- coding: utf-8 -*-
{
    'name': "hr_employee_code",

    'summary': """
        - add code reference to employees
        - add contrain Unique for reference code              
    """,

    'description': """
        
    """,

    'author': "ERPTOANCAU",
    'website': "http://www.erptoancau.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Outsource',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',        
        'views/hr_view.xml',
        
    ],
}