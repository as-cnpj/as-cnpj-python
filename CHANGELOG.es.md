# Changelog

Idiomas: [Português (Brasil)](CHANGELOG.md) | [English](CHANGELOG.en.md) | **Español** | [Français](CHANGELOG.fr.md)

## 0.1.3

- añade `validate_many` y `validate_many_cnpj`
- preserva el orden de entrada y devuelve `items` + `summary`
- expone códigos `reason` estables por ítem
- actualiza README y API para la validación por lotes

## 0.1.2

- actualiza el README para reflejar la publicación en PyPI
- convierte los enlaces del README a URLs absolutas de GitHub y del ecosistema
- añade badge y enlace directo al paquete `as-cnpj`

## 0.1.1

- corrige la renderización del banner del README en PyPI

## 0.1.0

- primera versión candidata pública del port Python
- validación de CNPJ numérico y alfanumérico
- normalización, formateo y cálculo de dígitos verificadores
- pruebas automatizadas contra los vectores compartidos del hub
- endurecimiento contra Unicode fuera de ASCII imprimible
- workflow de release preparado para publicación en PyPI
