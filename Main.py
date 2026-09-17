from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class CalculadoraLayout(BoxLayout):
    pass


class CalculadoraApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.operacion = ""

    def presionar_boton(self, texto):
        if texto == "=":
            try:
                resultado = eval(self.operacion)
                self.root.ids.pantalla.text = str(resultado)
                self.operacion = str(resultado)
            except:
                self.root.ids.pantalla.text = "Error"
                self.operacion = ""

        else:
            self.operacion += texto
            self.root.ids.pantalla.text = self.operacion

    def limpiar(self):
        self.operacion = ""
        self.root.ids.pantalla.text = "0"


CalculadoraApp().run()