from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    code_interne = fields.Char(
        string="Code interne",
        help="Code interne unique pour identification"
    )
