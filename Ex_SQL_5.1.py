import sqlite3

database = sqlite3.connect('sqlite-db/northwind.db')
database.text_factory = lambda x: x.decode('latin-1')

cur = database.cursor()

cur.execute("""SELECT ProductName FROM Products WHERE ProductID in 
			(SELECT ProductID FROM [Order Details] WHERE orderID in 
			(SELECT orderID FROM Orders WHERE CustomerID = 'ALFKI'))""")

rows = cur.fetchall()

for row in rows:
	print(row[0])
