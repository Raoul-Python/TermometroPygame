from tkinter import *
from tkinter import ttk



class mainApp(Tk): #la clase mainApp hereda de la clase "padre" Tk()

    size = "200x350"
    entrada = None
    tipoUnidad = None

    __temperaturaAnterior = ""


    def __init__(self):
        Tk.__init__(self)#Llama al constructor de Tk()

        self.geometry(self.size)
        self.title("TERMÓMETRO")
        self.configure(bg = "#DED7B9")
        self.resizable(0,0)

        self.temperatura = StringVar(value="")
        self.temperatura.trace("w", self.validateTemperature)

        self.tipoUnidad = StringVar(value="C")

        self.createLayout()

    
    def createLayout(self):
        #Cuadro de texto
        self.entrada = ttk.Entry(self, textvariable = self.temperatura).place(x=10, y=10)

        #Etiqueta...:
        self.lbUnidad = ttk.Label(self, text="Grados....: ").place(x=10, y=45)

        self.rb1 = ttk.Radiobutton(self, text = "Farenheit", variable= self.tipoUnidad, value = "F").place(x =20, y=75)
        self.rb2 = ttk.Radiobutton(self, text= "Centígrados", variable = self.tipoUnidad, value = "C").place(x =20, y=110)






       


    def validateTemperature(self, *args):

        nuevoValor = self.temperatura.get()

        #print(self.temperatura.get())

        try:

            float(nuevoValor)
            self.__temperaturaAnterior = nuevoValor
        except:
            self.temperatura.set(self.__temperaturaAnterior)


    def start(self):
        self.mainloop()

if __name__ == "__main__":

    objeto = mainApp()
    objeto.createLayout()
    objeto.start()

    

