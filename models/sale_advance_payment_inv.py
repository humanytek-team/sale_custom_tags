from odoo import models


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _prepare_invoice_values(self, order, name, amount, so_line):
        invoice_vals = super()._prepare_invoice_values(order, name, amount, so_line)
        invoice_vals["tag_ids"] = [(6, 0, order.tag_ids.ids)]
        invoice_vals["brand_tag_ids"] = [(6, 0, order.brand_tag_ids.ids)]
        invoice_vals["vertical_tag_ids"] = [(6, 0, order.vertical_tag_ids.ids)]
        return invoice_vals
