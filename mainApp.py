import pygame
from pygame.locals import *

class Termometro:

    def __init__(self):

        self.disfraz = pygame.image.load("D:/imagenes/termometro/termo1.png")#Variable que contiene el disfraz
        #La variable self.disfraz sólo me sirve para fijar la imagen del termómetro en la pantalla
        




class mainApp:

    entrada = None
    selector = None
    termometro = None

    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))#Dimensiones de mi termóemtro
        pygame.display.set_caption("TERMÓMETRO CASERO")
        self.__screen.fill((244, 236, 203))#El fondo de pantalla es un color

        self.termometro = Termometro() #Esta variable del Constructor me almacena el objeto
                                        #de clase Termómetro. Solo pinta el termómetro

    #Arrancamos el programa
    def start(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__on_close()


            #Me dibuja el termómetro
            self.__screen.blit(self.termometro.disfraz, (50,34))

            #Pintamos el programa, lo renderizamos
            pygame.display.flip()


    #Cerramos el programa con un método privado
    def __on_close(self):
        
        pygame.quit()
        sys.quit()





if __name__ == "__main__":

    pygame.init

    app = mainApp() # Creo un objeto de la clase mainApp

    app.start()

    input()

