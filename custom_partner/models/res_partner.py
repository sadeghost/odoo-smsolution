from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    code_interne = fields.Char(string='Code Interne', help='Code interne du partenaire')
    note_interne = fields.Text(string='Note Interne', help='Note interne pour le suivi du partenaire')
