# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "NxPO Budget Revision Monitoring - Project",
    "summary": "Budget Revision Monitoring with Project",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Ecosoft, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/account-budgeting",
    "depends": [
        "budget_control_revision_department_monitoring",
        "nxpo_res_project_analytic",
    ],
    "data": [
        "report/budget_monitor_revision_view.xml",
    ],
    "maintainers": ["Saran440"],
    "development_status": "Alpha",
}
