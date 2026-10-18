# Gasolina ou Etanol?

App Android que ajuda a decidir qual combustível compensa mais na hora de abastecer, usando a **regra dos 70%**.

## Como funciona

O etanol compensa quando custa **até 70% do preço da gasolina**.

Exemplo: com a gasolina a R$ 6,79 e o etanol a R$ 4,59, o etanol custa 68% do preço da gasolina, então ele compensa.

O app mostra:

- a recomendação (etanol ou gasolina);
- a porcentagem que o etanol representa;
- o preço máximo do etanol para ele ainda compensar.

## Recursos

- Aceita vírgula ou ponto nos preços (`5,89` ou `5.89`)
- Avisa quando o valor é inválido (vazio, letra, zero ou negativo)
- Teclado numérico no celular
- Visual responsivo, com tema claro e escuro

## Tecnologias

- Python 3.13
- [Flet](https://flet.dev) (interface do app)
- [uv](https://docs.astral.sh/uv/) (gerenciador de ambiente e pacotes)

## Como rodar no computador

Com o `uv` instalado, na pasta do projeto:

```
uv sync
uv run flet run main.py
```

## Como gerar o APK

```
uv run flet build apk --python-version 3.13 --arch arm64-v8a
```

O APK também pode ser baixado na página de
[Releases](https://github.com/jose8595/app-combustivel/releases).

## Sobre

Projeto feito durante meus estudos de Python.

Autor: José Renildes