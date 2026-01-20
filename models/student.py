from odoo import models, fields, api
from datetime import date


class Student(models.Model):
    _name = "school.student"
    _description = "Student"

    # BASIC INFO
    name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    parent_contact = fields.Char(string="Parent Contact")

    display_name = fields.Char(
        string="Display Name",
        compute="_compute_display_name",
        store=True,
        readonly=True
    )

    dob = fields.Date(string="Date of Birth")

    age = fields.Integer(
        string="Age",
        compute="_compute_age",
        store=True,
        readonly=True
    )

    grade = fields.Char(string="Grade")

    classroom_id = fields.Many2one(
        'school.classroom',
        string="Classroom"
    )

    subject_ids = fields.Many2many(
        'school.subject',
        string="Subjects"
    )

    # STATUS (DROPDOWN)
    status = fields.Selection(
        [
            ('draft', 'Draft'),
            ('active', 'Active'),
            ('passed', 'Passed'),
            ('dropped', 'Dropped'),
        ],
        string="Status",
        default='draft'
    )

    passing_date = fields.Date(string="Passing Date")
    drop_date = fields.Date(string="Drop Date")

    # FEES (MONETARY)
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        required=True,
        default=lambda self: self.env.company.currency_id
    )

    tuition_fee = fields.Monetary(
        string="Tuition Fee",
        currency_field='currency_id'
    )

    # COMPUTES
    @api.depends('name', 'last_name')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.name} {rec.last_name}"

    @api.depends('dob')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.dob:
                rec.age = today.year - rec.dob.year - (
                    (today.month, today.day) < (rec.dob.month, rec.dob.day)
                )
            else:
                rec.age = 0

    # BUTTON ACTIONS
    def action_confirm_student(self):
        for rec in self:
            rec.status = 'active'
        return True

    def action_cancel_student(self):
        return {'type': 'ir.actions.act_window_close'}
