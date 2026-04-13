# API

Idiomas: **Português (Brasil)** | [English](api.en.md) | [Español](api.es.md) | [Français](api.fr.md)

## Funções principais

- `normalize(value)`
- `is_valid(value, strict=False)`
- `format(value, strict=False)`
- `assert_valid(value, strict=False)`
- `calculate_check_digits(base12)`
- `validate_many(values, strict=False)`

## Aliases explícitos

- `normalize_cnpj(value)`
- `is_valid_cnpj(value, strict=False)`
- `format_cnpj(value, strict=False)`
- `assert_valid_cnpj(value, strict=False)`
- `calculate_cnpj_check_digits(base12)`
- `validate_many_cnpj(values, strict=False)`

## Regras gerais

- `normalize` não valida o CNPJ;
- `is_valid` retorna `True` ou `False`;
- `format` retorna `str` mascarada quando válida, e `None` quando inválida;
- `assert_valid` retorna a forma normalizada quando válida;
- `calculate_check_digits` recebe 12 caracteres-base e retorna 2 dígitos.

## `validate_many(values, strict=False)`

Recebe uma lista e retorna:

- `items`: resultado por item, preservando a ordem de entrada;
- `summary`: total, válidos, inválidos e contagem por motivo.

Lança `TypeError` se a entrada não for uma lista.

Cada item retorna:

- `index`
- `input`
- `normalized`
- `formatted`
- `valid`
- `strict_valid`
- `reason`

Motivos possíveis:

- `VALID`
- `INVALID_TYPE`
- `INVALID_ASCII`
- `INVALID_LENGTH`
- `INVALID_STRICT_FORMAT`
- `INVALID_BASE`
- `TRIVIAL_REPETITION`
- `INVALID_CHECK_DIGIT`
