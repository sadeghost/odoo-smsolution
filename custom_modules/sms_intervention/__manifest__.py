{
    'name': 'SMSolution - Gestion des Interventions',
    'version': '18.0.1.0.0',
    'category': 'Services',
    'summary': 'Gestion des interventions techniques',
    'description': """
        Module de gestion des interventions techniques pour IWA / SMSolution.

        Fonctionnalités :
        - Création et suivi des demandes d'intervention
        - Assignation des techniciens
        - Suivi du statut (brouillon, planifiée, en cours, terminée, annulée)
        - Historique des interventions par client
        - Séquence automatique (INT/0001, INT/0002, ...)
        - Chatter intégré (messages, activités)
    """,
    'author': 'SMSolution',
    'website': 'https://smsolution.mr',
    'depends': ['base', 'contacts', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/intervention_views.xml',
        'views/intervention_menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
