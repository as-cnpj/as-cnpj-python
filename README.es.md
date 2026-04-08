# AS-CNPJ Python Reference

Idiomas: [Português (Brasil)](README.md) | [English](README.en.md) | **Español** | [Français](README.fr.md)

Esta carpeta es la copia de trabajo de la biblioteca Python del ecosistema AS-CNPJ dentro del hub.

El repositorio público planificado es:

- `https://github.com/as-cnpj/as-cnpj-python`

## Empieza por aquí

- [API local](docs/api.md)
- [Estrategia de pruebas](test/README.md)
- [Checklist de release](docs/release-checklist.md)
- [Política de seguridad](SECURITY.md)
- [Hub del ecosistema AS-CNPJ](../../README.md)

## Papel dentro del hub

Existe para:

- consolidar el port Python a partir del contrato del ecosistema;
- probar compatibilidad con los vectores compartidos;
- servir como base para la futura apertura del repositorio `as-cnpj-python`.

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

CI planificada para el repositorio derivado:

- `Python 3.10`
- `Python 3.11`
- `Python 3.12`

## Publicación

- paquete planificado en PyPI: `as-cnpj`
- paquete de importación: `as_cnpj`
- estado actual: semilla local lista para una futura extracción
