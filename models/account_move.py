from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    tag_ids = fields.Many2many(
        string="Other Tags",
        comodel_name="crm.lead.tag",
        readonly=True,
    )
    brand_tag_ids = fields.Many2many(
        comodel_name="crm.brand_tag",
        readonly=True,
    )
    vertical_tag_ids = fields.Many2many(
        comodel_name="crm.vertical_tag",
        readonly=True,
    )
