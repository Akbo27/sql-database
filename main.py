import sqlite3
import os

db_folder = "db"
if not os.path.exists(db_folder):
    os.makedirs(db_folder)

con = sqlite3.connect(f"{db_folder}/demodb.db")

con.execute('''CREATE TABLE IF NOT EXISTS genres (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL UNIQUE
                    );''')

con.execute('''CREATE TABLE IF NOT EXISTS directors (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL
                    );''')

con.execute('''CREATE TABLE IF NOT EXISTS movies (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        release_year INTEGER,
                        genre_id INTEGER,
                        director_id INTEGER,
                        FOREIGN KEY (genre_id) REFERENCES genres(id),
                        FOREIGN KEY (director_id) REFERENCES directors(id)
                    );''')


