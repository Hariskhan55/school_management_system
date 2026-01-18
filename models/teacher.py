from odoo import models, fields

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher'

    name = fields.Char(string="Teacher Name", required=True)
    subject_ids = fields.Many2many('school.subject', string="Subjects")
    classroom_ids = fields.One2many('school.classroom', 'teacher_id', string="Classrooms")
