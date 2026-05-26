import json
import sqlite3

DB_NAME = "mjb.db"

"""
Stores the 8 realm puzzles from blue prince
Key = name (The associate country)
Element = (Board Layout , Solution) 
"""
DEFAULT_BOARD_SIZE = 3
REALM_PUZZLES = {
    "ORINDA ARIES": ([["GREEEN","BLACK","GREEN"],["BLACK","BLACK","BLACK"],["GREEN","YELLOW","GREEN"]],
                     ["BLACK"] * 4, DEFAULT_BOARD_SIZE),
    "FENN ARIES": ([["GREY","GREEN","GREY"],["ORANGE","RED","ORANGE"],["WHITE","GREEN","BLACK"]],
                   ["RED"] * 4, DEFAULT_BOARD_SIZE),
    "ARCH ARIES": ([["BLACK","YELLOW","GREY"],["YELLOW","GREEN","YELLOW"],["GREY","YELLOW","BLACK"]],
                   ["YELLOW"] * 4, DEFAULT_BOARD_SIZE),
    "ERAJA ARIES": ([["YELLOW","PURPLE","YELLOW"],["GREEN","RED","BLACK"],["PURPLE","PURPLE","PURPLE"]],
                    ["PURPLE"] * 4, DEFAULT_BOARD_SIZE),
    "Corarica": ([["ORANGE","BLACK","ORANGE"],["ORANGE","ORANGE","ORANGE"],["PURPLE","GREEN","PRURPLE"]],
                 ["ORANGE"] * 4,DEFAULT_BOARD_SIZE),
    "Mora Jai": ([["YELLOW","YELLOW","YELLOW"],["WHITE","PINK","WHITE"],["GREY","GREY","WHITE"]],
                 ["WHITE"] * 4, DEFAULT_BOARD_SIZE),
    "Verra": ([["PINK","PINK","GREY"],["GREY","GREY","GREY"],["ORANGE","ORANGE","ORANGE"]],
              ["PINK"] * 4,DEFAULT_BOARD_SIZE),
    "NUANCE": ([["GREEN","GREY","GREEN"],["GREY","ORANGE","ORANGE"],["GREY","BLACK","PURPLE"]],
               ["GREEN"] * 4, DEFAULT_BOARD_SIZE),
}

"""
Function to print the board database for testing and verification purposes
"""
def print_boards():
    pass

"""
Creates the initial database if there is none, or the database is empty
The initial database contains the 8 boards for the 8 realm puzzles in blue prince
"""
def init_database():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS boards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            board_name TEXT NOT NULL,
            board_layout TEXT NOT NULL,
            board_solution TEXT NOT NULL,
            board_size INTEGER NOT NULL,
            )
        '''
        )
        conn.commit()

        cursor.execute("SELECT * FROM boards")
        count = cursor.fetchone()[0]

        initial_boards =  [
            (name, json.dumps(board), json.dumps(solution), size)
            for name, (board, solution, size) in REALM_PUZZLES.items()
        ]

        cursor.executemany(
            """INSERT INTO boards (board_name, board_layout, board_solution, board_size) VALUES (?, ?, ?)""",
            initial_boards,
        )
        conn.commit()
