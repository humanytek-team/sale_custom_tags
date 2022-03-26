from odoo import api, fields, models


class SaleOder(models.Model):
    _inherit = "sale.order"

    tag_ids = fields.Many2many(
        string="Other Tags",
    )
    brand_tag_ids = fields.Many2many(
        comodel_name="crm.brand_tag",
    )
    vertical_tag_ids = fields.Many2many(
        comodel_name="crm.vertical_tag",
    )

    def _prepare_invoice(self):
        invoice_vals = super()._prepare_invoice()
        invoice_vals["tag_ids"] = [(6, 0, self.tag_ids.ids)]
        invoice_vals["brand_tag_ids"] = [(6, 0, self.brand_tag_ids.ids)]
        invoice_vals["vertical_tag_ids"] = [(6, 0, self.vertical_tag_ids.ids)]
        return invoice_vals
