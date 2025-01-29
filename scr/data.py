import sqlite3


class DataBase:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        
    def getUserByName(self, user_name: str | None = None):
        with self.connection:
            if user_name:
                return self.cursor.execute("SELECT * FROM users WHERE name = ?", (user_name,)).fetchall()
            return self.cursor.execute("SELECT * FROM users").fetchall()
