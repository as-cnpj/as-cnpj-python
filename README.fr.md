# AS-CNPJ Python Reference

Langues : [Português (Brasil)](README.md) | [English](README.en.md) | [Español](README.es.md) | **Français**

Ce dossier est la copie de travail de la bibliothèque Python de l'écosystème AS-CNPJ dans le hub.

Le dépôt public prévu est :

- `https://github.com/as-cnpj/as-cnpj-python`

## Commencez ici

- [API locale](docs/api.md)
- [Stratégie de tests](test/README.md)
- [Checklist de release](docs/release-checklist.md)
- [Politique de sécurité](SECURITY.md)
- [Hub de l'écosystème AS-CNPJ](../../README.md)

## Rôle dans le hub

Il existe pour :

- consolider le port Python à partir du contrat de l'écosystème ;
- prouver la compatibilité avec les vecteurs partagés ;
- servir de base à la future ouverture du dépôt `as-cnpj-python`.

## API publique miroir

- `normalize(value)`
- `is_valid(value, strict=False)`
- `format(value, strict=False)`
- `assert_valid(value, strict=False)`
- `calculate_check_digits(base12)`
- `normalize_cnpj(value)`
- `is_valid_cnpj(value, strict=False)`
- `format_cnpj(value, strict=False)`
- `assert_valid_cnpj(value, strict=False)`
- `calculate_cnpj_check_digits(base12)`

## Tests

```bash
python -m unittest discover -s test -p "test_*.py"
```

CI prévue pour le dépôt dérivé :

- `Python 3.10`
- `Python 3.11`
- `Python 3.12`

## Publication

- package PyPI prévu : `as-cnpj`
- package d'import : `as_cnpj`
- état actuel : graine locale prête pour une future extraction
