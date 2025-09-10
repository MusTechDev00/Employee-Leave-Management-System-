{
    'name': 'Employee Leave Management System',
    'author': "MusTechDev00",
    'description': 'The Employee Leave Management System in Odoo 18',
    'depends': ['base', 'hr'],

    'data':
        [
            'security/leave_security_rules.xml',
            'security/ir.model.access.csv',
            'security/ir.rule.csv',

            'data/request_sequence.xml',
            'views/leave_type_views.xml',
            'views/leave_request_views.xml',
            'views/menuitem.xml',
        ],

}
