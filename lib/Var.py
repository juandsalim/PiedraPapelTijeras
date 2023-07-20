
import pygame

"""sprites para jugador """

piedra = pygame.image.load("sprite\jugador\piedra.png")
piedra = pygame.transform.scale(piedra,(150,150))

papel = pygame.image.load("sprite\jugador\papel.png")
papel = pygame.transform.scale(papel,(150,150))

tijera = pygame.image.load("sprite\jugador\ijera.png")
tijera = pygame.transform.scale(tijera,(150,150))

"""sprites para maquina"""

piedram = pygame.image.load("sprite\maquina\piedra.png")
piedram = pygame.transform.scale(piedram,(150,150))

papelm = pygame.image.load("sprite\maquina\papel.png")
papelm = pygame.transform.scale(papelm,(150,150))

tijeram = pygame.image.load("sprite\maquina\ijera.png")
tijeram = pygame.transform.scale(tijeram,(150,150))

"""fondo main"""

fondomain = pygame.image.load(".\\sprite\\fondos\\inicio.png")
fondomain = pygame.transform.scale(fondomain,(640,480))

