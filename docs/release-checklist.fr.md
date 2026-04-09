# Checklist de Release

Langues : [Português (Brasil)](release-checklist.md) | [English](release-checklist.en.md) | [Español](release-checklist.es.md) | **Français**

- relire le README et le changelog ;
- valider `pyproject.toml` ;
- valider le workflow de CI et la matrice Python supportée ;
- exécuter `python -m unittest discover -s test -p "test_*.py"` ;
- exécuter `python -m build --sdist --wheel` ;
- exécuter `python -m twine check dist/*` ;
- confirmer l'alignement avec les vecteurs partagés ;
- publier via une GitHub Release avec Trusted Publishing sur PyPI.
