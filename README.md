# Odoo 18 - SMSolution / IWA

Dépôt central des modules Odoo personnalisés pour SMSolution / Istithmar West Africa.
Ce dépôt suit la stratégie de branches Odoo.sh (dev/staging/production) avec déploiement automatique sur le VPS.

## Structure du Dépôt

```
odoo-smsolution/
├── custom_modules/         # Modules développés en interne
│   └── custom_partner/     # Champs personnalisés sur res.partner
├── third_party_modules/    # Modules téléchargés (Odoo Apps Store)
├── oca_modules/            # Modules OCA (Odoo Community Association)
├── native_overrides/       # Héritage de modules natifs Odoo
│   └── sms_sale/           # Exemple : personnalisation du module Ventes
└── README.md
```

## Branches

| Branche | Rôle | Déploiement |
|---|---|---|
| `dev` | Développement | Local uniquement |
| `staging` | Pré-production / Tests | Manuel |
| `production` | Production | Automatique (webhook) |

## Workflow

1. Cloner le dépôt : `git clone https://github.com/sadeghost/odoo-smsolution.git`
2. Travailler sur `dev` : `git checkout dev`
3. Développer et tester localement
4. Push : `git push origin dev`
5. Merger vers `staging` puis `production`
6. Le VPS se met à jour automatiquement

## Serveur de Production

- URL : http://54.37.229.176:8069
- Déploiement automatique via webhook GitHub (port 9090)
