import sqlite3
con = sqlite3.connect('teste.db')
cur = con.cursor()
cur.execute("CREATE TABLE movie(title, year, score)")
con.commit()
