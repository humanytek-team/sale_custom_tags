from odoo import fields, models


class CRMBrandTag(models.Model):
    _name = "crm.brand_tag"

    name = fields.Char(
        index=True,
    )
