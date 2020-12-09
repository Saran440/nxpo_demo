# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrExpense(models.Model):
    _name = "hr.division"
    _description = "Division of Company"
    _inherit = ["mail.thread"]
    _order = "name"

    name = fields.Char(string="Division Name", required=True)
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        index=True,
        readonly=True,
        default=lambda self: self.env.company,
    )
    active = fields.Boolean(string="Active", default=True)

    _sql_constraints = [("unique_name", "UNIQUE(name)", "Division Name must be unique")]
