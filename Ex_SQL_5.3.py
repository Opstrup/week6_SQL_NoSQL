import sqlite3

database = sqlite3.connect('sqlite-db/northwind.db')
database.text_factory = lambda x: x.decode('latin-1')

cur = database.cursor()

cur.execute("""SELECT ProductID FROM [Order Details] WHERE Quantity < 2
			   INTERSECT
			   SELECT ProductID FROM Products""")

rows = cur.fetchall()

for row in rows:
	print(row[0])