import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
     connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO post (title, content) VALUES (?, ?)",
           ('First Post', 'Content for the first post')
           )

cur.execute("INSERT INTO post (title, content) VALUES (?, ?)",
           ('Second Post', 'Content for the Second post')
           )

connection.commit()
connection.close()

