# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class BudgetMonitorReport(models.Model):
    _inherit = "budget.monitor.report"

    activity_name = fields.Char(string="Activity Name")

    def _select_query_common(self, select_query, value):
        select_query = ",".join([select_query, value])
        return select_query

    def _from_query_common(self, from_query, value):
        from_query = "\n".join([from_query, value])
        return from_query

    # Budget
    def _select_budget(self):
        select_budget_query = super()._select_budget()
        select_budget_query = self._select_query_common(
            select_budget_query, "null::char as activity_name")
        return select_budget_query

    # Actual
    def _select_actual(self):
        select_actual_query = super()._select_actual()
        select_actual_query = self._select_query_common(
            select_actual_query, "ba.name as activity_name")
        return select_actual_query

    def _from_actual(self):
        from_actual_query = super()._from_actual()
        from_actual_query = self._from_query_common(
            from_actual_query,
            "left outer join budget_activity ba on aml.activity_id = ba.id"
        )
        return from_actual_query

    # Purchase
    def _select_po_commit(self):
        select_po_query = super()._select_po_commit()
        select_po_query = self._select_query_common(
            select_po_query, "ba.name as activity_name")
        return select_po_query

    def _from_po_commit(self):
        from_po_query = super()._from_po_commit()
        from_po_query = self._from_query_common(
            from_po_query,
            "left outer join budget_activity ba on a.activity_id = ba.id"
        )
        return from_po_query

    # Purchase Request
    def _select_pr_commit(self):
        select_pr_query = super()._select_pr_commit()
        select_pr_query = self._select_query_common(
            select_pr_query, "ba.name as activity_name")
        return select_pr_query

    def _from_pr_commit(self):
        from_pr_query = super()._from_pr_commit()
        from_pr_query = self._from_query_common(
            from_pr_query,
            "left outer join budget_activity ba on a.activity_id = ba.id"
        )
        return from_pr_query

    # Expense
    def _select_ex_commit(self):
        select_ex_query = super()._select_ex_commit()
        select_ex_query = self._select_query_common(
            select_ex_query, "ba.name as activity_name")
        return select_ex_query

    def _from_ex_commit(self):
        from_ex_query = super()._from_ex_commit()
        from_ex_query = self._from_query_common(
            from_ex_query,
            "left outer join budget_activity ba on a.activity_id = ba.id"
        )
        return from_ex_query
