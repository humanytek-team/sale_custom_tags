from odoo import fields, models


class CRMVerticalTag(models.Model):
    _name = "crm.vertical_tag"

    name = fields.Char(
        index=True,
    )
