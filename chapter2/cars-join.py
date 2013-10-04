import sqlite3

with sqlite3.connect("cars.db") as connection:
     c = connection.cursor()

     c.execute("""SELECT inventory.make, inventory.model, inventory.quantity, orders.order_date
                         FROM inventory INNER JOIN orders
                         ON inventory.make = orders.make AND inventory.model = orders.model
                         ORDER BY inventory.make ASC""")

     rows = c.fetchall()

     for r in rows:
          print "Make - Model: " + r[0] + " - " + r[1]
          print "Quantity: " + str(r[2])
          print "Order date: " + r[3]
          print