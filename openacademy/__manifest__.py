# Copyright 2020, Jarsa
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    'name': 'Openacademy',
    'summary': 'Module to teach how to make a module',
    'version': '12.0.1.0.0',
    'category': 'Tecmur',
    'website': 'https://www.jarsa.com.mx/',
    'author': 'Jarsa, Odoo Community Association (OCA), Tecmur',
    'license': 'LGPL-3',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/openacademy_course_views.xml',
        'views/openacademy_session_views.xml',
        'views/openacademy_material_views.xml',
        'views/res_partner_views.xml',
        'views/res_partner_category_views.xml',
        'data/res_partner_data.xml',
    ],
    'demo': [
        'demo/openacademy_course.xml',
    ],
}
