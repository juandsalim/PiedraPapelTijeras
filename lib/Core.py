import pygame
import random
from lib import Color as c
from lib import Var as v
# Inicialización de Pygame
pygame.init()
pygame.mixer.init()

# Inicialización de la ventana del juego
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Piedra, Papel, Tijera")


# Clase para representar una opción del juego

class Opcion:
    def __init__(self, img_path, pos, choice):
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (60, 60))
        self.rect = self.img.get_rect()
        self.rect.topleft = pos
        self.choice = choice
        
# Clase para representar al jugador
class Jugador:
    def __init__(self):
        self.choice = None
        self.score = 0
    
    def set_choice(self, choice):
        self.choice = choice
    
    def set_random_choice(self, options):
        self.choice = random.choice([option.choice for option in options])

# class Humano:
class Humano(Jugador):
    def __init__(self):
        super().__init__()
        
# Clase para representar a la máquina
class Maquina(Jugador):
    def __init__(self, options):
        super().__init__()
        self.options = options  
        

class Juego:
    def __init__(self):
        self.options = []
        self.jugador = Humano()
        self.maquina = Maquina(self.options)
        self.result = None
        
        # Carga de imágenes y creación de opciones
        
        self.options.append(Opcion("sprite\jugador\piedra.png", (180, 100), "piedra"))
        self.options.append(Opcion("sprite\jugador\papel.png", (280, 100), "papel"))
        self.options.append(Opcion("sprite\jugador\ijera.png", (380, 100), "tijera"))
    
    pygame.mixer.music.load(".\\music\\main.mp3")
    pygame.mixer.music.play(-1)
    
    def run(self):
        # Bucle principal del juego
        enter = False
        while not enter:
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key==pygame.K_RETURN:
                        enter=True
            window.blit(v.fondomain,(0,0))
            pygame.display.flip()
        
        
        running = True
        while running:
            # Manejo de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Obtener la posición del clic del jugador
                    pos = pygame.mouse.get_pos()
                    
                    # Verificar si el jugador hizo clic en una opción
                    for option in self.options:
                        if option.rect.collidepoint(pos):
                            self.jugador.set_choice(option.choice)
                            self.maquina.set_random_choice(self.options)
                            
                            # Lógica del juego
                            if self.jugador.choice == self.maquina.choice:
                                self.result = "Empate"
                            elif (self.jugador.choice == "piedra" and self.maquina.choice == "tijera") or \
                                 (self.jugador.choice == "papel" and self.maquina.choice == "piedra") or \
                                 (self.jugador.choice == "tijera" and self.maquina.choice == "papel"):
                                self.result = "¡Ganaste!"
                                self.jugador.score += 1
                            else:
                                self.result = "¡Perdiste!"
                                self.maquina.score += 1
                            
                            # Mostrar resultado en la consola
                            print(f"Jugador: {self.jugador.choice} | Máquina: {self.maquina.choice} | Resultado: {self.result}")
            
            # Actualizar la ventana del juego
            window.fill(c.NEGRO)
            for option in self.options:
            # Renderizado de las puntuaciones y nombres de jugadores
                fuente=pygame.font.SysFont("Roboto",60)
                mensaje=fuente.render("Selecciona una opcion",40,c.BLANCO)
                score_h=pygame.font.SysFont("Roboto",30).render("Humano",20,c.BLANCO)
                score_m=pygame.font.SysFont("Roboto",30).render("Maquina",20,c.BLANCO)
                mensaje_r=fuente.render(self.result,50,c.BLANCO)
                puntuacion_jugador = fuente.render(str(self.jugador.score),50,c.BLANCO)
                puntuacion_maquina = fuente.render(str(self.maquina.score),50,c.BLANCO)
            # dibujos en pantalla    
                window.blit(score_h,[40,220])
                window.blit(score_m,[530,220])
                window.blit(puntuacion_jugador,[60,250])
                window.blit(puntuacion_maquina,[590,250])
                window.blit(mensaje,[90,30])
                window.blit(mensaje_r,[220,200])
                window.blit(option.img, option.rect.topleft)
            # verifico la eleccion de los jugadores para dibujar la misma en pantalla  
                if self.jugador.choice == "piedra":
                    window.blit(v.piedra,[100,300])
                elif self.jugador.choice == "papel":
                    window.blit(v.papel,[100,300])
                elif self.jugador.choice == "tijera":
                    window.blit(v.tijera,[100,300])
                    
                if self.maquina.choice == "piedra":
                    window.blit(v.piedram,[400,300])
                elif self.maquina.choice == "papel":
                    window.blit(v.papelm,[400,300])
                elif self.maquina.choice == "tijera":
                    window.blit(v.tijeram,[400,300])
            pygame.display.flip()
        
        # Finalización del juego
        pygame.quit()
        