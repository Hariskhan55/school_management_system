from odoo import models, fields


class Teacher(models.Model):
    _name = "school.teacher"
    _description = "Teacher"

    # BASIC INFO
    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    section = fields.Char(string="Section")

    teacher_id = fields.Many2one(
        'school.teacher',
        string="Teacher"
    )
    # LINK TO USER (VERY IMPORTANT FOR SECURITY)
    user_id = fields.Many2one(
        'res.users',
        string="Related User",
        help="User account linked with this teacher"
    )

    # ACADEMIC INFO
    subject_ids = fields.Many2many(
        'school.subject',
        string="Subjects"
    )

    # SALARY INFO
    salary = fields.Monetary(string="Salary")
    currency_id = fields.Many2one(
        'res.currency',
        string="Currency",
        default=lambda self: self.env.company.currency_id
    )
