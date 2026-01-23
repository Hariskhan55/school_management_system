{
    'name': 'School Management System',
    'version': '1.0',
    'summary': 'Manage students, teachers, classrooms, subjects and fees',
    'category': 'Education',
    'author': 'Your Name',
    'depends': [
        'base',
        'account'
    ], 
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
'views/menu.xml',
        'reports/student_action.xml',
        'reports/student_template.xml',
        'views/student.xml',
        'views/classroom.xml',
        'views/subject.xml',
        'reports/teacher_template.xml',
        'reports/teacher_action.xml',
        'reports/classroom_action.xml',
        'reports/classroom_template.xml',
        'views/teacher.xml',
    ],

    'installable': True,
    'application': True,
}
