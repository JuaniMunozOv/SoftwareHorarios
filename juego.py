import pygame
import random

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tigre Saltando Árboles")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
green = (34, 139, 34)
orange = (255, 165, 0)
dark_orange = (255, 140, 0)

# Configuración del tigre
tiger_x = 100
tiger_y = screen_height - 100
tiger_width = 50
tiger_height = 30
tiger_jump = False
jump_height = 10
jump_count = 10

# Configuración del árbol
tree_width = 70
tree_height = 120
tree_x = screen_width
tree_y = screen_height - tree_height

# Velocidad del juego
speed = 5

# Puntuación
score = 0
font = pygame.font.SysFont(None, 35)

# Función para mostrar la puntuación
def show_score(x, y, score):
    score_display = font.render("Puntuación: " + str(score), True, black)
    screen.blit(score_display, (x, y))

# Función para dibujar el tigre
def draw_tiger(x, y):
    # Cuerpo del tigre (rectángulo)
    pygame.draw.rect(screen, orange, [x, y, tiger_width, tiger_height])
    # Cabeza del tigre (círculo)
    pygame.draw.circle(screen, dark_orange, (x + tiger_width - 10, y + 10), 15)
    # Pata delantera
    pygame.draw.rect(screen, dark_orange, [x + 10, y + tiger_height - 10, 10, 10])
    # Pata trasera
    pygame.draw.rect(screen, dark_orange, [x + 30, y + tiger_height - 10, 10, 10])
    
# Bucle principal del juego
running = True
while running:
    pygame.time.delay(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Movimiento del tigre
    keys = pygame.key.get_pressed()
    
    if not tiger_jump:
        if keys[pygame.K_SPACE]:
            tiger_jump = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            tiger_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            tiger_jump = False
            jump_count = 10
    
    # Movimiento del árbol
    tree_x -= speed
    if tree_x < -tree_width:
        tree_x = screen_width
        score += 1
    
    # Colisión
    if tree_x < tiger_x + tiger_width < tree_x + tree_width and tiger_y + tiger_height > tree_y:
        running = False  # Fin del juego si hay colisión
    
    # Dibujar en la pantalla
    screen.fill(white)
    pygame.draw.rect(screen, green, [tree_x, tree_y, tree_width, tree_height])
    draw_tiger(tiger_x, tiger_y)
    show_score(10, 10, score)
    
    pygame.display.update()

# Finalizar pygame
pygame.quit()
