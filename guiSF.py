from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from SeriesFourier import serieFourierCuadrada, serieFourierTriangular

class Principal(Screen):
    def calcular(self):

        if self.ids.r.text != "":
            r = float(self.ids.r.text)
        else:
            r = 0
        
        if self.ids.s.text != "":
            s = float(self.ids.s.text)
        else:
            s = 0

        if self.ids.n.text != "":
            n = int(self.ids.n.text)
        else:
            n = 6

        opcion = self.ids.funcion.text

        if opcion == "Cuadrada":
            serieFourierCuadrada(s, r, n)
        else:
            serieFourierTriangular(s, r, n)
        print("Hola mundo")

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("guiSF.kv")

class MyApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    myApp = MyApp()
    myApp.run()