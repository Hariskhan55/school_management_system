from odoo import models, fields

class Teacher(models.Model):
    _name = "school.teacher"
    _description = "Teacher"

    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    subject_ids = fields.Many2many('school.subject', string="Subjects")
    salary = fields.Monetary(string="Salary")
    currency_id = fields.Many2one(
        'res.currency',
        default=lambda self: self.env.company.currency_id
    )
