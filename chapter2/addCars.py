import sqlite3

with sqlite3.connect("cars.db") as connection:
	
	c = connection.cursor()
	
	newCars = [ ('Ford', 'FModel01', 100),
				('Ford', 'FModel02', 200),
				('Ford', 'FModel03', 300),
				('Honda', 'HModel01', 400),
				('Honda', 'HModel02', 500)]

	c.executemany('INSERT INTO inventory VALUES(?, ?, ?)', newCars)
	
