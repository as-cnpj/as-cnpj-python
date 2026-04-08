# Checklist de Release

Idiomas: [Português (Brasil)](release-checklist.md) | [English](release-checklist.en.md) | **Español** | [Français](release-checklist.fr.md)

- revisar README y changelog;
- validar `pyproject.toml`;
- validar el workflow de CI y la matriz de Python soportada;
- ejecutar `python -m unittest discover -s test -p "test_*.py"`;
- confirmar alineación con los vectores compartidos;
- publicar solo cuando el repositorio derivado exista y esté listo para uso público.
