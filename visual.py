import pygame

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# Define draw_2D function outside the game loop
def draw_2D(cube):
    # Define the position and size of the square
    x, y = 100, 100  # Position of the square
    size = 10  # Size of the square

    # Define the color of the square (RGB)
    color = (255, 0, 0)  # Red

    # Draw the square
    pygame.draw.rect(screen, color, pygame.Rect(x, y, size, size))
    
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    draw_2D()  # Call draw_2D inside the game loop
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
