from tkinter import *
from tkinter import ttk



class mainApp(Tk): #la clase mainApp hereda de la clase "padre" Tk()

    size = "200x350"
    entrada = None
    tipoUnidad = None

    def __init__(self):
        Tk.__init__(self)#Llama al constructor de Tk()

        self.geometry(self.size)
        self.title("TERMÓMETRO")
        self.configure(bg = "#DED7B9")

        self.temperatura = StringVar(value="")
        self.tipoUnidad = StringVar(value="C")

        self.createLayout()

    
    def createLayout(self):

        self.entrada = Entry(self, variable = self.temperatura)
       





    def start(self):
        self.mainloop()

if __name__ == "__main__":

    objeto = mainApp()
    objeto.createLayout()
    objeto.start()

    

