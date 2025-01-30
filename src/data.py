import sqlite3


class DataBase:
    def __init__(self, db_file):  # init database file
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        
    def getUserByName(self, user_name: str = None):  # get user by name
        with self.connection:
            return self.cursor.execute("SELECT * FROM users WHERE name = ?", (user_name,)).fetchall()
        
    def getAllNames(self):  # get all users
        with self.connection:
            return self.cursor.execute("SELECT name FROM users").fetchall()