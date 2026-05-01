# Third Party Modules (Modules Tiers / Partenaires)

Ce dossier contient les modules téléchargés depuis l'Odoo Apps Store ou d'autres fournisseurs.
Ces modules sont versionnés ici pour garantir la synchronisation entre local, GitHub et VPS.

## Comment ajouter un module tiers

1. Téléchargez le module (ZIP) depuis apps.odoo.com
2. Décompressez-le dans ce dossier
3. Commit + push via le workflow Git habituel

## Important

Ne modifiez PAS directement ces modules. Si vous avez besoin de les personnaliser,
créez un module d'héritage dans `native_overrides/` ou `custom_modules/`.
