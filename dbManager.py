import sqlite3
import time
import datetime

conn = sqlite3.connect('Ebrahim.db') #change name



def add_to_student(st_id, name, status):
	conn.execute("INSERT INTO student VALUES (?,?,?)", [st_id, name, status]) 
	conn.commit()

def add_to_class(cl_id, name, start, stop, status):
	conn.execute("INSERT INTO class VALUES (?,?,?,?,?)", [cl_id, name, start, stop, status]) 
	conn.commit()

def remove_from_student(st_id):
	conn.execute("DELETE FROM student WHERE ID=?", (st_id,))
	conn.commit()

def remove_from_class(cl_id):
	conn.execute("DELETE FROM class WHERE ID=?", (cl_id,))
	conn.commit()

def log_into_class():
	ask = int(input("Enter class ID to log in: "))
	status = conn.execute("SELECT STATUS FROM class WHERE ID=?", (ask,))
	result = ""
	for row in status:
		result =row[0]
	
	if result == 'Not in session':
		conn.execute("UPDATE class set STATUS='Class in session' WHERE ID=?", (ask,))
		logTime = str(datetime.datetime.now().replace(microsecond=0))
		conn.execute("UPDATE class SET START='" +logTime +"' WHERE ID=?", (ask,))
		conn.commit()
		print("Logged in Successfully at :", logTime)
	elif result == 'Class in session':
		print('Class already logged in!')
		
def log_out_class():
	ask = int(input("Enter class ID to log out: "))
	status = conn.execute("SELECT STATUS FROM class WHERE ID=?", (ask,))
	result = ""
	for row in status:
		result =row[0]
		
	if result == 'Not in session':
		print('Class already logged in!')
		
	elif result == "Class in session":
		conn.execute("UPDATE class set STATUS='Not in session' WHERE ID=?", (ask,))
		#localtime = time.localtime()
		#logTime = time.strftime("%d-%b-%Y %H:%M:%S", localtime)
		logTime = str(datetime.datetime.now().replace(microsecond=0))
		conn.execute("UPDATE class SET STOP='" +logTime +"' WHERE ID=?", (ask,))
		#conn.execute("UPDATE student SET STATUS='" +output +"' WHERE ")
		conn.commit()
		print("Logged out Successfully at :", logTime)
		
def student_check_in(st_id, cl_id):
	start = conn.execute("SELECT START FROM class WHERE ID=?", (cl_id, ))
	status = conn.execute("SELECT STATUS FROM student WHERE ID=?", (st_id, ))
	output = ""
	for row in status:
		output = row[0]
	result = ""
	for row in start:
		result = row[0]
		try:
			result = datetime.datetime.strptime(result, "%d-%b-%Y %H:%M:%S")
		except:
			print("Class not in session yet")
			return
	stop = conn.execute("SELECT STOP FROM class WHERE ID=?", (cl_id, ))
	result2 = ""
	for row in stop:
		result2 = row[0]
		result2 = datetime.datetime.strptime(result2, "%d-%b-%Y %H:%M:%S")

	if result < result2:
		print ("Class not in session yet")
	elif output == "In class":
		print("Student already checked in to a class.")
	else:
		new_status = "In class"
		conn.execute("UPDATE student SET STATUS='" +new_status +"'WHERE ID=?", (st_id, ))
		conn.commit()
		print("Checked in Successfully!")
	
def student_check_out(st_id, cl_id, reason):

	st_status = conn.execute("SELECT STATUS FROM student WHERE ID=?", (st_id, ))
	cl_status = conn.execute("SELECT STATUS FROM class WHERE ID=?", (cl_id, ))

	result1 = ""
	for row in cl_status:
		result1 = row[0]
	if result1 == "Not in session":
		print("Retry, class not in session")
	result = ""
	for row in st_status:
		result = row[0]
	if result == "Not in class":
		print("This student has not been checked in")
	elif result == "In class":
		new_status = "Not in class"
		conn.execute("UPDATE student SET STATUS='" +new_status +"' WHERE ID=?", (st_id, ))
		conn.commit()
		print("Student checked out due to: " + reason)
		
def list_all_students():
	the_list = conn.execute("SELECT NAME,STATUS FROM student GROUP BY NAME")
	for row in the_list:
		print (row)

def list_all_classes():
	the_list = conn.execute("SELECT NAME,STATUS FROM classes GROUP BY NAME")
	