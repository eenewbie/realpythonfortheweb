import sqlite3

with sqlite3.connect("cars.db") as connection:
     c = connection.cursor()

     c.execute("SELECT * FROM inventory")

     rows = c.fetchall()

     for r in rows:
          print "Make/Model: " + r[0] + "/" + r[1]
          print "Quantity: " + str(r[2])
          
          sqlString = "SELECT orders.order_date FROM orders WHERE orders.make = '" + r[0] + "' AND orders.model = '" + r[1] + "' ORDER BY orders.order_date ASC"
          #print sqlString
          c.execute(sqlString)
          more_rows = c.fetchall()
          
          for mr in more_rows:
               print mr[0]
          print