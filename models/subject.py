from odoo import models, fields

class Subject(models.Model):
    _name = 'school.subject'
    _description = 'Subject'

    name = fields.Char(string="Subject Name", required=True)
    student_ids = fields.Many2many('school.student', string="Students")
    teacher_ids = fields.Many2many('school.teacher', string="Teachers")
