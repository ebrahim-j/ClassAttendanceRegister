import sqlite3

conn = sqlite3.connect('Ebrahim.db') #change name
c = conn.cursor()

c.execute('''CREATE TABLE class
       (ID INTEGER PRIMARY KEY ,
       NAME TEXT,
       START TEXT,
       STOP TEXT,
       STATUS TEXT );''')


c.execute('''CREATE TABLE student
       (ID INTEGER PRIMARY KEY ,
       NAME TEXT,
       STATUS TEXT );''')

c.execute('''CREATE TABLE student_register (
    CLASS_ID INTEGER,
    STUDENT_ID INTEGER,
    FOREIGN KEY(CLASS_ID) REFERENCES class(ID),
    FOREIGN KEY(STUDENT_ID) REFERENCES student(ID)
);''')

conn.close()

