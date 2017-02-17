from random import randint
#from Klass import Klass
from dbManager import add_to_student
from dbManager import remove_from_student
from dbManager import student_check_in
from dbManager import list_all_students
# import sqlite3

# conn = sqlite3.connect('Ebrahim.db') #change name
# c = conn.cursor()

class Student():

	student_id = []
	students = {}

	def __init__(self, id, name, status ):
		self.id = id
		self.name = name
		self.status = status
		
	def add_student(name):
		name = str(name)
		status = "Not in class"
		id = randint(1000,9999)
		while id in Student.student_id or id == 0:
			id = randint(1000,9999)
		Student.student_id.append(id)
		new_student = Student(id, name, status)
		Student.students[id] = new_student
		add_to_student(id, name, status)
		print("Done Successfully!\nNew student ID is: ", id)
		
	def remove_student(ask):
	
		ask = int(ask)
		try:
			#del Student.students[ask]
			remove_from_student(ask)
			print("Deleted!")
		except:
			print("This dude was not in the system anyway!")
			
	def checkIn(st_id, cl_id):
		st_id = int(st_id)
		cl_id = int(cl_id)
		student_check_in(st_id, cl_id)


	def list_students():
		list_all_students()
