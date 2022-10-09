import pandas as pd
import sqlite3
from IPython.display import display
con = sqlite3.connect('teste.db')
cur = con.cursor()
cur.execute("SELECT * FROM movie")
resultados = cur.fetchall()
resultados = pd.DataFrame(resultados)
display(resultados)
