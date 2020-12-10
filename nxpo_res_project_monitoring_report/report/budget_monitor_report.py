# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class BudgetMonitorReport(models.Model):
    _inherit = "budget.monitor.report"

    project_id = fields.Many2one(
        comodel_name="res.project",
    )
    parent_project = fields.Char(string="Parent Project")

    def _select_budget(self):
        select_budget_query = super()._select_budget()
        select_budget_query = ",".join([
            select_budget_query, "aa.project_id, rp.parent_project"])
        return select_budget_query

    def _from_budget(self):
        from_budget_query = super()._from_budget()
        from_budget_query = "\n".join([
            from_budget_query,
            """ join account_analytic_account aa
                on mbi.analytic_account_id = aa.id
                left outer join res_project rp on aa.project_id = rp.id """])
        return from_budget_query

    def _select_actual(self):
        select_actual_query = super()._select_actual()
        select_actual_query = ",".join([
            select_actual_query, "aa.project_id, rp.parent_project"])
        return select_actual_query

    def _from_actual(self):
        from_actual_query = super()._from_actual()
        from_actual_query = "\n".join([
            from_actual_query,
            """ join account_analytic_account aa
                on aml.analytic_account_id = aa.id
                left outer join res_project rp on aa.project_id = rp.id  """])
        return from_actual_query
