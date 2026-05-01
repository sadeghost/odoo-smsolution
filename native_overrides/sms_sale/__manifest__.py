{
    'name': 'SMSolution - Sale Customization',
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'summary': 'Personnalisation du module Ventes pour SMSolution',
    'description': """
        Ce module hérite du module natif 'sale' pour ajouter des
        fonctionnalités spécifiques à SMSolution / IWA.
        
        Fonctionnalités :
        - Ajout du champ 'Référence Projet' sur le bon de commande
    """,
    'author': 'SMSolution',
    'website': 'https://smsolution.mr',
    'depends': ['sale'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
