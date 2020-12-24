# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class MisBudgetItem(models.Model):
    _inherit = "mis.budget.item"

    is_readonly = fields.Boolean(compute="_compute_amount_readonly")

    @api.depends("budget_control_id")
    def _compute_amount_readonly(self):
        today = fields.Date.context_today(self)
        for rec in self:
            rec.is_readonly = (
                (rec.date_from < today or today > rec.date_to) and True or False
            )
