# AS-CNPJ Python

Langues : [Português (Brasil)](README.md) | [English](README.en.md) | [Español](README.es.md) | **Français**

Bibliothèque AS-CNPJ pilotée par son auteur pour la validation, la normalisation, le formatage et le calcul des chiffres vérificateurs du CNPJ numérique et alphanumérique en Python.

Dépôt public :

- `https://github.com/as-cnpj/as-cnpj-python`

## Commencez ici

- [API locale](docs/api.md)
- [Stratégie de tests](test/README.md)
- [Checklist de release](docs/release-checklist.md)
- [Politique de sécurité](SECURITY.md)
- [Hub de l'écosystème AS-CNPJ](../../README.md)

## Statut

- dépôt public et maintenance active ;
- CI exécutée sur `Python 3.10` à `Python 3.14` ;
- API fonctionnelle couverte par des tests automatisés ;
- workflow de release prêt pour Trusted Publishing sur PyPI.

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

Matrice CI prise en charge :

- `Python 3.10`
- `Python 3.11`
- `Python 3.12`
- `Python 3.13`
- `Python 3.14`

## Publication

- package PyPI prévu : `as-cnpj`
- package d'import : `as_cnpj`
- état actuel : prêt pour la première publication publique sur PyPI
