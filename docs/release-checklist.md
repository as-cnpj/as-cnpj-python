# Release Checklist

Idiomas: **Português (Brasil)** | [English](release-checklist.en.md) | [Español](release-checklist.es.md) | [Français](release-checklist.fr.md)

- revisar README e changelog;
- validar `pyproject.toml`;
- validar workflow de CI e matriz de Python suportada;
- rodar `python -m unittest discover -s test -p "test_*.py"`;
- rodar `python -m build --sdist --wheel`;
- rodar `python -m twine check dist/*`;
- confirmar alinhamento com vetores compartilhados;
- publicar por GitHub Release com Trusted Publishing no PyPI.
