import sqlite3
import os

db_folder = "db"
if not os.path.exists(db_folder):
    os.makedirs(db_folder)

con = sqlite3.connect(f"{db_folder}/demodb.db")

# con.execute('''CREATE TABLE genres (
#                         id INTEGER PRIMARY KEY,
#                         name TEXT
#                     );''')

# con.execute('''CREATE TABLE directors (
#                         id INTEGER PRIMARY KEY,
#                         name TEXT
#                     );''')

# con.execute('''CREATE TABLE movies (
#                         id INTEGER PRIMARY KEY,
#                         title TEXT,
#                         release_year INTEGER,
#                         genre_id INTEGER,
#                         director_id INTEGER,
#                         FOREIGN KEY (genre_id) REFERENCES genres(id),
#                         FOREIGN KEY (director_id) REFERENCES directors(id)
#                     );''')

con.execute("INSERT INTO genres (name) VALUES ('Action')")
con.execute("INSERT INTO genres (name) VALUES ('Drama')")
con.execute("INSERT INTO genres (name) VALUES ('Comedy')")
con.execute("INSERT INTO genres (name) VALUES ('Sci-Fi')")
    
con.execute("INSERT INTO directors (name) VALUES ('Steven Spielberg')")
con.execute("INSERT INTO directors (name) VALUES ('Christopher Nolan')")
con.execute("INSERT INTO directors (name) VALUES ('Martin Scorsese')")
    
con.execute("INSERT INTO movies (title, release_year, genre_id,director_id) VALUES ('Jurassic Park', 1993, 1, 1)")
con.execute("INSERT INTO movies (title, release_year, genre_id, director_id) VALUES ('Inception', 2010, 4, 2)")
con.execute("INSERT INTO movies (title, release_year, genre_id, director_id) VALUES ('The Wolf of Wall Street', 2013, 2, 3)")
con.execute("INSERT INTO movies (title, release_year, genre_id, director_id) VALUES ('The Dark Knight', 2008, 1, 2)")
con.execute("INSERT INTO movies (title, release_year, genre_id, director_id) VALUES ('E.T.', 1982, 1, 1)")

con.commit()