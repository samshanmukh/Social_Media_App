""" Model file."""

import sqlite3

ROOT = path.dirname(path.relpath((__file__)))


def create_post(name, content):
	# Database connection
	con = sql.connect(path.join(ROOT, 'database.db'))

	# Cursor object to iterate through db
	cur = con.cursor()

	# Insert values into table
	cur.execute('insert into posts (name, content) values(?, ?)', name, content)

	# Closing the connection
	con.commit()
	con.close()

def get_posts():
	# Database connection
	con = sql.connect(path.join(ROOT, 'database.db'))

	# Cursor object to iterate through db
	cur = con.cursor()

	# Getting values from the table
	cur.execute('select * from posts')

	posts = cur.fetchall()

	return posts