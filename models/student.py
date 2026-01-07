from odoo import models, fields

class Student(models.Model):
    _name = 'school.student'
    _description = 'Student'

    name = fields.Char(string="Student Name", required=True)
    age = fields.Integer(string="Age")
    grade = fields.Char(string="Grade")
