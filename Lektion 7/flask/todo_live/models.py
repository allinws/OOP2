import sqlite3


class Schema:

    def __init__(self):
        self.conn = sqlite3.connect('todo.sqlite')
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


class UserModel:
    TABLENAME = "User"

    def __init__(self):
        self.conn = sqlite3.connect('todo.sqlite')
        self.conn.row_factory = sqlite3.Row # Convert tuples to objects when we fetch data from the db

    def create(self, name, email):
        with self.conn:
            self.conn.execute(f"INSERT INTO {self.TABLENAME} (name, email) VALUES (?, ?)", (name, email))
            row = self.conn.execute("SELECT * FROM {} WHERE rowid = last_insert_rowid()".format(self.TABLENAME)).fetchone()
            return dict(row)