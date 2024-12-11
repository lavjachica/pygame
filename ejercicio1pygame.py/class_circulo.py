import pygame
import math

class Circulo():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.velocidad = 5
        self.color = (255,0,0)

    def dibujar(self,ventana):
        center = (self.x,self.y)
        radio = 90
        pygame.draw.circle(ventana,self.color,center,radio)

    def movimiento(self, teclas):

        movimiento_x = 0
        movimiento_y = 0

        # Movimientos en el eje y 
        if teclas[pygame.K_i]:
                movimiento_y = - self.velocidad
        if teclas[pygame.K_k]:
            movimiento_y = self.velocidad
            
            # Movimientos en el eje x
        if teclas[pygame.K_l]:
            movimiento_x = self.velocidad
        if teclas[pygame.K_j]:
            movimiento_x = - self.velocidad

            # Ajustando velocidad para cuando hayan movimientos en diagonales
        if movimiento_x != 0 and movimiento_y != 0:
            movimiento_x /= math.sqrt(2)
            movimiento_y /= math.sqrt(2)

            # actualizando los movimientos
        self.x += movimiento_x
        self.y += movimiento_y