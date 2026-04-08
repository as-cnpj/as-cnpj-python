# Release Checklist

Languages: [Português (Brasil)](release-checklist.md) | **English** | [Español](release-checklist.es.md) | [Français](release-checklist.fr.md)

- review README and changelog;
- validate `pyproject.toml`;
- validate the CI workflow and the supported Python matrix;
- run `python -m unittest discover -s test -p "test_*.py"`;
- confirm alignment with shared vectors;
- publish only when the derived repository exists and is ready for public use.
