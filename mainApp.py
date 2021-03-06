import pygame, sys
from pygame.locals import *

class Termometro:

    def __init__(self):

        self.disfraz = pygame.image.load("D:/imagenes/termometro/termo1.png")#Variable que contiene el disfraz
        #La variable self.disfraz sólo me sirve para fijar la imagen del termómetro en la pantalla


class Entrada:

    __value = 0
    __strValue = "0"
    __posicion = [0,0]
    __tamagno = [0,0]


    #Creamos la fuente a usar en el cuadro de texto con su tamaño. Todo ello en el constructor
    def __init__(self, value = 0):

        self.__font = pygame.font.SysFont('Arial', 24)

        self.value(value)

    def on_event(self, event):

        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__strValue) < 10: #event.unicode es la tecla que hemos pulsado

                self.__strValue += event.unicode

                


        """
        try:
            self.__value = int(value)
            self.__strValue = str(value)
        except:
            pass"""
        

       


    def value(self, value = None): #Función getter y setter con excepción
        if value == None:
            return self.__value
        else:
            val = str(value)

            try:
                self.__value = int(val)
                self.__strValue = val

            except:
                pass

    def anchoCuadro(self, val = None): 
        if val == None:
            return self.__tamagno[0]

        else:

            try:
                self.__tamagno[0] = int(val)

            except:
                pass


    def altoCuadro(self, val = None):
            if val == None:
                return self.__tamagno[1]

            else:

                try:
                    self.__tamagno[1] = int(val)

                except:
                    pass


    def size(self, val = None):
        if val == None:
            return self.__tamagno
        else:
            try:
                h = int(val[1])
                w = int(val[0])
                self.__tamagno = [int(val[0]), int(val[1])]

            except:

                pass


    def posX(self, val = None):
        if val == None:
            return self.__posicion[0]
        else:
            try:
                self.__posicion[0] = int(val)
            except:
                pass
    
    def posY(self, val = None):
        if val == None:
            return self.__posicion[1]
        else:
            try:
                self.__posicion[1] = int(val)
            except:
                pass


    def posicionTotal(self, val = None):
        if val == None:
            return self.__posicion
        else:
            try:
                self.__posicion = [int(val[0]), int(val[1])]

            except:
                pass

    def render(self):

         #Creamos el cuadro de texto....: Este textBlock sólo puede recoger y contener texto
        textBlock = self.__font.render(self.__strValue, True, (74, 74, 74))

        rectangulo = textBlock.get_rect() #Nos da un rectángulo gráfico
        rectangulo.left = self.__posicion[0] # Coordenada de la X
        rectangulo.top = self.__posicion[1] #Coordenada de la Y
        rectangulo.size =  self.__tamagno

        #Voy a devolver textBlock y rectángulo. Puedo hacerlo de 2 formas.. como un diccionario o una tupla

        """ 
        return{
            "fondo" : rectangulo,
            "texto" : textBlock
        }
        """
        return (rectangulo, textBlock)





class mainApp:

    entrada = None
    selector = None
    termometro = None

    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))#Dimensiones de mi termóemtro
        pygame.display.set_caption("TERMÓMETRO pY")
        self.__screen.fill((244, 236, 203))#El fondo de pantalla es un color

        self.termometro = Termometro() #Esta variable del Constructor me almacena el objeto
                                        #de clase Termómetro. Solo pinta el termómetro

        self.entrada = Entrada()

        self.entrada.posicionTotal([106, 58])

        self.entrada.size([133, 28])



    #Arrancamos el programa
    def start(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__on_close()

                    self.entrada.on_event(event)


                

            #Me dibuja el termómetro en su posición
            self.__screen.blit(self.termometro.disfraz, (50,34))

            #Pintamos el cuadro de texto
            texto = self.entrada.render()

            pygame.draw.rect(self.__screen, (255, 255, 255), texto[0]) #texto[0] es return (rectangulo, textBlock) de la función render
                                                                        #creamos el rectángulo blanco en su posición y tamaño
            self.__screen.blit(texto[1], self.entrada.posicionTotal())#Pintamos foto del texto

            #Pintamos el programa, lo renderizamos
            pygame.display.flip()


    #Cerramos el programa con un método privado
    def __on_close(self):
        
        pygame.quit()
        sys.exit()





if __name__ == "__main__":

    pygame.init()

    app = mainApp() # Creo un objeto de la clase mainApp

    app.start()

    input()

