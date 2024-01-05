import pygame

# Define draw_2D function outside the game loop
def draw_2D(screen, cube):
    """
          0
        1 2 3 4
          5
    """

    draw_3x3(200,200,cube[0],screen,20)
    draw_3x3(125,275,cube[1],screen,20)
    draw_3x3(200,275,cube[2],screen,20)
    draw_3x3(275,275,cube[3],screen,20)
    draw_3x3(350,275,cube[4],screen,20)
    draw_3x3(200,350,cube[5],screen,20)






def draw_3x3(x, y, face, screen, size):
    """
    Draws a 3x3 square representing
    a side given the top left x and y
    coord and the face array
    """
    color_map = {
        0: (255, 255, 255),  # white
        1: (0, 128, 0),      # green
        2: (255, 0, 0),      # red
        3: (0, 0, 255),      # blue
        4: (255, 165, 0),    # orange
        5: (255, 255, 0)     # yellow
    }

    curr_x = x
    x_count = 0
    for tiles in range(9):
        pygame.draw.rect(screen, color_map[face[tiles][0]], pygame.Rect(curr_x, y, size, size))
        curr_x += size + 5
        x_count += 1

        if x_count == 3:  # End of current row, reset for new row
            curr_x = x
            y += size + 5
            x_count = 0
