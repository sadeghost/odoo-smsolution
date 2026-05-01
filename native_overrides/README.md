# Native Overrides (Héritage de Modules Natifs)

Ce dossier contient les modules qui HÉRITENT des modules natifs Odoo pour les personnaliser.
On ne modifie JAMAIS le code source Odoo directement. À la place, on crée un module
d'héritage qui étend le comportement du module natif.

## Convention

Nommez le module `sms_<module_natif>` (ex: `sms_sale`, `sms_account`, `sms_crm`).
Utilisez `_inherit` dans les modèles Python et `inherit_id` dans les vues XML.

## Exemple de structure

```
sms_sale/
├── __manifest__.py      # depends: ['sale']
├── __init__.py
├── models/
│   ├── __init__.py
│   └── sale_order.py    # class SaleOrder(_inherit = 'sale.order')
└── views/
    └── sale_order_views.xml  # inherit_id="sale.view_order_form"
```
