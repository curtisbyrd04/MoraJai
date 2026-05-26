"""
main.py

Main file for running the screen through pygame and processing user input
"""

import pygame
import sys
import database as db
import color_functions as cf
import mj_board as mjb


pygame.init()

#Screen Width and Height
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

"""
    Creates the board and sets it's initial values
"""
def init_board(board):
    button_x = WIDTH/3
    button_y = HEIGHT/3
    button_width = 100
    button_height = 100
    for row in range(len(board)):
        for col in range(len(board[row])):
            # for the testing of the green function
            board[col][row] = mjb.Button(pygame.Rect(button_x, button_y, 100, 100), mjb.color_dict['GREY'], (col, row))
            button_x += button_width + 10
        button_x -= (button_width + 10) * len(board[row])
        button_y += button_height + 10
    # for the testing the color functions
    # will replace with sql library
    board[1][2].color = mjb.color_dict['ORANGE']
    board[0][2].color = mjb.color_dict['PINK']
    board[0][0].color = mjb.color_dict['BLUE']
    board[2][2].color = mjb.color_dict['PINK']
    board[0][1].color = mjb.color_dict['BLACK']
    board[2][1].color = mjb.color_dict['ORANGE']
    board[1][1].color = mjb.color_dict['PINK']

"""
    Function for displaying the board to the screen
"""
def print_board(board):
    screen.fill((255,255,255))
    for row in range(len(board)):
        for col in range(len(board[row])):
            pygame.draw.rect(screen, board[col][row].color, board[col][row].rect)
            #print(board[col][row].color)
    pygame.display.flip()


"""
    Main game function
    Takes in the board and the clicked tiles and changes the board currently
    Return: None
"""
def morajai(cur_board, cur_button, middle_pos, wildcard=False):
    size = len(cur_board)

    if cur_button.color == mjb.color_dict['BLUE'] and wildcard == False:
        morajai(cur_board, cur_button,  middle_pos, wildcard=True)

    elif (cur_button.color == mjb.color_dict['GREEN']) or (wildcard == True and cur_board[middle_pos][middle_pos].color == mjb.color_dict['GREEN']):
        cf.green_action(cur_board, cur_button, wildcard)

    elif (cur_button.color == mjb.color_dict['BLACK']) or (wildcard == True and cur_board[middle_pos][middle_pos].color == mjb.color_dict['BLACK']):
        cf.black_action(cur_board, cur_button, wildcard)

    elif (cur_button.color == mjb.color_dict['YELLOW'] and cur_button.position[1] != 0) or (wildcard == True and cur_board[middle_pos][middle_pos].color == mjb.color_dict['YELLOW'] and cur_button.position[1] != 0) :
        cf.yellow_action(cur_board, cur_button, wildcard)

    elif (cur_button.color == mjb.color_dict['PURPLE'] and cur_button.position[1] != size - 1) or (wildcard == True and cur_board[middle_pos][middle_pos].color == mjb.color_dict['PURPLE'] and cur_button.position[1] != size - 1):
        cf.purple_action(cur_board, cur_button, wildcard)

    elif (cur_button.color == mjb.color_dict['RED']) or (wildcard == True and cur_board[middle_pos][middle_pos].color == mjb.color_dict['RED']):
        cf.red_action(cur_board, cur_button, wildcard)

    elif (cur_button.color == mjb.color_dict['WHITE'] or (wildcard == True and cur_board[middle_pos][middle_pos].color == mjb.color_dict['WHITE'])):
        cf.white_action(cur_board, cur_button, wildcard)

    elif (cur_button.color == mjb.color_dict['ORANGE'] or (wildcard == True and cur_board[middle_pos][middle_pos].color == mjb.color_dict['ORANGE'])):
        cf.orange_action(cur_board, cur_button, wildcard)

    elif (cur_button.color == mjb.color_dict['PINK'] or (wildcard and cur_board[middle_pos][middle_pos].color == mjb.color_dict['PINK'])):
        cf.pink_action(cur_board, cur_button, wildcard)


def main():
    mj_board = mjb.Board(3,3)
    init_board(mj_board.grid)
    running = True
    while running:
        print_board(mj_board.grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for col in range(len(mj_board.grid)):
                    for row in range(len(mj_board.grid[col])):
                        if mj_board.grid[col][row].rect.collidepoint(mouse_pos):
                            #assume the button isn't blue
                            morajai(mj_board.grid, mj_board.grid[col][row], mj_board.middle_pos)
                            print_board(mj_board.grid)
    sys.exit()

if __name__ == '__main__':
    main()


