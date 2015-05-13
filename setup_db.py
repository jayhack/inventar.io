import sqlite3

if __name__ == '__main__':

	#=====[ Step 1: connect	]=====
	conn = sqlite3.connect('inventario.db')
	c = conn.cursor()

	#=====[ Step 2: clear	]=====
	c.execute('''DROP TABLE IF EXISTS requests''')
	c.execute('''DROP TABLE IF EXISTS submissions''')
	conn.commit()

	#=====[ Step 3: create tables	]=====
	c.execute('''CREATE TABLE requests
				(id INT, sender TEXT, item TEXT, date TEXT)''')
	c.execute('''CREATE TABLE submissions
				(id INT, sender TEXT, item TEXT, qty INT, price REAL, date TEXT)''')
	conn.commit()

	#=====[ Step 4: close	]=====
	conn.close()