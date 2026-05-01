from odoo import models, fields


class SaleOrder(models.Model):
    """Héritage du modèle sale.order pour ajouter des champs SMSolution.
    
    Ce module illustre comment personnaliser un module natif Odoo
    sans modifier le code source original. On utilise _inherit pour
    étendre le modèle existant.
    """
    _inherit = 'sale.order'

    project_ref = fields.Char(
        string='Référence Projet',
        help='Référence interne du projet lié à cette commande',
    )
