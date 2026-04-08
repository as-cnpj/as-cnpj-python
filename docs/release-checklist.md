# Release Checklist

Idiomas: **Português (Brasil)** | [English](release-checklist.en.md) | [Español](release-checklist.es.md) | [Français](release-checklist.fr.md)

- revisar README e changelog;
- validar `pyproject.toml`;
- validar workflow de CI e matriz de Python suportada;
- rodar `python -m unittest discover -s test -p "test_*.py"`;
- confirmar alinhamento com vetores compartilhados;
- publicar somente quando o repo derivado existir e estiver pronto para uso público.
