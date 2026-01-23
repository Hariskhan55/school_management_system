from odoo import models, fields, api
from odoo.exceptions import AccessError


class Teacher(models.Model):
    _name = "school.teacher"
    _description = "Teacher"

    # =====================
    # BASIC INFO
    # =====================
    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    section = fields.Char(string="Section")

    # LINK TO USER (VERY IMPORTANT FOR SECURITY)
    user_id = fields.Many2one(
        'res.users',
        string="Related User",
        help="User account linked with this teacher"
    )

    # =====================
    # ACADEMIC INFO
    # =====================
    subject_ids = fields.Many2many(
        'school.subject',
        string="Subjects"
    )

    # =====================
    # SALARY INFO (ADMIN ONLY VIA ACCESS RIGHTS)
    # =====================
    salary = fields.Monetary(string="Salary")
    currency_id = fields.Many2one(
        'res.currency',
        string="Currency",
        default=lambda self: self.env.company.currency_id
    )

    # =====================
    # BANK DETAILS (NEW)
    # =====================
    bank_name = fields.Char(string="Bank Name")
    bank_account_number = fields.Char(string="Account Number")
    bank_ifsc = fields.Char(string="IFSC Code")
    bank_branch = fields.Char(string="Branch Name")

    # =====================
    # SECURITY CHECK (IMPORTANT)
    # =====================
    @api.model
    def create(self, vals):
        """
        Teachers cannot create teacher records.
        Only Admin can create.
        """
        if self.env.user.has_group('school_management_system.group_school_teacher'):
            raise AccessError("Teachers are not allowed to create teacher records.")
        return super().create(vals)

    def write(self, vals):
        """
        Teacher can edit ONLY their own bank details.
        Admin can edit everything.
        """
        for rec in self:
            # If teacher group
            if self.env.user.has_group('school_management_system.group_school_teacher'):
                if rec.user_id != self.env.user:
                    raise AccessError(
                        "You can only modify your own bank details."
                    )
        return super().write(vals)
