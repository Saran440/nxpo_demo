# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class BudgetMonitorReport(models.Model):
    _inherit = "budget.monitor.report"

    project_id = fields.Many2one(
        comodel_name="res.project",
    )
    parent_project = fields.Char(string="Parent Project")

    def _select_project_common(self, select_query):
        select_query = ",".join([
            select_query, "aa.project_id, rp.parent_project"])
        return select_query

    def _from_project_common(self, from_query, join):
        from_query = "\n".join(
            [
                from_query,
                """
                join account_analytic_account aa on %s
                left outer join res_project rp on aa.project_id = rp.id
            """
                % (join),
            ]
        )
        return from_query

    # Budget
    def _select_budget(self):
        select_budget_query = super()._select_budget()
        select_budget_query = self._select_project_common(select_budget_query)
        return select_budget_query

    def _from_budget(self):
        from_budget_query = super()._from_budget()
        from_budget_query = self._from_project_common(
            from_budget_query, "mbi.analytic_account_id = aa.id"
        )
        return from_budget_query

    # Actual
    def _select_actual(self):
        select_actual_query = super()._select_actual()
        select_actual_query = self._select_project_common(select_actual_query)
        return select_actual_query

    def _from_actual(self):
        from_actual_query = super()._from_actual()
        from_actual_query = self._from_project_common(
            from_actual_query, "aml.analytic_account_id = aa.id"
        )
        return from_actual_query

    # Expense
    def _select_ex_commit(self):
        select_ex_query = super()._select_ex_commit()
        select_ex_query = self._select_project_common(select_ex_query)
        return select_ex_query

    def _from_ex_commit(self):
        from_ex_query = super()._from_ex_commit()
        from_ex_query = self._from_project_common(
            from_ex_query, "a.analytic_account_id = aa.id"
        )
        return from_ex_query

    # Purchase Request
    def _select_pr_commit(self):
        select_ex_query = super()._select_pr_commit()
        select_ex_query = self._select_project_common(select_ex_query)
        return select_ex_query

    def _from_pr_commit(self):
        from_ex_query = super()._from_pr_commit()
        from_ex_query = self._from_project_common(
            from_ex_query, "a.analytic_account_id = aa.id"
        )
        return from_ex_query

    # Purchase
    def _select_po_commit(self):
        select_ex_query = super()._select_po_commit()
        select_ex_query = self._select_project_common(select_ex_query)
        return select_ex_query

    def _from_po_commit(self):
        from_ex_query = super()._from_po_commit()
        from_ex_query = self._from_project_common(
            from_ex_query, "a.analytic_account_id = aa.id"
        )
        return from_ex_query
