import sqlite3


class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo/todo.db')
        self.create_user_table()
        self.create_to_do_table()

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def create_to_do_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Todo" (
          id INTEGER PRIMARY KEY,
          title TEXT,
          description TEXT,
          is_completed boolean DEFAULT 0,
          created_on Date DEFAULT CURRENT_DATE,
          due_date Date,
          user_id INTEGER FOREIGNKEY REFERENCES User(id)
        );
        """

        self.conn.execute(query)

    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "User" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT,
        created_on Date default CURRENT_DATE
        );
        """
        self.conn.execute(query)