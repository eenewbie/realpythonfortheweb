import csv
import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	orders = csv.reader(open("orders.csv", "rU"))

	c.executemany("INSERT INTO orders(make, model, order_date) VALUES(?, ?, ?)", orders)