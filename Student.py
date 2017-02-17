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
		
	def add_student():
		name = input("Name of student: ")
		status = "Not in class"
		id = randint(1000,9999)
		while id in Student.student_id or id == 0:
			id = randint(1000,9999)
		Student.student_id.append(id)
		new_student = Student(id, name, status)
		Student.students[id] = new_student
		add_to_student(id, name, status)
		print("Done Successfully!\nNew student ID is: ", id)
		
	def remove_student():
		ask = int(input("Which student do you want to remove? "))
		
		try:
			#del Student.students[ask]
			remove_from_student(ask)
			print("Deleted!")
		except:
			print("This dude was not in the system anyway!")
			
	def checkIn():
		cl_id = int(input("Which class is this btw(By ID please)? ")) #check for class validity

		#if cl_id not in Klass.classes:
		#	print ("This class doesn't exist bro! Try again")

		st_id = int(input("Which student(By ID please)?" ))
		student_check_in(st_id, cl_id)

		"""if st_id not in Student.students:
			print("Who is this dude? We don't know him!")
		else:
			if Student.students[st_id].status == "Not in class": #also check if class is logged in
				Student.students[st_id].status = "In class"
				print("Checked In Successfully!")
			else:
				print("Already checked in to a class")""" #say which class if possible

	def list_students():
		# for key in Student.students:
			# print ("{} - {}".format( Student.students[key].name, Student.students[key].status))
		list_all_students()

	def students_in_class(cl_id):
		count = 0
		for key in Student.students:
			if Student.students[key].status == "In class":
				count += 1
		return count

	"""def in_class():


	def autocheckout(st_id):
		for key in Klass.classes:
			if Klass.classes[key].status == "Class in session":
				for key in Student.students:
					if """
