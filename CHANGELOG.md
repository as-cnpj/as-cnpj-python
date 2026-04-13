# Changelog

Idiomas: **Português (Brasil)** | [English](CHANGELOG.en.md) | [Español](CHANGELOG.es.md) | [Français](CHANGELOG.fr.md)

## 0.1.3

- adiciona `validate_many` e `validate_many_cnpj`
- preserva a ordem de entrada e retorna `items` + `summary`
- expõe `reason` estável por item
- atualiza README e API para a validação em lote

## 0.1.2

- atualização do README para refletir a publicação no PyPI
- conversão dos links do README para URLs absolutas do GitHub e do ecossistema
- adição de badge e link diretos para o pacote `as-cnpj`

## 0.1.1

- correção do banner do README para renderização correta no PyPI

## 0.1.0

- primeira release pública candidata do port Python
- validação de CNPJ numérico e alfanumérico
- normalização, formatação e cálculo de dígitos verificadores
- testes automatizados contra os vetores compartilhados do hub
- endurecimento contra Unicode fora de ASCII imprimível
- workflow de release preparado para publicação no PyPI
