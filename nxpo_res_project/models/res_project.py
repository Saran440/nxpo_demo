# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ResProject(models.Model):
    _name = "res.project"
    _description = "Project Management"
    _inherit = "mail.thread"
    _order = "sequence, id"
    _check_company_auto = True

    name = fields.Char(
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        tracking=True,
    )
    parent_project = fields.Char(readonly=True)
    description = fields.Html(
        readonly=True, copy=False, states={"draft": [("readonly", False)]}
    )
    active = fields.Boolean(
        default=True,
        help="If the active field is set to False, "
        "it will allow you to hide the project without removing it.",
    )
    sequence = fields.Integer(
        default=10,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Gives the sequence order when displaying a list of Projects.",
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        required=True,
        readonly=True,
        default=lambda self: self.env.company,
    )
    user_id = fields.Many2one(
        comodel_name="res.users",
        string="Project Manager",
        default=lambda self: self.env.user,
        readonly=True,
        states={"draft": [("readonly", False)]},
        tracking=True,
    )
    date_from = fields.Date(
        required=True,
        string="Project Start",
        readonly=True,
        states={"draft": [("readonly", False)]},
        tracking=True,
    )
    date_to = fields.Date(
        required=True,
        string="Project End",
        readonly=True,
        states={"draft": [("readonly", False)]},
        tracking=True,
    )
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirm", "Confirmed"),
            ("close", "Closed"),
            ("cancel", "Cancelled"),
        ],
        string="Status",
        required=True,
        readonly=True,
        copy=False,
        tracking=True,
        default="draft",
    )

    _sql_constraints = [("unique_name", "UNIQUE(name)", "name must be unique")]

    @api.model
    def create(self, vals):
        if not vals.get("parent_project", False):
            vals["parent_project"] = vals["name"]
        return super().create(vals)

    def copy(self, default=None):
        self.ensure_one()
        if default is None:
            default = {}
        if "name" not in default:
            default["name"] = _("%s (copy)") % (self.name)
            name_duplicate = self.search_count([("name", "=", default["name"])])
            if name_duplicate:
                raise UserError(_("Name is duplicated."))
        res = super().copy(default=default)
        return res

    def action_split_project(self):
        for project in self.browse(self.env.context["active_ids"]):
            project_id = project.copy()
        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "res.project",
            "res_id": project_id.id,
        }

    def action_confirm(self):
        return self.write({"state": "confirm"})

    def action_close_project(self):
        return self.write({"state": "close"})

    def action_draft(self):
        return self.write({"state": "draft"})

    def action_cancel(self):
        return self.write({"state": "cancel"})
