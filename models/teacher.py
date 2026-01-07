from odoo import models, fields

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher'

    name = fields.Char(string="Teacher Name", required=True)
    subject = fields.Char(string="Subject")
    experience = fields.Integer(string="Experience (Years)")
