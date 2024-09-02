from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import os

from info import *  # Se importan los diccionarios

# Pantalla del menú principal
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Cambiar el color de fondo de la ventana a un azul suave
        Window.clearcolor = (0.9, 0.95, 1, 1)  # Azul suave
        
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Encabezado
        header = Label(
            text="Bienvenido a la App de Salud",
            font_size=32,
            color=(0, 0.5, 0, 1),  # Verde oscuro
            size_hint=(1, 0.2),
            bold=True
        )
        layout.add_widget(header)
        
        # Imagen central
        image = Image(
            source='recursos/principal.jpg',  # Ruta de la imagen que desees usar
            size_hint=(0.2, 0.4),
            allow_stretch=True,
            keep_ratio=False,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        layout.add_widget(image)
        
        # Botón "Enfermedades"
        button_enfermedades = Button(
            text="Enfermedades",
            font_name="Roboto",  # Usar la fuente predeterminada
            background_color=(0.2, 0.8, 0.2, 1),  # Verde
            color=(1, 1, 1, 1),  # Texto en blanco
            font_size=24,
            size_hint=(0.3, 0.15),
            bold=True,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        button_enfermedades.bind(on_release=self.ir_enfermedades)
        layout.add_widget(button_enfermedades)
        
        # Botón "Preguntas Frecuentes"
        button_preguntas = Button(
            text="Preguntas Frecuentes",
            font_name="Roboto",
            background_color=(0.2, 0.6, 1, 1),  # Azul
            color=(1, 1, 1, 1),  # Texto en blanco
            font_size=24,
            size_hint=(0.3, 0.15),
            bold=True,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        button_preguntas.bind(on_release=self.ir_preguntas)
        layout.add_widget(button_preguntas)
        
        # Botón "Salir del Programa"
        button_salir = Button(
            text="Salir del Programa",
            font_name="Roboto",
            background_color=(0.5, 0.5, 0.5, 1),  # Gris
            color=(1, 1, 1, 1),  # Texto en blanco
            font_size=24,
            size_hint=(0.3, 0.15),
            bold=True,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        button_salir.bind(on_release=self.salir_programa)
        layout.add_widget(button_salir)
        
        # Footer (opcional)
        footer = Label(
            text="Cuidamos de ti y de los tuyos",
            font_size=18,
            color=(0.2, 0.2, 0.2, 1),  # Gris oscuro
            size_hint=(1, 0.1)
        )
        layout.add_widget(footer)
        
        # Agregar el layout al screen
        self.add_widget(layout)
    
    def ir_enfermedades(self, instance):
        self.manager.current = 'seleccion_enfermedad'
    
    def ir_preguntas(self, instance):
        self.manager.current = 'seleccion_preguntas_frecuentes'
    
    def salir_programa(self, instance):
        App.get_running_app().stop()

# Pantalla de selección de enfermedad
class SeleccionEnfermedadScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Label instructivo
        label_instructivo = Label(
            text='Selecciona la enfermedad estomacal que estás presentando',
            font_size=24,
            color=(0, 0.5, 0, 1),  # Verde oscuro
            size_hint=(1, 0.1),
            bold=True,
            halign='center'
        )
        layout.add_widget(label_instructivo)
        
        # Spinner para seleccionar enfermedad estomacal
        self.spinner_enfermedades = Spinner(
            text='Selecciona una enfermedad estomacal',
            values=list(problemas_digestivos.keys()),
            size_hint=(None, None),
            size=(400, 50),
            bold=True,
            pos_hint={'center_x': .5, 'center_y': .5},
            background_color=[0.2, 0.6, 0.8, 1])
        self.spinner_enfermedades.bind(text=self.on_enfermedad_select)
        layout.add_widget(self.spinner_enfermedades)
        
        # Espacio para la imagen de una persona enferma
        image_path = os.path.join('recursos/seleccion_enfermedad.jpg')  # Ajusta la ruta de la imagen
        image = Image(
            source=image_path,
            size_hint=(0.3, 0.2),
            allow_stretch=True,
            keep_ratio=False,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        layout.add_widget(image)
        
        # Botón para continuar a la información detallada
        button_continuar = Button(
            text='Continuar',
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': .5},
            background_color=[0.2, 0.8, 0.2, 1])  # Verde claro
        button_continuar.bind(on_release=self.mostrar_informacion_enfermedad)
        layout.add_widget(button_continuar)
        
        # Botón para regresar al Menú Principal
        button_back = Button(
            text='Volver al Menú Principal',
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': .5},
            background_color=[0.8, 0.2, 0.2, 1])  # Rojo claro
        button_back.bind(on_release=self.volver_menu)
        layout.add_widget(button_back)
        
        self.add_widget(layout)
        self.selected_enfermedad = None

    def on_leave(self):
        # Resetea el Spinner antes de salir de la pantalla
        self.reset_spinner()

    def on_enfermedad_select(self, spinner, text):
        self.selected_enfermedad = text

    def mostrar_informacion_enfermedad(self, instance):
        if self.selected_enfermedad:
            self.manager.transition = SlideTransition(direction="left")
            self.manager.get_screen('informacion_enfermedad').mostrar_informacion(self.selected_enfermedad)
            self.manager.current = 'informacion_enfermedad'
        else:
            self.popup_error("Por favor seleccione una enfermedad antes de continuar.")

    def popup_error(self, mensaje):
        popup = Popup(title='Error', content=Label(text=mensaje), size_hint=(None, None), size=(400, 200))
        popup.open()

    def volver_menu(self, instance):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'menu'

    def reset_spinner(self):
        self.spinner_enfermedades.text = 'Selecciona una enfermedad estomacal'
        self.selected_enfermedad = None

# Pantalla de información detallada de la enfermedad
class InformacionEnfermedadScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_problema = None  # Variable para almacenar la enfermedad seleccionada

        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Label para el nombre de la enfermedad seleccionada
        self.label_enfermedad = Label(
            text='Información sobre la Enfermedad',
            font_size=24,
            color=(0, 0.5, 0, 1),  # Verde oscuro
            size_hint=(1, 0.1),
            halign='center',
            valign='middle'
        )
        layout.add_widget(self.label_enfermedad)

        # Spinner para seleccionar grupo de edad
        self.spinner_edad = Spinner(
            text='Selecciona tu grupo de edad',
            values=['Bebé/Niño', 'Adulto/Adulto Mayor'],
            size_hint=(None, None),
            size=(400, 50),
            pos_hint={'center_x': .5},
            background_color=[0.2, 0.6, 0.8, 1]
        )
        self.spinner_edad.bind(text=self.on_edad_select)
        layout.add_widget(self.spinner_edad)

        # GridLayout para la información de la enfermedad
        info_layout = GridLayout(cols=1, padding=[20, 20], spacing=10, size_hint_y=None)
        info_layout.bind(minimum_height=info_layout.setter('height'))

        self.label_medicacion = Label(
            text='',
            font_size=18,
            color=(0, 0, 0, 1),  # Negro
            size_hint_y=None,
            halign='left',
            valign='top',
            text_size=(self.width - 40, self.height - 20)  # Ajustar el ancho
        )
        info_layout.add_widget(self.label_medicacion)

        self.label_alimentacion = Label(
            text='',
            font_size=18,
            color=(0, 0, 0, 1),  # Negro
            size_hint_y=None,
            halign='left',
            valign='top',
            text_size=(self.width - 40, self.height - 20)  # Ajustar el ancho
        )
        info_layout.add_widget(self.label_alimentacion)

        self.label_recomendacion = Label(
            text='',
            font_size=18,
            color=(0, 0, 0, 1),  # Negro
            size_hint_y=None,
            halign='left',
            valign='top',
            text_size=(self.width - 40, self.height - 20)  # Ajustar el ancho
        )
        info_layout.add_widget(self.label_recomendacion)

        scroll_view = ScrollView(size_hint=(1, 0.4))
        scroll_view.add_widget(info_layout)
        layout.add_widget(scroll_view)

        # Imagen relacionada con la enfermedad
        self.image = Image(
            source='',  # No se muestra ninguna imagen inicialmente
            size_hint=(0.3, 0.4),
            allow_stretch=True,
            keep_ratio=True,
            pos_hint={'center_x': .5}
        )
        layout.add_widget(self.image)

        # Botón para regresar a la selección de enfermedad
        button_back = Button(
            text='Volver a Selección de Enfermedad',
            size_hint=(None, None),
            size=(300, 50),
            pos_hint={'center_x': .5},
            background_color=[0.8, 0.2, 0.2, 1]
        )
        button_back.bind(on_release=self.volver_seleccion_enfermedad)
        layout.add_widget(button_back)

        self.add_widget(layout)

    def on_edad_select(self, spinner, text):
        if self.selected_problema:
            problema = problemas_digestivos[self.selected_problema]
            medicacion = problema['medicacion']['dosis'].get(text, "No especificado")
            self.label_medicacion.text = (f"Medicación para {text}:\n"
                                          f"Medicamento: {problema['medicacion']['medicamento']}\n"
                                          f"Dosis: {medicacion}\n"
                                          f"Tiempo de medicación: {problema['medicacion']['tiempo_med']}")

            self.label_alimentacion.text = (f"Alimentación recomendada:\n"
                                            f"  Debe comer: {problema['dieta']['debe_comer']}\n"
                                            f"  No debe comer: {problema['dieta']['no_debe_comer']}")

            self.label_recomendacion.text = f"Recomendación: {problema['recomendacion']}"

            # Ajustar el tamaño del texto
            self.label_medicacion.text_size = (self.width - 40, None)
            self.label_alimentacion.text_size = (self.width - 40, None)
            self.label_recomendacion.text_size = (self.width - 40, None)

            # Mostrar la imagen relacionada con la enfermedad
            image_path = os.path.join('recursos', f"{self.selected_problema}.jpg")
            if os.path.exists(image_path):
                self.image.source = image_path
            else:
                self.image.source = 'recursos/default.jpg'  # Imagen por defecto si no se encuentra la específica

        else:
            self.label_medicacion.text = "Selecciona un grupo de edad."

    def set_enfermedad(self, enfermedad):
        """ Configura la enfermedad seleccionada en la pantalla anterior. """
        self.selected_problema = enfermedad
        self.label_enfermedad.text = f"Información sobre: {enfermedad}"
        self.label_medicacion.text = ""
        self.label_alimentacion.text = ""
        self.label_recomendacion.text = ""
        self.image.source = ''  # Limpiar la imagen

    def mostrar_informacion(self, enfermedad):
        """ Método para configurar la pantalla con la enfermedad seleccionada. """
        self.set_enfermedad(enfermedad)

    def volver_seleccion_enfermedad(self, instance):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'seleccion_enfermedad'
        self.reset_screen()  # Resetea la pantalla al regresar

    def reset_screen(self):
        """ Resetea la pantalla al regresar a la selección de enfermedad. """
        self.spinner_edad.text = 'Selecciona tu grupo de edad'
        self.label_medicacion.text = ""
        self.label_alimentacion.text = ""
        self.label_recomendacion.text = ""
        self.image.source = ''  # Limpiar la imagen

# Pantalla de selección de sección de preguntas frecuentes
class SeleccionPreguntasFrecuentesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Configuración del color de fondo
        Window.clearcolor = (0.9, 0.95, 1, 1)  # Azul suave

        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=[20, 10, 20, 10], spacing=20)

        # Label instructivo
        label_instructivo = Label(
            text='Selecciona la sección de preguntas frecuentes de tu interés',
            font_size=24,
            color=(0, 0.5, 0, 1),  # Verde oscuro
            size_hint=(1, 0.15),
            halign='center',
            valign='middle'
        )
        layout.add_widget(label_instructivo)

        # Spinner para seleccionar la sección de preguntas frecuentes
        self.spinner_secciones = Spinner(
            text='Selecciona una sección',
            values=list(preguntas_frecuentes.keys()),
            size_hint=(0.8, None),
            size=(400, 50),
            pos_hint={'center_x': .5},
            background_color=[0.2, 0.6, 0.8, 1]
        )
        layout.add_widget(self.spinner_secciones)

        # Espacio para la imagen de comidas balanceadas
        image_path = os.path.join('recursos\preguntas_fre.jpg')  # Ajusta la ruta de la imagen
        image = Image(
            source=image_path,
            size_hint=(1, 0.5),
            allow_stretch=True,
            keep_ratio=True
        )
        layout.add_widget(image)

        # Botón para continuar a la sección de preguntas
        button_continuar = Button(
            text='Continuar',
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': .5},
            background_color=[0.2, 0.8, 0.2, 1]  # Verde claro
        )
        button_continuar.bind(on_release=self.continuar_seccion)
        layout.add_widget(button_continuar)

        # Botón para regresar al Menú Principal (abajo)
        button_back = Button(
            text='Volver al Menú Principal',
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': .5},
            background_color=[0.8, 0.2, 0.2, 1]  # Rojo claro
        )
        button_back.bind(on_release=self.volver_menu)
        layout.add_widget(button_back)

        self.add_widget(layout)

    def on_leave(self):
        # Resetea el Spinner antes de salir de la pantalla
        self.reset_spinner()

    def continuar_seccion(self, instance):
        if self.spinner_secciones.text != 'Selecciona una sección':
            # Asegúrate de que el método mostrar_preguntas esté disponible
            presentacion_preguntas_screen = self.manager.get_screen('presentacion_preguntas')
            if hasattr(presentacion_preguntas_screen, 'mostrar_preguntas'):
                presentacion_preguntas_screen.mostrar_preguntas(self.spinner_secciones.text)
                self.manager.transition = SlideTransition(direction="left")
                self.manager.current = 'presentacion_preguntas'
            else:
                self.popup_error("Error: No se pudo mostrar las preguntas. Contacta al administrador.")
        else:
            self.popup_error("Por favor selecciona una sección antes de continuar.")

    def volver_menu(self, instance):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'menu'

    def reset_spinner(self):
        """ Resetea la pantalla al regresar al Menú Principal. """
        self.spinner_secciones.text = 'Selecciona una sección'

    def popup_error(self, mensaje):
        """ Muestra un popup de error si no se selecciona una sección. """
        popup = Popup(title='Error', content=Label(text=mensaje), size_hint=(None, None), size=(400, 200))
        popup.open()

# Pantalla de presentación de preguntas frecuentes
class PresentacionPreguntasScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Label para el nombre de la sección seleccionada
        self.label_seccion = Label(
            text='Preguntas Frecuentes',
            font_size=24,
            color=(0, 0.5, 0, 1),  # Verde oscuro
            size_hint=(1, 0.1),
            halign='center',
            valign='middle'
        )
        layout.add_widget(self.label_seccion)

        # StackLayout principal que contendrá las filas
        self.stack_layout = StackLayout(orientation='lr-tb', padding=[20, 20], spacing=20, size_hint_y=None)
        self.stack_layout.bind(minimum_height=self.stack_layout.setter('height'))

        # ScrollView para el layout de preguntas
        scroll_view = ScrollView(size_hint=(1, 0.8))
        scroll_view.add_widget(self.stack_layout)
        layout.add_widget(scroll_view)

        # Botón para regresar a la selección de sección
        button_back = Button(
            text='Volver a Selección de Sección',
            size_hint=(None, None),
            size=(300, 50),
            pos_hint={'center_x': .5},
            background_color=[0.8, 0.2, 0.2, 1]  # Rojo claro
        )
        button_back.bind(on_release=self.volver_seleccion)
        layout.add_widget(button_back)

        self.add_widget(layout)

    def mostrar_preguntas(self, seccion):
        """ Muestra las preguntas y respuestas según la sección seleccionada. """
        self.stack_layout.clear_widgets()  # Limpiar preguntas anteriores

        preguntas = preguntas_frecuentes.get(seccion, {}).get('preguntas', [])
        fila_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint_y=None, height=0)

        for idx, pregunta in enumerate(preguntas):
            stack_layout = self.crear_stack_layout(pregunta['pregunta'], pregunta['respuesta'], "path_to_image")

            fila_layout.add_widget(stack_layout)
            fila_layout.height = max(fila_layout.height, stack_layout.height)

            # Si alcanzamos 3 preguntas en una fila o es la última pregunta, añadimos la fila al layout principal
            if (idx + 1) % 3 == 0 or idx == len(preguntas) - 1:
                self.stack_layout.add_widget(fila_layout)
                fila_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint_y=None, height=0)

        # Desplazar el ScrollView a la parte superior
        self.stack_layout.parent.scroll_y = 1

        # Actualiza el nombre de la sección
        self.label_seccion.text = f"Preguntas Frecuentes: {seccion}"

    def crear_stack_layout(self, pregunta_texto, respuesta_texto, imagen_source):
        stack_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None), width=Window.width / 3 - 60)
        
        # Crear layouts para pregunta/respuesta e imagen
        pregunta_respuesta_layout = self.crear_pregunta_layout(pregunta_texto, respuesta_texto)
        imagen_layout = self.crear_imagen_layout(imagen_source)
        
        # Añadir pregunta/respuesta en la parte superior y la imagen en la parte inferior
        stack_layout.add_widget(pregunta_respuesta_layout)
        stack_layout.add_widget(imagen_layout)

        # Establecer el tamaño del stack_layout
        stack_layout.height = pregunta_respuesta_layout.height + imagen_layout.height
        
        return stack_layout

    def crear_pregunta_layout(self, pregunta_texto, respuesta_texto):
        # BoxLayout para mantener pregunta y respuesta en una columna
        contenido_layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(1, None))
        
        pregunta_label = Label(
            text=pregunta_texto,
            font_size=18,
            color=(0, 0, 0, 1),  # Negro
            size_hint=(1, None),
            halign='justify',
            valign='top',
            text_size=(Window.width / 3 - 60, None)
        )
        pregunta_label.bind(texture_size=pregunta_label.setter('size'))

        respuesta_label = Label(
            text=respuesta_texto,
            font_size=16,
            color=(0, 0, 0, 1),  # Negro
            size_hint=(1, None),
            halign='justify',
            valign='top',
            text_size=(Window.width / 3 - 60, None)
        )
        respuesta_label.bind(texture_size=respuesta_label.setter('size'))

        # Ajustar el tamaño del contenido layout según los textos
        contenido_layout.add_widget(pregunta_label)
        contenido_layout.add_widget(respuesta_label)
        contenido_layout.height = pregunta_label.height + respuesta_label.height

        return contenido_layout

    def crear_imagen_layout(self, imagen_source):
        # BoxLayout para centrar la imagen en X y mantenerla en la parte inferior
        imagen_layout = BoxLayout(orientation='vertical', size_hint=(1, None), height=150)
        
        imagen = Image(
            source=imagen_source,
            size_hint=(None, None),
            height=150,
            width=150,
            pos_hint={'center_x': 0.5},  # Centrar la imagen en X
            allow_stretch=True,
            keep_ratio=True
        )
        
        imagen_layout.add_widget(imagen)
        
        return imagen_layout

    def volver_seleccion(self, instance):
        """ Vuelve a la pantalla de selección de sección. """
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'seleccion_preguntas_frecuentes'
        self.reset_screen()  # Resetea la pantalla al regresar

    def reset_screen(self):
        """ Resetea la pantalla al regresar a la selección de sección. """
        self.label_seccion.text = 'Preguntas Frecuentes'
        self.stack_layout.clear_widgets()

# Clase principal de la aplicación
class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='menu'))
        sm.add_widget(SeleccionEnfermedadScreen(name='seleccion_enfermedad'))
        sm.add_widget(InformacionEnfermedadScreen(name='informacion_enfermedad'))
        sm.add_widget(SeleccionPreguntasFrecuentesScreen(name='seleccion_preguntas_frecuentes'))
        sm.add_widget(PresentacionPreguntasScreen(name='presentacion_preguntas'))
        return sm

if __name__ == '__main__':
    MainApp().run()