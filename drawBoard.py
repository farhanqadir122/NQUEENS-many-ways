import time

import pygame
from PIL import Image


# This is used to draw the chess board using pygame given the number of queens and the row positions. The states are
# generated dynamically and the picture is also resized and adjusted according to the board using Image module.
def draw_board(the_board):
    """ Draw a chess board with queens, as determined by the the_board. """

    pygame.init()
    colors = [(255, 255, 255), (0, 0, 0)]  # Set up colors [red, white]

    n = len(the_board)  # This is an NxN chess board.
    surface_sz = 750  # Proposed physical surface size.
    sq_sz = surface_sz // n  # sq_sz is length of a square.
    surface_sz = n * sq_sz  # Adjust to exactly fit n squares.

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))

    queen_size = int(sq_sz * 0.85)

    image = Image.open('queen.png')
    new_image = image.resize((queen_size, queen_size))
    new_image.save('queen2.png')

    image = Image.open('queenb.png')
    new_image = image.resize((queen_size, queen_size))
    new_image.save('queenb2.png')

    queen = pygame.image.load("queen2.png")
    queenb = pygame.image.load("queenb2.png")

    queenOffset = (sq_sz - queen.get_width()) // 2

    while True:

        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        # Draw a fresh background (a blank chess board)
        for row in range(n):  # Draw each row of the board.
            c_index = row % 2  # Alternate starting color
            for col in range(n):  # Run through cols drawing squares
                the_square = (col * sq_sz, row * sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_index], the_square)
                # Now flip the color index for the next square
                c_index = (c_index + 1) % 2

        # Now that squares are drawn, draw the queens.
        for (col, row) in enumerate(the_board):
            if (col + row) % 2 == 0:
                surface.blit(queen, (col * sq_sz + queenOffset, row * sq_sz + queenOffset))
            else:
                surface.blit(queenb, (col * sq_sz + queenOffset, row * sq_sz + queenOffset))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    draw_board([0, 5, 3, 1])
    draw_board([6, 4, 2, 0, 5, 7, 1, 3])
    draw_board([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1])
    draw_board([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9, 20, 12, 1, 11, 9, 15])
