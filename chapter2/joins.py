import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	c.execute("""SELECT population.city, population.population, regions.region 
					FROM population INNER JOIN regions 
					ON population.city = regions.city
					ORDER BY population.city ASC""")

	rows = c.fetchall()

	for r in rows:
		print "City: " + r[0]
		print "Population: " + str(r[1])
		print "Region: " + r[2]
		print