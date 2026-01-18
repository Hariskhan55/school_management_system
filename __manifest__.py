{
    'name': 'School Management System',
    'version': '1.0',
    'summary': 'Manage students, teachers, classrooms, subjects and fees',
    'category': 'Education',
    'author': 'Your Name',
    'website': 'https://example.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/student.xml',
        'views/teacher.xml',
        'views/classroom.xml',
        'views/subject.xml',
    ],
    'installable': True,
    'application': True,
}
