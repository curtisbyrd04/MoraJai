"""
color_functions.py

File for all the function helpers for the colored tiles
There is no function for grey because it does nothing
Blue is handled directly in the mora jai function
"""

import mj_board as mjb

"""
    Handler for orange tile movement
    Changes color to match the majority of the tiles around it
"""
def orange_action(cur_board, cur_button, wildcard=False):
    adjacent_colors = []
    freq_dict = {}
    max_freq = -1
    solution_color = []
    for col in range(len(cur_board)):
        for row in range(len(cur_board[col])):
            if (abs(col - cur_button.position[0]) == 1) and (abs(row - cur_button.position[1]) == 0):
                adjacent_colors.append(cur_board[col][row].color)
            elif (abs(col - cur_button.position[0]) == 0) and (abs(row - cur_button.position[1]) == 1):
                adjacent_colors.append(cur_board[col][row].color)
    for color in adjacent_colors:
        if color not in freq_dict.keys():
            freq_dict[color] = 1
        else:
            freq_dict[color] += 1
    for color in freq_dict.keys():
        if len(solution_color) == 0:
            solution_color.append(color)
            max_freq = freq_dict[color]
        elif freq_dict[color] > max_freq:
            solution_color.clear()
            solution_color.append(color)
        elif freq_dict[color] == max_freq:
            solution_color.append(color)
    if (len(solution_color) == 1):
        cur_button.color = solution_color[0]
    else:
        pass
"""
    Handler for green tile movement
    Swaps positions with the tile opposite to it (does nothing while in the center)
"""
def green_action(cur_board, cur_button, wildcard=False):
    # the number 2 here is used because that's the maximum index of a 3x3 grid, 0,1,2
    ref_position = (abs(cur_button.position[0] - 2), abs(cur_button.position[1] - 2))
    temp_color = cur_board[ref_position[0]][ref_position[1]].color
    cur_button.color = temp_color
    if wildcard:
        cur_board[ref_position[0]][ref_position[1]].color = mjb.color_dict['BLUE']
    else:
        cur_board[ref_position[0]][ref_position[1]].color = mjb.color_dict['GREEN']

"""
    Handler for pink tile movement
    Rotates the surrounding tiles counter clockwise
"""
def pink_action(cur_board, cur_button, wildcard=False):
    #Still have to think of the best way to implement pink
    pass

"""
    Handler for green tile movement
    Moves everything in the current row to the right (wrapping around the edge)
"""
def black_action(cur_board, cur_button, wildcard=False):
    cur_row_val = cur_button.position[1]
    temp_row = [None] * 3
    for i in range(len(cur_board)):
        temp_row[(i + 1) % 3] = cur_board[i][cur_row_val].color
    for i in range(len(cur_board)):
        cur_board[i][cur_row_val].color = temp_row[i]

"""
    Handler for white tile movement
    Turns it's self and all orthogonally adjacent tiles of the same color grey.
    Turns all grey orthogonally adjacent tiles to match this tile
"""
def white_action(cur_board, cur_button, wildcard=False):
    greylist = []
    cur_color_list = []
    for col in range(len(cur_board)):
        for row in range(len(cur_board[col])):
            if (abs(col - cur_button.position[0]) == 1) and (abs(row - cur_button.position[1]) == 0):
                if cur_board[col][row].color == mjb.color_dict['GREY']:
                    greylist.append(cur_board[col][row])
                elif cur_board[col][row].color == cur_button.color:
                    cur_color_list.append(cur_board[col][row])
            elif (abs(col - cur_button.position[0]) == 0) and (abs(row - cur_button.position[1]) == 1):
                if cur_board[col][row].color == mjb.color_dict['GREY']:
                    greylist.append(cur_board[col][row])
                elif cur_board[col][row].color == cur_button.color:
                    cur_color_list.append(cur_board[col][row])
    for i in range(len(greylist)):
        greylist[i].color = cur_button.color
    for i in range(len(cur_color_list)):
        cur_color_list[i].color = mjb.color_dict['GREY']
    cur_button.color = mjb.color_dict['GREY']

"""
    Handler for red tile movement
    Turns all white tiles black, and all black tiles red
"""
def red_action(cur_board, cur_button, wildcard=False):
    for col in range(len(cur_board)):
        for row in range(len(cur_board[col])):
            if cur_board[col][row].color == mjb.color_dict['BLACK']:
                cur_board[col][row].color = cur_button.color
            elif cur_board[col][row].color == mjb.color_dict['GREY']:
                cur_board[col][row].color = mjb.color_dict['BLACK']

"""
    Handler for yellow tile movement
    Moves upward swapping places with the tile above it
"""
def yellow_action(cur_board, cur_button, wildcard=False):
    cur_button.color = cur_board[cur_button.position[0]][cur_button.position[1] - 1].color
    if wildcard:
        cur_board[cur_button.position[0]][cur_button.position[1] - 1].color = mjb.color_dict['BLUE']
    else:
        cur_board[cur_button.position[0]][cur_button.position[1] - 1].color = mjb.color_dict['YELLOW']

"""
    Handler for purple tile movement
    Moves downward swapping places with the tile below it
"""
def purple_action(cur_board, cur_button, wildcard=False):
    cur_button.color = cur_board[cur_button.position[0]][cur_button.position[1] + 1].color
    if wildcard:
        cur_board[cur_button.position[0]][cur_button.position[1] + 1].color = mjb.color_dict['BLUE']
    else:
        cur_board[cur_button.position[0]][cur_button.position[1] + 1].color = mjb.color_dict['PURPLE']