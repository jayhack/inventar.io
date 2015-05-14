import sqlite3

if __name__ == '__main__':

	#=====[ Step 1: connect	]=====
	conn = sqlite3.connect('/home/jayhack/inventar.io')
	c = conn.cursor()

	#=====[ Step 2: clear	]=====
	c.execute('''DROP TABLE IF EXISTS quiero_submissions''')
	c.execute('''DROP TABLE IF EXISTS tengo_submissions''')
	conn.commit()

	#=====[ Step 3: create tables	]=====
	c.execute('''CREATE TABLE quiero_submissions
				(id INT, sender TEXT, item TEXT, date TEXT)''')
	c.execute('''CREATE TABLE tengo_submissions
				(id INT, sender TEXT, item TEXT, qty INT, price REAL, date TEXT)''')
	conn.commit()

	#=====[ Step 4: close	]=====
	conn.close()