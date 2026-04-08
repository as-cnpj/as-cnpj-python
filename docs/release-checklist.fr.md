# Checklist de Release

Langues : [Português (Brasil)](release-checklist.md) | [English](release-checklist.en.md) | [Español](release-checklist.es.md) | **Français**

- relire le README et le changelog ;
- valider `pyproject.toml` ;
- valider le workflow de CI et la matrice Python supportée ;
- exécuter `python -m unittest discover -s test -p "test_*.py"` ;
- confirmer l'alignement avec les vecteurs partagés ;
- publier seulement quand le dépôt dérivé existera et sera prêt pour l'usage public.
