# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class Department(models.Model):
    _inherit = "hr.department"

    division_parent_id = fields.Many2one(
        comodel_name="hr.division", string="Parent Division", index=True
    )

    @api.depends("name", "parent_id.complete_name", "division_parent_id.name")
    def _compute_complete_name(self):
        super()._compute_complete_name()
        for department in self:
            if department.division_parent_id:
                department.complete_name = "{} / {}".format(
                    department.division_parent_id.name,
                    department.complete_name,
                )
