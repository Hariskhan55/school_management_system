from odoo import models, fields, api


class Classroom(models.Model):
    _name = 'school.classroom'
    _description = 'Classroom'

    name = fields.Char(string="Class Name", required=True)
    section = fields.Char(string="Section")
    teacher_id = fields.Many2one('school.teacher', string="Teacher")

    student_ids = fields.One2many(
        'school.student',
        'classroom_id',
        string="Students"
    )

    @api.model
    def classroom_exists(self, name):
        return bool(self.search([('name', '=', name)], limit=1))
