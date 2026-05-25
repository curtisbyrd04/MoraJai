"""
mj_board.py

File that contains all the code and variables for managing the board
"""
color_dict = ({'WHITE': (225, 225, 225), 'BLACK': (0, 0, 0), 'RED': (255, 0, 0), 'BLUE': (0, 0, 255), 'GREEN' : (0, 255, 0),
               'YELLOW' : (255,255,0), 'PURPLE' : (200,0,255), "GREY" : (122,122,122), "ORANGE" : (255, 165, 0), "PINK" : (255, 192, 203), "NULL" : (4,0,4)})

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        #Assuming the board is always going to be a square with an odd width
        self.middle_pos = (width - 1) / 2
        self.grid = [['WHITE' for _ in range(self.width)] for _ in range(self.height)]

class Button:
    def __init__(self, rect, color, position):
        self.rect = rect
        self.color = color
        self.position = position
