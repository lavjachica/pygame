import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Mi Juego en Pygame")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)

# Configurar la fuente
fuente = pygame.font.Font(None, 36)

# Posición del rectángulo
x = ancho // 2
y = alto // 2
velocidad = 5

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        

    # Manejo de teclas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad

    # Limitar el movimiento dentro de la pantalla
    x = max(0, min(ancho - 50, x))
    y = max(0, min(alto - 50, y))

    # Dibujar en la pantalla
    pantalla.fill(NEGRO)  # Limpiar la pantalla con negro
    pygame.draw.rect(pantalla, AZUL, (x, y, 50, 50))  # Dibujar un rectángulo azul

    # Mostrar texto en pantalla
    texto = fuente.render('Usa las flechas para mover el cuadro', True, BLANCO)
    pantalla.blit(texto, (50, 50))  # Dibuja el texto en (50, 50)

    pygame.display.flip()  # Actualizar la pantalla

# Finalizar Pygame (aunque en este caso nunca se alcanza)
pygame.quit()