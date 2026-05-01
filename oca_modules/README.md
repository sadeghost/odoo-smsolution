# OCA Modules (Odoo Community Association)

Ce dossier contient les modules de la communauté OCA (https://github.com/OCA).
Ils sont copiés ici (et non en submodule) pour garantir un contrôle total sur les versions.

## Comment ajouter un module OCA

1. Identifiez le module sur https://github.com/OCA
2. Clonez le dépôt OCA correspondant (branche 18.0)
3. Copiez UNIQUEMENT le module souhaité dans ce dossier
4. Commit + push via le workflow Git habituel

## Exemple

```bash
git clone -b 18.0 https://github.com/OCA/web.git /tmp/oca-web
cp -r /tmp/oca-web/web_responsive ./oca_modules/
```
