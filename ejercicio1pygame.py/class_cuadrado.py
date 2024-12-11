import pygame
import math

class Cuadrado():
    def __init__(self,x,y):
        self.x = x #movimientos en los ejes (x,y)
        self.y = y
        self.color = (0,0,255)
        self.velocidad = 5 # aumento para los pixeles

    # cuadrado
    def dibujar(self, ventana):

        puntos = [(self.x,self.y), (self.x +100, self.y), (self.x +100, self.y -100), (self.x, self.y -100) ]
        pygame.draw.polygon(ventana,self.color,puntos)

# el movimiento para el cuadrado

    def movimiento(self,teclas):

        movimiento_x = 0
        movimiento_y = 0

        
        # Movimientos en el eje y 
        if teclas[pygame.K_w]:
            movimiento_y = - self.velocidad
        if teclas[pygame.K_s]:
            movimiento_y = self.velocidad
        
        # Movimientos en el eje x
        if teclas[pygame.K_d]:
            movimiento_x = self.velocidad
        if teclas[pygame.K_a]:
            movimiento_x = - self.velocidad

        # Ajustando velocidad para cuando hayan movimientos en diagonales
        if movimiento_x != 0 and movimiento_y != 0:
            movimiento_x /= math.sqrt(2)
            movimiento_y /= math.sqrt(2)

        # actualizando los movimientos
        self.x += movimiento_x
        self.y += movimiento_y