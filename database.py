import json
import sqlite3

DB_NAME = "mjb.db"

"""
Stores the 8 realm puzzles from blue prince
Key = name (The associate country)
Element = (Board Layout , Solution) 
"""
REALM_PUZZLES = {
    "ORINDA ARIES": ([["GREEEN","BLACK","GREEN"],["BLACK","BLACK","BLACK"],["GREEN","YELLOW","GREEN"]],
                     ["BLACK"] * 4),
    "FENN ARIES": ([["GREY","GREEN","GREY"],["ORANGE","RED","ORANGE"],["WHITE","GREEN","BLACK"]],
                   ["RED"] * 4),
    "ARCH ARIES": ([["BLACK","YELLOW","GREY"],["YELLOW","GREEN","YELLOW"],["GREY","YELLOW","BLACK"]],
                   ["YELLOW"] * 4),
    "ERAJA ARIES": ([["YELLOW","PURPLE","YELLOW"],["GREEN","RED","BLACK"],["PURPLE","PURPLE","PURPLE"]],
                    ["PURPLE"] * 4),
    "Corarica": ([["ORANGE","BLACK","ORANGE"],["ORANGE","ORANGE","ORANGE"],["PURPLE","GREEN","PRURPLE"]],
                 ["ORANGE"] * 4),
    "Mora Jai": ([["YELLOW","YELLOW","YELLOW"],["WHITE","PINK","WHITE"],["GREY","GREY","WHITE"]],
                 ["WHITE"] * 4),
    "Verra": ([["PINK","PINK","GREY"],["GREY","GREY","GREY"],["ORANGE","ORANGE","ORANGE"]],
              ["PINK"] * 4),
    "NUANCE": ([["GREEN","GREY","GREEN"],["GREY","ORANGE","ORANGE"],["GREY","BLACK","PURPLE"]],
               ["GREEN"] * 4),
}

"""
Funciton to print the board database for testing and verification purposes
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
            )
        '''
        )
        conn.commit()

        cursor.execute("SELECT * FROM boards")
        count = cursor.fetchone()[0]

        initial_boards =  [
            (name, json.dumps(board), json.dumps(solution))
            for name, board, solution in REALM_PUZZLES.items()
        ]

        cursor.executemany(
            """INSERT INTO boards (board_name, board_layout, board_solution) VALUES (?, ?, ?)""",
            initial_boards,
        )
        conn.commit()
