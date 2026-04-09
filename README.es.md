# AS-CNPJ Python

Idiomas: [Português (Brasil)](README.md) | [English](README.en.md) | **Español** | [Français](README.fr.md)

Biblioteca autoral AS-CNPJ para validación, normalización, formateo y cálculo de dígitos verificadores de CNPJ numérico y alfanumérico en Python.

Repositorio público:

- `https://github.com/as-cnpj/as-cnpj-python`

## Empieza por aquí

- [API local](docs/api.md)
- [Estrategia de pruebas](test/README.md)
- [Checklist de release](docs/release-checklist.md)
- [Política de seguridad](SECURITY.md)
- [Hub del ecosistema AS-CNPJ](../../README.md)

## Estado

- repositorio público y mantenimiento activo;
- CI ejecutándose en `Python 3.10` a `Python 3.14`;
- API funcional cubierta por pruebas automatizadas;
- workflow de release preparado para Trusted Publishing en PyPI.

## API pública espejada

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

## Pruebas

```bash
python -m unittest discover -s test -p "test_*.py"
```

Matriz de CI soportada:

- `Python 3.10`
- `Python 3.11`
- `Python 3.12`
- `Python 3.13`
- `Python 3.14`

## Publicación

- paquete planificado en PyPI: `as-cnpj`
- paquete de importación: `as_cnpj`
- estado actual: listo para la primera publicación pública en PyPI
