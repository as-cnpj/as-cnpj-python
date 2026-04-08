# AS-CNPJ Python

Idiomas: **Português (Brasil)** | [English](README.en.md) | [Español](README.es.md) | [Français](README.fr.md)

[![CI](https://github.com/as-cnpj/as-cnpj-python/actions/workflows/ci.yml/badge.svg)](https://github.com/as-cnpj/as-cnpj-python/actions/workflows/ci.yml)

Biblioteca autoral para validação de CNPJ numérico e alfanumérico em Python.

Repositório: `https://github.com/as-cnpj/as-cnpj-python`

## Status

- repositório público e ativo;
- CI rodando em `Python 3.10`, `Python 3.11`, `Python 3.12`, `Python 3.13` e `Python 3.14`;
- API inicial já funcional e coberta por testes automatizados;
- publicação no PyPI ainda não realizada;
- algoritmo validado com vetores compartilhados do ecossistema.

## Instalação

Enquanto a publicação no PyPI não acontece, a forma mais direta de avaliação é instalar a partir do GitHub:

```bash
python -m pip install git+https://github.com/as-cnpj/as-cnpj-python.git
```

Import package:

```python
from as_cnpj import is_valid_cnpj
```

## Comece por aqui

- [API da biblioteca](docs/api.md)
- [Estratégia de testes](test/README.md)
- [Checklist de release](docs/release-checklist.md)
- [Política de segurança](SECURITY.md)
- [Hub do ecossistema AS-CNPJ](https://github.com/as-cnpj/as-cnpj)

## O que esta biblioteca resolve

Esta biblioteca existe para cobrir, com uma única API Python, a coexistência entre:

- CNPJ legado numérico;
- CNPJ alfanumérico previsto pela Receita Federal para julho de 2026;
- entradas com máscara e sem máscara;
- fluxos permissivos e fluxos com validação estrita.

Ela implementa:

- validação;
- normalização;
- formatação;
- cálculo de dígitos verificadores;
- consistência com vetores compartilhados do ecossistema.

## Exemplos rápidos

Validação e normalização:

```python
from as_cnpj import is_valid, normalize

is_valid("12.ABC.345/01DE-35")
normalize("12.abc.345/01de-35")
```

Formatação para exibição:

```python
from as_cnpj import format_cnpj

format_cnpj("12ABC34501DE35")
```

Borda estrita de API:

```python
from as_cnpj import is_valid_cnpj

is_valid_cnpj("12.ABC.345/01DE-35", strict=True)
```

Geração de fixtures e testes:

```python
from as_cnpj import calculate_cnpj_check_digits

calculate_cnpj_check_digits("12ABC34501DE")
```

## Casos de uso

- formulários de cadastro B2B com aceitação do formato legado e do formato alfanumérico;
- backends Python que precisam validar payloads antes de persistir ou integrar com ERP;
- rotinas de saneamento e migração de base com normalização consistente;
- suites de teste e homologação que precisam gerar e validar exemplos de CNPJ.

## Garantias centrais

- aceita `A-Z0-9` nos 12 primeiros caracteres;
- mantém os 2 dígitos verificadores como numéricos;
- usa módulo 11 com conversão `ASCII - 48`;
- normaliza entrada para caixa alta;
- rejeita repetições triviais inválidas;
- suporta modo permissivo e modo estrito;
- não depende de bibliotecas de runtime para o núcleo do algoritmo.

## API pública

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

Execução direta:

```bash
python -m unittest discover -s test -p "test_*.py"
```

O conjunto cobre:

- casos positivos numéricos;
- casos positivos alfanuméricos;
- casos negativos;
- modo estrito;
- consistência entre aliases;
- vetores compartilhados do hub.

## Vetores compartilhados

O `as-cnpj-python` não define a verdade sozinho.

O contrato do ecossistema também depende de:

- vetores compartilhados no hub;
- regras documentadas a partir das fontes oficiais;
- convergência entre implementações em linguagens diferentes.

## Ecossistema

Org GitHub:

- `https://github.com/as-cnpj`

Hub do projeto:

- manifesto;
- documentação consolidada;
- vetores compartilhados;
- governança entre linguagens.

## Manutenção

Maintainer:

- `@0moura`

Contato institucional:

- `ascnpj@0moura.io`
