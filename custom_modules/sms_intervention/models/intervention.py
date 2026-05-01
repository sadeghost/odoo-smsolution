from odoo import models, fields, api


class Intervention(models.Model):
    """Modèle principal pour la gestion des interventions techniques.

    Ce modèle permet de créer, planifier, suivre et clôturer des
    interventions techniques assignées à des techniciens pour des clients.
    """
    _name = 'sms.intervention'
    _description = 'Intervention Technique'
    _order = 'date_planned desc, id desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Référence',
        required=True,
        copy=False,
        readonly=True,
        default='Nouveau',
    )
    partner_id = fields.Many2one(
        'res.partner',
        string='Client',
        required=True,
        tracking=True,
    )
    technician_id = fields.Many2one(
        'res.users',
        string='Technicien',
        tracking=True,
    )
    date_planned = fields.Datetime(
        string='Date Prévue',
        tracking=True,
    )
    date_done = fields.Datetime(
        string='Date Réalisée',
    )
    description = fields.Text(
        string='Description du Problème',
    )
    resolution = fields.Text(
        string='Résolution',
    )
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('planned', 'Planifiée'),
        ('in_progress', 'En Cours'),
        ('done', 'Terminée'),
        ('cancelled', 'Annulée'),
    ], string='Statut', default='draft', tracking=True)
    priority = fields.Selection([
        ('0', 'Normale'),
        ('1', 'Urgente'),
        ('2', 'Critique'),
    ], string='Priorité', default='0')
    duration = fields.Float(
        string='Durée (heures)',
    )
    intervention_type = fields.Selection([
        ('maintenance', 'Maintenance'),
        ('installation', 'Installation'),
        ('repair', 'Réparation'),
        ('consulting', 'Consultation'),
        ('other', 'Autre'),
    ], string='Type', default='maintenance')
    notes = fields.Html(
        string='Notes Internes',
    )

    @api.model_create_multi
    def create(self, vals_list):
        """Génère automatiquement la séquence INT/0001, INT/0002, etc."""
        for vals in vals_list:
            if vals.get('name', 'Nouveau') == 'Nouveau':
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'sms.intervention'
                ) or 'Nouveau'
        return super().create(vals_list)

    def action_plan(self):
        """Passer l'intervention en statut 'Planifiée'."""
        self.write({'state': 'planned'})

    def action_start(self):
        """Démarrer l'intervention."""
        self.write({'state': 'in_progress'})

    def action_done(self):
        """Terminer l'intervention et enregistrer la date de réalisation."""
        self.write({
            'state': 'done',
            'date_done': fields.Datetime.now(),
        })

    def action_cancel(self):
        """Annuler l'intervention."""
        self.write({'state': 'cancelled'})

    def action_reset_draft(self):
        """Remettre l'intervention en brouillon."""
        self.write({'state': 'draft'})
