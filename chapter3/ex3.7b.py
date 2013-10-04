#http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?apikey=q5e9vhsgtsbqbwbka76pf5g4
import json, requests, sqlite3

YOUR_OWN_KEY = 'q5e9vhsgtsbqbwbka76pf5g4'
#url = requests.get("http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?apikey=%s", % ())

url = requests.get("http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?apikey=%s" %(YOUR_OWN_KEY,))

binary = url.content

output = json.loads(binary)

movies = output["movies"]

with sqlite3.connect("movies.db") as connection:
	c = connection.cursor()

	for movie in movies:
		c.execute("INSERT INTO new_movies VALUES(?, ?, ?, ?, ?, ?, ?)", (movie["title"], movie["year"], movie["mpaa_rating"], movie["release_dates"]["theater"], movie["runtime"], movie["ratings"]["critics_score"], movie["ratings"]["audience_score"]))

	c.execute("SELECT * FROM new_movies ORDER BY title ASC")
	rows = c.fetchall()

	for r in rows:
		print r[0], r[1], r[3], r[4], r[5], r[6]
