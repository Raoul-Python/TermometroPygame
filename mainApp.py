import pygame
from pygame.locals import *

class mainApp(self):

    entrada = None
    selector = None
    termometro = None

    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))#Dimensiones de mi termóemtro
        pygame.display.set_caption("TERMÓMETRO CASERO")
        self.__screen.fill((244, 236, 203))#El fondo de pantalla es un color
        

