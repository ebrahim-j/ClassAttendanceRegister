import sqlite3

conn = sqlite3.connect('ClassAttendance.db')
c = conn.cursor()

def create_tables():
	c.execute('CREATE TABLE IF NOT EXISTS students(id INTEGER, name TEXT, age INTEGER, )') #check this to complete
	c.execute('CREATE TABLE IF NOT EXISTS classes(id INTEGER, name TEXT, duration TEXT, )') #check this to complete
	c.execute('CREATE TABLE IF NOT EXISTS attendance()') #check this to complete
	
	
def dynamic_data_entry():
	id = #something
	name = input("Name: ")
	age = #rethink this
	c.execute('INSERT INTO ClassAttendance (id, name, age) VALUES(?, ?, ?, ?)',
	 (id, name, age))
	conn.commit()
	
