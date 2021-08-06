from odoo import fields, models

class HrAppraisalGoal(models.Model):
    _name = "hr.appraisal.goal"
    _description = "Appraisal Goal Management"

    name = fields.Char(required=True)
    employee_id = fields.Many2one('hr.employee', string="Owner",
        default=lambda self: self.env.user.employee_id, required=True)
    manager_id = fields.Many2one('hr.employee', string="Challenged By", required=True)
    progression = fields.Selection(selection=[
        ('0', '0 %'),
        ('25', '25 %'),
        ('50', '50 %'),
        ('75', '75 %'),
        ('100', '100 %')
    ], string="Progression", default="0", required=True)
    description = fields.Text()
    deadline = fields.Date()

    def action_confirm(self):
        self.write({'progression': '100'})
