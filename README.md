<div align="center">
  <img src="https://raw.githubusercontent.com/as-cnpj/as-cnpj-python/main/assets/brand/as-cnpj-logo-dark.svg" alt="AS-CNPJ Python" width="860" />
</div>

<p align="center">
  Biblioteca autoral do ecossistema AS-CNPJ para validação, normalização, formatação e cálculo de dígitos verificadores de CNPJ numérico e alfanumérico em Python.
</p>

<p align="center">
  <a href="https://github.com/as-cnpj/as-cnpj-python">Repositório</a> ·
  <a href="https://pypi.org/project/as-cnpj/">PyPI</a> ·
  <a href="https://as-cnpj.org">Site</a> ·
  <a href="https://github.com/as-cnpj/as-cnpj">Hub do ecossistema</a> ·
  <a href="https://github.com/as-cnpj/as-cnpj-python/blob/main/docs/api.md">API</a> ·
  <a href="https://github.com/as-cnpj/as-cnpj-python/blob/main/test/README.md">Testes</a>
</p>

<p align="center">
  <a href="https://pypi.org/project/as-cnpj/"><img alt="PyPI as-cnpj" src="https://img.shields.io/pypi/v/as-cnpj?style=flat-square&label=pypi&labelColor=1C1917&color=F97316"></a>
  <a href="https://github.com/as-cnpj/as-cnpj-python/actions/workflows/ci.yml"><img alt="CI as-cnpj-python" src="https://img.shields.io/github/actions/workflow/status/as-cnpj/as-cnpj-python/ci.yml?branch=main&style=flat-square&label=ci&labelColor=1C1917"></a>
  <a href="https://github.com/as-cnpj/as-cnpj-python/actions/workflows/ci.yml"><img alt="Python 3.10 to 3.14" src="https://img.shields.io/badge/python-3.10%20%7C%203.14-F97316?style=flat-square&labelColor=1C1917"></a>
  <a href="https://github.com/as-cnpj/as-cnpj-python/blob/main/LICENSE"><img alt="License MIT" src="https://img.shields.io/github/license/as-cnpj/as-cnpj-python?style=flat-square&label=license&labelColor=1C1917&color=84A870"></a>
  <a href="https://as-cnpj.org"><img alt="Site as-cnpj.org" src="https://img.shields.io/badge/as--cnpj.org-documentação-FB923C?style=flat-square&labelColor=1C1917"></a>
</p>

Idiomas: **Português (Brasil)** | [English](https://github.com/as-cnpj/as-cnpj-python/blob/main/README.en.md) | [Español](https://github.com/as-cnpj/as-cnpj-python/blob/main/README.es.md) | [Français](https://github.com/as-cnpj/as-cnpj-python/blob/main/README.fr.md)

## Status

- repositório público e ativo;
- publicado no PyPI como [`as-cnpj`](https://pypi.org/project/as-cnpj/);
- CI rodando em `Python 3.10`, `Python 3.11`, `Python 3.12`, `Python 3.13` e `Python 3.14`;
- API funcional e coberta por testes automatizados;
- release workflow preparado para publicação no PyPI via Trusted Publishing;
- fluxo de publicação e pacote já ativos publicamente.

## Instalação

```bash
python -m pip install as-cnpj
```

Import público:

```python
from as_cnpj import is_valid_cnpj
```

## Exemplo rápido

```python
from as_cnpj import (
    assert_valid,
    calculate_cnpj_check_digits,
    format_cnpj,
    is_valid,
    normalize,
)

is_valid("12.ABC.345/01DE-35")
normalize("12.abc.345/01de-35")
format_cnpj("12ABC34501DE35")
assert_valid("12.ABC.345/01DE-35", strict=True)
calculate_cnpj_check_digits("12ABC34501DE")
```

## Casos de uso

- formulários de cadastro B2B com aceitação do formato legado e do formato alfanumérico;
- backends Python que precisam validar payloads antes de persistir ou integrar com ERP;
- rotinas de saneamento e migração de base com normalização consistente;
- suites de teste e homologação que precisam gerar e validar exemplos de CNPJ.

## O que esta biblioteca entrega

- validação de CNPJ numérico legado;
- validação de CNPJ alfanumérico previsto pela Receita Federal para julho de 2026;
- suporte a entradas com máscara e sem máscara;
- modo permissivo e modo estrito;
- zero dependências de runtime para o núcleo do algoritmo;
- consistência com vetores compartilhados do hub.

## API pública

Funções principais:

- `normalize(value)`
- `is_valid(value, strict=False)`
- `format(value, strict=False)`
- `assert_valid(value, strict=False)`
- `calculate_check_digits(base12)`
- `validate_many(values, strict=False)`

Aliases explícitos:

- `normalize_cnpj(value)`
- `is_valid_cnpj(value, strict=False)`
- `format_cnpj(value, strict=False)`
- `assert_valid_cnpj(value, strict=False)`
- `calculate_cnpj_check_digits(base12)`
- `validate_many_cnpj(values, strict=False)`

## Validação em lote

Além da API unitária, a biblioteca também expõe:

- `validate_many(values, strict=False)`
- `validate_many_cnpj(values, strict=False)`

O retorno preserva a ordem de entrada e entrega:

- `items`: resultado item a item com `index`, `input`, `normalized`, `formatted`, `valid`, `strict_valid` e `reason`;
- `summary`: total, válidos, inválidos e contagem agregada por motivo.

```python
from as_cnpj import validate_many

result = validate_many([
    "12.ABC.345/01DE-35",
    "12.ABC.345/01DE-36",
    None,
])

result["items"][0]["valid"]
result["items"][1]["reason"]
result["summary"]["reasons"]
```

## Garantias centrais

- aceita `A-Z0-9` nos 12 primeiros caracteres;
- mantém os 2 dígitos verificadores como numéricos;
- usa módulo 11 com conversão `ASCII - 48`;
- normaliza entrada para caixa alta;
- rejeita repetições triviais inválidas;
- mantém o contrato alinhado aos vetores compartilhados do ecossistema.

## Documentação e referências

- [API da biblioteca](https://github.com/as-cnpj/as-cnpj-python/blob/main/docs/api.md)
- [Estratégia de testes](https://github.com/as-cnpj/as-cnpj-python/blob/main/test/README.md)
- [Checklist de release](https://github.com/as-cnpj/as-cnpj-python/blob/main/docs/release-checklist.md)
- [Política de segurança](https://github.com/as-cnpj/as-cnpj-python/blob/main/SECURITY.md)
- [Hub do ecossistema AS-CNPJ](https://github.com/as-cnpj/as-cnpj)

## Publicação

- pacote publicado no PyPI: `as-cnpj`
- import público: `as_cnpj`
- release via GitHub Releases com Trusted Publishing para o PyPI

## Vetores compartilhados

O `as-cnpj-python` não define a verdade sozinho.

O contrato do ecossistema depende também de:

- vetores compartilhados no hub;
- regras documentadas a partir das fontes oficiais;
- convergência entre implementações em linguagens diferentes.

## Manutenção

Maintainer: `@0moura`  
Contato institucional: `ascnpj@0moura.io`
