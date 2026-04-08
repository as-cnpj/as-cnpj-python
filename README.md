# AS-CNPJ Python Reference

Idiomas: **Português (Brasil)** | [English](README.en.md) | [Español](README.es.md) | [Français](README.fr.md)

Esta pasta é a cópia de trabalho da biblioteca Python do ecossistema AS-CNPJ dentro do hub.

O repositório público planejado da biblioteca é:

- `https://github.com/as-cnpj/as-cnpj-python`

## Comece por aqui

- [API local](docs/api.md)
- [Estratégia de testes](test/README.md)
- [Checklist de release](docs/release-checklist.md)
- [Política de segurança](SECURITY.md)
- [Hub do ecossistema AS-CNPJ](../../README.md)

## Papel desta pasta dentro do hub

Ela existe para:

- consolidar o port Python a partir do contrato do ecossistema;
- provar compatibilidade com os vetores compartilhados;
- servir de base para a abertura futura do repositório `as-cnpj-python`.

## API pública espelhada

Funções principais:

- `normalize(value)`
- `is_valid(value, strict=False)`
- `format(value, strict=False)`
- `assert_valid(value, strict=False)`
- `calculate_check_digits(base12)`

Aliases explícitos:

- `normalize_cnpj(value)`
- `is_valid_cnpj(value, strict=False)`
- `format_cnpj(value, strict=False)`
- `assert_valid_cnpj(value, strict=False)`
- `calculate_cnpj_check_digits(base12)`

## Testes

```bash
python -m unittest discover -s test -p "test_*.py"
```

CI planejada para o repo derivado:

- `Python 3.10`
- `Python 3.11`
- `Python 3.12`

## Publicação

- pacote planejado no PyPI: `as-cnpj`
- import package: `as_cnpj`
- status atual: semente local pronta para extração futura
