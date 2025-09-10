from odoo import models, fields, api

class LeaveTypes(models.Model):
    _name = "leave.type"
    _description = "Leave Types"

    name = fields.Char('Name')
    limit = fields.Integer('Limit')
    is_paid = fields.Boolean('Is Paid')
    description_leave = fields.Text("Description")

