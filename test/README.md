# Testes

Idiomas: **Português (Brasil)** | [English](README.en.md) | [Español](README.es.md) | [Français](README.fr.md)

## Objetivo

Garantir que o port Python preserva o contrato funcional do ecossistema AS-CNPJ.

## Execução

```bash
python -m unittest discover -s test -p "test_*.py"
```

## Cobertura

- exemplo oficial alfanumérico;
- caso legado numérico;
- DV inválido;
- normalização;
- modo estrito;
- tipos inválidos;
- vetores compartilhados do hub.
