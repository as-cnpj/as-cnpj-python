# AS-CNPJ Python Reference

Languages: [Português (Brasil)](README.md) | **English** | [Español](README.es.md) | [Français](README.fr.md)

This folder is the working copy of the AS-CNPJ Python library inside the hub.

The planned public repository is:

- `https://github.com/as-cnpj/as-cnpj-python`

## Start here

- [Local API](docs/api.md)
- [Test strategy](test/README.md)
- [Release checklist](docs/release-checklist.md)
- [Security policy](SECURITY.md)
- [AS-CNPJ ecosystem hub](../../README.md)

## Role inside the hub

It exists to:

- consolidate the Python port from the ecosystem contract;
- prove compatibility against the shared vectors;
- serve as the base for the future `as-cnpj-python` repository.

## Mirrored public API

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

Planned CI for the derived repository:

- `Python 3.10`
- `Python 3.11`
- `Python 3.12`

## Publication

- planned PyPI package: `as-cnpj`
- import package: `as_cnpj`
- current status: local seed ready for future extraction
