import pygame
import random

pygame.init()

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Laboratorio N°2 - Ejercicio 2")


# Colores
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
AZUL = (0,0, 255)
## velocidad del triangulo 
velocidad = 0.5
# FPS (Frames por segundo)
FPS = 60
reloj = pygame.time.Clock()


class Puntos:
    def __init__(self, x, y, velocidad):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.radio = 8  # Tamaño del punto

    def mover(self):
        self.y += self.velocidad
        if self.y > ALTO:  # Se reinicia ka posición cuando el punto rojo sale de la pantalla
            self.reiniciar()

    def reiniciar(self):
        self.x = random.randint(0, ANCHO - self.radio)
        self.y = random.randint(-100, -40)

    def dibujar(self):
        pygame.draw.circle(pantalla, ROJO, (self.x, self.y), self.radio)

# Clase Triángulo
teclas = pygame.key.get_pressed()
class Triangulo:
    def __init__(self, x, y):
        self.pos = [x,y]
        self.color = AZUL

    def mover(self, pantalla): 
        if teclas[pygame.K_UP]:
            self.pos -= velocidad
        if teclas[pygame.K_DOWN]:
            self.pos += velocidad
        if teclas[pygame.K_LEFT]:
            self.pos -= velocidad
        if teclas[pygame.K_RIGHT]:
            self.pos += velocidad
    def dibujar(self, pantalla):
        pygame.draw.polygon(pantalla, self.color, ((self.pos[0], self.pos[1]),
                                            (self.pos[0] -30, self.pos[1]+ 50),
                                            (self.pos[0] +30, self.pos[1] +50)))

# Función Principal
    def main():
    # Creación de la lista de puntos rojos
        puntos_rojos = [Puntos(random.randint(0, ANCHO - 10), random.randint(-100, -40), random.randint(2, 6)) for _ in range(5)]

        corriendo = True
        while corriendo:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False

        # Limpiar pantalla
            pantalla.fill(NEGRO)
            triangulo1.dibujar(pantalla)
            triangulo1.mover(teclas)

        # Mover y dibujar los puntos rojos
            for punto in puntos_rojos:
               punto.mover()
               punto.dibujar()

        # Actualizar pantalla
            pygame.display.flip()
            reloj.tick(FPS)
        

    pygame.quit()

# Iniciar el juego
    if __name__ == "__main__":
       main()
triangulo1= Triangulo(400,500)