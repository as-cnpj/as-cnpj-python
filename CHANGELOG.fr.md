# Changelog

Langues : [Português (Brasil)](CHANGELOG.md) | [English](CHANGELOG.en.md) | [Español](CHANGELOG.es.md) | **Français**

## 0.1.3

- ajoute `validate_many` et `validate_many_cnpj`
- préserve l'ordre d'entrée et renvoie `items` + `summary`
- expose des codes `reason` stables par élément
- met à jour le README et l'API pour la validation par lot

## 0.1.2

- met à jour le README pour refléter la publication sur PyPI
- convertit les liens du README en URLs absolues vers GitHub et l'écosystème
- ajoute un badge et un lien direct vers le package `as-cnpj`

## 0.1.1

- corrige le rendu de la bannière du README sur PyPI

## 0.1.0

- première version candidate publique du port Python
- validation du CNPJ numérique et alphanumérique
- normalisation, formatage et calcul des chiffres de contrôle
- tests automatisés contre les vecteurs partagés du hub
- durcissement contre les entrées Unicode hors ASCII imprimable
- workflow de release prêt pour la publication sur PyPI
