# Contribuição

Idiomas: **Português (Brasil)** | [English](CONTRIBUTING.en.md) | [Español](CONTRIBUTING.es.md) | [Français](CONTRIBUTING.fr.md)

## Regra geral

Esta semente segue a governança do hub `as-cnpj`.

Antes de abrir contribuição:

- alinhe a mudança com os vetores compartilhados;
- não copie código de terceiros;
- preserve a equivalência funcional com o ecossistema;
- mantenha a API pequena e auditável.

## Escopo aceito

- correções de bug;
- melhoria de testes;
- ajustes de documentação;
- melhorias de portabilidade Python.

## Antes de propor mudança

Rode:

```bash
python -m unittest discover -s test -p "test_*.py"
```
