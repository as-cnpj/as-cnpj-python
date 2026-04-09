# Release Checklist

Languages: [Português (Brasil)](release-checklist.md) | **English** | [Español](release-checklist.es.md) | [Français](release-checklist.fr.md)

- review README and changelog;
- validate `pyproject.toml`;
- validate the CI workflow and the supported Python matrix;
- run `python -m unittest discover -s test -p "test_*.py"`;
- run `python -m build --sdist --wheel`;
- run `python -m twine check dist/*`;
- confirm alignment with shared vectors;
- publish through a GitHub Release with Trusted Publishing on PyPI.
