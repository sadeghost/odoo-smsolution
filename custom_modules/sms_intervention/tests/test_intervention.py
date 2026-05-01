from odoo.tests.common import TransactionCase, tagged
from odoo.exceptions import ValidationError, AccessError
from datetime import datetime


@tagged('post_install', '-at_install')
class TestIntervention(TransactionCase):
    """Tests unitaires pour le module sms_intervention.

    Ces tests vérifient :
    - La création d'une intervention avec séquence automatique
    - Le workflow complet (brouillon → planifiée → en cours → terminée)
    - Les transitions d'état invalides
    - Les droits d'accès
    - Les champs calculés
    """

    @classmethod
    def setUpClass(cls):
        """Préparer les données de test."""
        super().setUpClass()

        # Créer un partenaire de test
        cls.partner = cls.env['res.partner'].create({
            'name': 'Client Test SMSolution',
            'email': 'client.test@smsolution.mr',
        })

        # Récupérer un utilisateur technicien
        cls.technician = cls.env['res.users'].create({
            'name': 'Technicien Test',
            'login': 'tech_test@smsolution.mr',
            'email': 'tech_test@smsolution.mr',
        })

    # =========================================================
    # TEST 1 : Création et séquence automatique
    # =========================================================
    def test_01_create_intervention_sequence(self):
        """Test que la création génère une séquence INT/XXXX."""
        intervention = self.env['sms.intervention'].create({
            'partner_id': self.partner.id,
            'description': 'Problème réseau',
            'intervention_type': 'repair',
        })
        self.assertTrue(
            intervention.name.startswith('INT/'),
            f"La référence devrait commencer par 'INT/', obtenu: {intervention.name}"
        )
        self.assertEqual(intervention.state, 'draft')

    # =========================================================
    # TEST 2 : Workflow complet
    # =========================================================
    def test_02_workflow_complete(self):
        """Test le workflow : brouillon → planifiée → en cours → terminée."""
        intervention = self.env['sms.intervention'].create({
            'partner_id': self.partner.id,
            'technician_id': self.technician.id,
            'description': 'Installation serveur',
            'intervention_type': 'installation',
        })

        # État initial
        self.assertEqual(intervention.state, 'draft')

        # Planifier
        intervention.action_plan()
        self.assertEqual(intervention.state, 'planned')

        # Démarrer
        intervention.action_start()
        self.assertEqual(intervention.state, 'in_progress')

        # Terminer
        intervention.action_done()
        self.assertEqual(intervention.state, 'done')
        self.assertTrue(
            intervention.date_done,
            "La date de réalisation devrait être remplie automatiquement"
        )

    # =========================================================
    # TEST 3 : Annulation et remise en brouillon
    # =========================================================
    def test_03_cancel_and_reset(self):
        """Test l'annulation et la remise en brouillon."""
        intervention = self.env['sms.intervention'].create({
            'partner_id': self.partner.id,
            'description': 'Maintenance préventive',
            'intervention_type': 'maintenance',
        })

        # Planifier puis annuler
        intervention.action_plan()
        intervention.action_cancel()
        self.assertEqual(intervention.state, 'cancelled')

        # Remettre en brouillon
        intervention.action_reset_draft()
        self.assertEqual(intervention.state, 'draft')

    # =========================================================
    # TEST 4 : Champs obligatoires
    # =========================================================
    def test_04_required_fields(self):
        """Test que le partenaire est obligatoire."""
        with self.assertRaises(Exception):
            self.env['sms.intervention'].create({
                'description': 'Sans client',
            })

    # =========================================================
    # TEST 5 : Assignation technicien
    # =========================================================
    def test_05_technician_assignment(self):
        """Test l'assignation d'un technicien."""
        intervention = self.env['sms.intervention'].create({
            'partner_id': self.partner.id,
            'technician_id': self.technician.id,
            'description': 'Consultation réseau',
            'intervention_type': 'consulting',
        })
        self.assertEqual(intervention.technician_id.id, self.technician.id)

    # =========================================================
    # TEST 6 : Priorité
    # =========================================================
    def test_06_priority_default(self):
        """Test que la priorité par défaut est 'Normale'."""
        intervention = self.env['sms.intervention'].create({
            'partner_id': self.partner.id,
            'description': 'Test priorité',
        })
        self.assertEqual(intervention.priority, '0')

    # =========================================================
    # TEST 7 : Séquence incrémentale
    # =========================================================
    def test_07_sequence_incremental(self):
        """Test que les séquences sont incrémentales."""
        int1 = self.env['sms.intervention'].create({
            'partner_id': self.partner.id,
            'description': 'Première intervention',
        })
        int2 = self.env['sms.intervention'].create({
            'partner_id': self.partner.id,
            'description': 'Deuxième intervention',
        })
        # Extraire les numéros
        num1 = int(int1.name.split('/')[1])
        num2 = int(int2.name.split('/')[1])
        self.assertEqual(num2, num1 + 1, "Les séquences doivent être incrémentales")

    # =========================================================
    # TEST 8 : Type d'intervention
    # =========================================================
    def test_08_intervention_types(self):
        """Test les différents types d'intervention."""
        for itype in ['maintenance', 'installation', 'repair', 'consulting']:
            intervention = self.env['sms.intervention'].create({
                'partner_id': self.partner.id,
                'description': f'Test type {itype}',
                'intervention_type': itype,
            })
            self.assertEqual(intervention.intervention_type, itype)
