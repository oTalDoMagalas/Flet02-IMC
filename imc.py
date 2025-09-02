import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.padding = 30

    is_dark = False
    page.bgcolor = ft.Colors.WHITE

    peso = ft.TextField(label="Peso (kg)", prefix_icon=ft.Icons.FITNESS_CENTER_OUTLINED, width=400)
    altura = ft.TextField(label="Altura (m)", prefix_icon=ft.Icons.HEIGHT, width=400)
    resultado = ft.Text(size=18, weight="bold")

    def calcular_imc(e):
        try:
            p = float(peso.value)
            a = float(altura.value)
            imc = p / (a * a)
            if imc < 18.5:
                status = "Abaixo do peso"
            elif 18.5 <= imc < 24.9:
                status = "Peso normal"
            elif 25 <= imc < 29.9:
                status = "Sobrepeso"
            else:
                status = "Obesidade"
            resultado.value = f"IMC: {imc:.2f} ({status})"
        except:
            resultado.value = "Preencha os campos corretamente!"
        page.update()

    # limpar campos
    def limpar(e):
        peso.value = ""
        altura.value = ""
        resultado.value = ""
        page.update()

    # alternar tema
    def toggle_theme(e):
        nonlocal is_dark
        is_dark = not is_dark
        if is_dark:
            page.bgcolor = ft.Colors.BLACK
            toggle.icon = ft.Icons.WB_SUNNY_OUTLINED
            titulo.color = ft.Colors.WHITE
            subtitulo.color = ft.Colors.WHITE
            resultado.color = ft.Colors.WHITE
        else:
            page.bgcolor = ft.Colors.WHITE
            toggle.icon = ft.Icons.DARK_MODE_OUTLINED
            titulo.color = ft.Colors.BLACK
            subtitulo.color = ft.Colors.BLACK
            resultado.color = ft.Colors.BLACK
        page.update()

    # botão de tema
    toggle = ft.IconButton(
        icon=ft.Icons.DARK_MODE_OUTLINED,
        icon_size=30,
        on_click=toggle_theme,
        tooltip="Alternar tema"
    )

    titulo = ft.Text("🧮Calculadora de IMC", size=30, weight="bold", color=ft.Colors.BLACK)
    subtitulo = ft.Text("Informe seus dados", size=21, color=ft.Colors.BLACK)

    calcular_btn = ft.ElevatedButton("Calcular IMC", on_click=calcular_imc, bgcolor=ft.Colors.DEEP_PURPLE, color=ft.Colors.WHITE)
    limpar_btn = ft.ElevatedButton("Limpar", on_click=limpar, bgcolor=ft.Colors.RED, color=ft.Colors.WHITE)

    # layout
    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(),  # espaço vazio à esquerda
                        titulo,
                        toggle
                    ],
                    alignment="spaceBetween",
                    width=400  # largura da linha para centralizar o título
                ),
                subtitulo,
                peso,
                altura,
                # Botões centralizados com espaço uniforme
                ft.Row(
                    [calcular_btn, limpar_btn],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                ),
                resultado,
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=10
        )
    )

ft.app(target=main)
