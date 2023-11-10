import flet as ft
import pygame
import keyboard as kyb
#funciones del sistema
pygame.init()
contador_inicio= 0

def main(page: ft.Page):
    pygame.mixer.music.load("se_va_1_llegan_2_nicki_nicole.mp3")
    page.title="LMS PLAY"
    #CAMBIAR TEMA DE LA APP
    page.window_width=470
    page.window_height=720
    page.window_resizable=False
    page.update()
    page.theme_mode=ft.ThemeMode.LIGHT
    #CAMBIAR LA UBICACION
    page.vertical_alignment=ft.MainAxisAlignment.END
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    
    #Poner el cover de la musica, en este caso solo una img sencilla
    imagen = ft.Image(
        src="portada.jpg",
        width=400,
        height=400,
        fit=ft.ImageFit.CONTAIN,
    )

    page.add(imagen)
    
    def reproducir(t):
        global contador_inicio
        btn_play.content.selected_icon=ft.icons.PAUSE_ROUNDED
        selector = btn_play.content.selected = not btn_play.content.selected
        #print(selector) (si esta reproduciendo es true y si se pone pause es false)
        btn_play.content.update()

        if selector == False:
            pygame.mixer.music.pause()
        else:
            if contador_inicio == 0:
                pygame.mixer.music.play()
                contador_inicio= 1
            else:
                pygame.mixer.music.unpause()

    def parar(e):
        global contador_inicio
        pygame.mixer.music.stop()
        contador_inicio = 0
        #cambiar el icono de a reproducir si es que el boton esta en pausa
        btn_play.content.selected = False
        btn_play.update()
        page.snack_bar=ft.SnackBar(ft.Text("Se detuvo la canción"))
        page.snack_bar.open=True
        page.update()
    
    def fast_adelantar(e):
        #Investigar como adelantar la musica (la funcion de bloquear botones se desarrolla aparte)
        pass
        
    
    #AÑADIR LOS BOTONES
    #crear el contenedor de los botones
    fast_restroceso = ft.Container(
        content=ft.IconButton(icon=ft.icons.FAST_REWIND_ROUNDED, icon_size=40)
    )
    btn_play = ft.Container(
        content=ft.IconButton(icon=ft.icons.PLAY_ARROW_ROUNDED, icon_size=40,
        on_click=reproducir)
    )
    fast_avanzar = ft.Container(
        content=ft.IconButton(icon=ft.icons.FAST_FORWARD_ROUNDED, icon_size=40, on_click=fast_adelantar)
    )
    btn_stop = ft.Container(
        content=ft.IconButton(icon=ft.icons.STOP_ROUNDED, icon_size=40,selected_icon=ft.icons.STOP_ROUNDED,on_click=parar)
    )
    
    nav = ft.Container(
        ft.Row(
            [
                ft.Container(content=fast_restroceso),
                ft.Container(content=btn_play),
                ft.Container(content=fast_avanzar),
                ft.Container(content=btn_stop)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        padding=12,
        margin=50,
        border_radius=13,
        bgcolor=ft.colors.RED_100
    )
    page.add(nav)
    kyb.add_hotkey('ctrl+c', lambda: reproducir(None))
    kyb.add_hotkey('ctrl+x', lambda: parar(None))

ft.app(target=main)
