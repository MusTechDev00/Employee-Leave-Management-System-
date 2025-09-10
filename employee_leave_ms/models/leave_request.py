from odoo import fields, models, api, _


class LeaveRequest(models.Model):
    _name = "leave.request"
    _description = "Leave Request"

    name = fields.Char("Request Id", default="New", readonly=True, required=True)
    # employee_id = fields.Many2one('hr.employee')
    leave_type_id = fields.Many2one('leave.type')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('Start Date')
    number_of_days = fields.Float('Number of days', compute="_compute_number_of_days")
    reason = fields.Text("Reason")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('to_approve', 'To Approve'),
        ('approved', 'Approved'),
        ('refused', 'Refused'),
        ('canceled', 'Canceled'),
    ], string="Status", default="draft")

    manager_id = fields.Many2one('hr.employee')
    rejection_reason = fields.Text("Rejection Reason")

    @api.depends('start_date', 'end_date')
    def _compute_number_of_days(self):
        for rec in self:
            if rec.start_date and rec.end_date:
                rec.number_of_days = (rec.end_date - rec.start_date).days + 1
            else:
                rec.number_of_days = 0

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('leave.request') or _('New')
        return super(LeaveRequest, self).create(vals)

    def action_submit_request(self):
        self.write({'state': 'to_approve'})

    def action_approve_request(self):
        self.write({'state': 'approved'})
        # Optional: Add logic here to deduct leave days from the employee's balance

    def action_refuse_request(self):
        self.write({'state': 'refused'})

    def action_cancel_request(self):
        self.write({'state': 'canceled'})

    def write(self, vals):
        # If normal employee tries to change state or rejection_reason, block
        if not self.env.user.has_group('employee_leave_ms.group_leave_manager'):
            if 'state' in vals or 'rejection_reason' in vals:
                raise models.ValidationError("You are not allowed to update the state or rejection reason.")
        return super(LeaveRequest, self).write(vals)

    employee_id = fields.Many2one(
        'hr.employee',
        string="Employee",
        domain=lambda self: self._get_employee_domain()
    )

    @api.model
    def _get_employee_domain(self):
        """Restrict employees for normal users, allow all for managers"""
        if self.env.user.has_group('employee_leave_ms.group_leave_manager'):
            return []  # no restriction → managers see all
        return [('user_id', '=', self.env.uid)]
