# controller.py
import pygame
import time
from cube import RubiksCube
from visual import draw_2D

def main():
    # Initialize Pygame and create a screen
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    # Create a new Rubik's Cube instance
    rubiks_cube = RubiksCube()

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill the screen with black background
        draw_2D(screen, rubiks_cube.cube)  # Draw the cube

        pygame.display.flip()
        clock.tick(60)

        time.sleep(3)
        rubiks_cube.verticle_turn(0,False)
        draw_2D(screen,rubiks_cube.cube)
        

    pygame.quit()

if __name__ == "__main__":
    main()
