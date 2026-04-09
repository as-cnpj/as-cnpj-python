# Checklist de Release

Idiomas: [Português (Brasil)](release-checklist.md) | [English](release-checklist.en.md) | **Español** | [Français](release-checklist.fr.md)

- revisar README y changelog;
- validar `pyproject.toml`;
- validar el workflow de CI y la matriz de Python soportada;
- ejecutar `python -m unittest discover -s test -p "test_*.py"`;
- ejecutar `python -m build --sdist --wheel`;
- ejecutar `python -m twine check dist/*`;
- confirmar alineación con los vectores compartidos;
- publicar mediante GitHub Release con Trusted Publishing en PyPI.
