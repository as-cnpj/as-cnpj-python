# AS-CNPJ Python

Languages: [Português (Brasil)](README.md) | **English** | [Español](README.es.md) | [Français](README.fr.md)

Author-led AS-CNPJ library for numeric and alphanumeric CNPJ validation, normalization, formatting, and check digit calculation in Python.

Public repository:

- `https://github.com/as-cnpj/as-cnpj-python`

## Start here

- [Local API](docs/api.md)
- [Test strategy](test/README.md)
- [Release checklist](docs/release-checklist.md)
- [Security policy](SECURITY.md)
- [AS-CNPJ ecosystem hub](../../README.md)

## Status

- public repository and active maintenance;
- CI running on `Python 3.10` through `Python 3.14`;
- functional API covered by automated tests;
- release workflow prepared for Trusted Publishing on PyPI.

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

Supported CI matrix:

- `Python 3.10`
- `Python 3.11`
- `Python 3.12`
- `Python 3.13`
- `Python 3.14`

## Publication

- planned PyPI package: `as-cnpj`
- import package: `as_cnpj`
- current status: ready for the first public PyPI release
