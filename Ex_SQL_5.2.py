import sqlite3

database = sqlite3.connect('sqlite-db/northwind.db')
database.text_factory = lambda x: x.decode('latin-1')

cur = database.cursor()

cur.execute("""SELECT COUNT(*), CustomerALFKI.OrderID, CustomerALFKI.CustomerID FROM 
            ( SELECT * FROM Orders WHERE CustomerID = 'ALFKI' ) CustomerALFKI 
            INNER JOIN 'Order Details' od
            on CustomerALFKI.OrderID = od.OrderID
            INNER JOIN 'Products' pd
            on od.ProductID = pd.ProductID
            GROUP BY od.OrderID
            HAVING COUNT(*) > 1""")

rows = cur.fetchall()

for row in rows:
	print(row[0])
