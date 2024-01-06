# controller.py
import pygame
import time
from cube import RubiksCube
from visual import draw_2D
from scramber import scramble_conversion

def main():
    # Initialize Pygame and create a screen
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    # Create a new Rubik's Cube instance
    rubiks_cube = RubiksCube()

    # Prepare the scramble moves
    moves = scramble_conversion("U2")
    move_index = 0  # Index to track which move we are on
    last_move_time = 0
    move_delay = 1  # Delay in seconds between moves

    # Main game loop
    running = True

    time.sleep(3)
    while running:
        current_time = time.time()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        # Update the cube state if it's time for the next move
        if current_time - last_move_time > move_delay and move_index < len(moves):
            move = moves[move_index]
            prime = move < 0
            move = abs(move)
            #if move == 1:  # L move
                #rubiks_cube.verticle_turn(0, not prime)
            #elif move == 2:  # R move
                #rubiks_cube.verticle_turn(2, prime)
            if move == 3:  # U move
                rubiks_cube.horizontal_turn(0, prime)
            elif move == 4:  # D move
                rubiks_cube.horizontal_turn(2, prime)
            #elif(abs(move) == 5): #B move
                #rubiks_cube.face_turn(0,prime)
            #elif(abs(move) == 6): #F move
                #rubiks_cube.face_turn(0, prime)
            last_move_time = current_time
            move_index += 1
        screen.fill((0, 0, 0))  # Fill the screen with black background
        draw_2D(screen, rubiks_cube.cube)  # Draw the cube

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
