# -*- coding: utf-8 -*-
{
    'name': 'School Management System',
    'version': '1.0',
    'summary': 'Manage Students and Teachers',
    'description': """
School Management System Module
- Manage students
- Manage teachers
- Simple school management
""",
    'author': 'Your Name',
    'website': 'http://www.yourwebsite.com',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student.xml',
        'views/teacher.xml',
        'views/classroom.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
