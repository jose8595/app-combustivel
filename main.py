import flet as ft

LIMITE = 0.7


def converter(texto):
    return float(texto.replace(",", "."))


def calcular_razao(gasolina, etanol):
    return etanol / gasolina


def preco_maximo_etanol(gasolina):
    return gasolina * LIMITE


def formatar_preco(valor):
    return f"R$ {valor:.2f}".replace(".", ",")


def recomendar(razao):
    if razao <= LIMITE:
        return "Abasteça com etanol"
    else:
        return "Abasteça com gasolina"


def main(page: ft.Page):
    page.title = "Gasolina ou Etanol"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN)
    page.dark_theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN)
    page.padding = 16
    page.scroll = ft.ScrollMode.AUTO

    # ---------- Cabeçalho ----------
    cabecalho = ft.Row(
        [
            ft.Icon(ft.Icons.LOCAL_GAS_STATION, size=36, color=ft.Colors.GREEN),
            ft.Column(
                [
                    ft.Text("Gasolina ou Etanol?", size=24, weight=ft.FontWeight.BOLD),
                    ft.Text("Descubra qual compensa mais", size=13, opacity=0.7),
                ],
                spacing=0,
            ),
        ],
        spacing=12,
    )

    # ---------- Campos ----------
    campo_gasolina = ft.TextField(
        label="Preço da gasolina",
        prefix="R$ ",
        keyboard_type=ft.KeyboardType.NUMBER,
        border_radius=12,
        filled=True,
    )
    campo_etanol = ft.TextField(
        label="Preço do etanol",
        prefix="R$ ",
        keyboard_type=ft.KeyboardType.NUMBER,
        border_radius=12,
        filled=True,
    )

    # ---------- Cartão de resultado ----------
    icone_resultado = ft.Icon(ft.Icons.ECO, size=32)
    titulo_resultado = ft.Text(size=20, weight=ft.FontWeight.BOLD)
    detalhe = ft.Text(size=14)

    cartao_resultado = ft.Container(
        visible=False,
        padding=16,
        border_radius=16,
        content=ft.Row(
            [
                icone_resultado,
                ft.Column([titulo_resultado, detalhe], spacing=4, expand=True),
            ],
            vertical_alignment=ft.CrossAxisAlignment.START,
            spacing=12,
        ),
    )

    def mostrar(cor, icone, titulo, texto):
        cartao_resultado.bgcolor = ft.Colors.with_opacity(0.15, cor)
        icone_resultado.icon = icone
        icone_resultado.color = cor
        titulo_resultado.value = titulo
        detalhe.value = texto
        cartao_resultado.visible = True

    def calcular(e):
        try:
            gasolina = converter(campo_gasolina.value)
            etanol = converter(campo_etanol.value)

            if gasolina <= 0 or etanol <= 0:
                mostrar(
                    ft.Colors.RED,
                    ft.Icons.ERROR_OUTLINE,
                    "Preço inválido",
                    "Os preços precisam ser maiores que zero.",
                )
            else:
                razao = calcular_razao(gasolina, etanol)
                maximo = formatar_preco(preco_maximo_etanol(gasolina))
                texto = (
                    f"O etanol custa {razao:.0%} do preço da gasolina.\n"
                    f"Com a gasolina a {formatar_preco(gasolina)}, "
                    f"o etanol compensa até {maximo}."
                )
                if razao <= LIMITE:
                    mostrar(ft.Colors.GREEN, ft.Icons.ECO, recomendar(razao), texto)
                else:
                    mostrar(
                        ft.Colors.ORANGE,
                        ft.Icons.LOCAL_GAS_STATION,
                        recomendar(razao),
                        texto,
                    )
        except ValueError:
            mostrar(
                ft.Colors.RED,
                ft.Icons.ERROR_OUTLINE,
                "Valor inválido",
                "Digite apenas números, por exemplo 5,89.",
            )

        page.update()

    def limpar(e):
        campo_gasolina.value = ""
        campo_etanol.value = ""
        cartao_resultado.visible = False
        page.update()

    campo_etanol.on_submit = calcular

    botoes = ft.Row(
        [
            ft.Button(
                "Calcular",
                icon=ft.Icons.CALCULATE,
                on_click=calcular,
                expand=True,
                height=48,
            ),
            ft.OutlinedButton("Limpar", on_click=limpar, height=48),
        ],
        spacing=12,
    )

    rodape = ft.Text(
        "Regra dos 70%: o etanol compensa quando custa até 70% do preço da gasolina.",
        size=12,
        opacity=0.6,
    )

    # ---------- Responsivo ----------
    conteudo = ft.Column(
        [cabecalho, campo_gasolina, campo_etanol, botoes, cartao_resultado, rodape],
        spacing=16,
        col={"xs": 12, "sm": 10, "md": 6, "lg": 4},
    )

    page.add(
        ft.SafeArea(
            content=ft.ResponsiveRow(
                [conteudo],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )
    )


ft.run(main)