from random import randint
import time
from Student import Student
from dbManager import add_to_class
from dbManager import remove_from_class
from dbManager import log_into_class
from dbManager import log_out_class

class Klass():

    class_id = [] 
    classes = {}

    def __init__(self, id, name, start, stop, status ):
        self.id = id
        self.name = name
        self.start = start
        self.stop = stop
        self.status = status #1 or 0 when db implimented
            
            
    def add_class():
        name = input("Name of class: ")
        start = None
        stop = None
        status = "Not in session"
        id = randint(100,999) 
        while id in Klass.class_id or id == 0:
            id = randint(100,999)
        Klass.class_id.append(id)
        new_class = Klass(id, name, start, stop, status)
        Klass.classes[id] = new_class
        add_to_class(id, name, start, stop, status)
        print("Done Successfully!\nYour class ID is: ", id)
            
            
    def remove_class():
        ask = int(input("Which class do you want to remove? "))
        try:
            #del Klass.classes[ask]
            remove_from_class(ask)
            print("Deleted!")
        except:
            print("This class was not in our system anyway!")

    def log_in():
	    log_into_class()
                       
    def log_out():
        log_out_class()

    def list_classes():
        for key in Klass.classes:
            tally = Student.students_in_class(key)
            print ("{} - {} student(s) in class - {}".format( Klass.classes[key].name, tally, Klass.classes[key].status))
