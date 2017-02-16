from random import randint
import time
from Student import Student


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
        print("Done Successfully!\nYour class ID is: ", id)
            
            
    def remove_class():
        ask = int(input("Which class do you want to remove? "))
        if ask in Klass.classes:
            del Klass.classes[ask]
            print("Deleted!")
        else:
            print("This class was not in our system anyway!")

    def log_in():
        ask = int(input("Enter class ID to log in: ")) 
        if  Klass.classes[ask].status == "Class in session": #what if already logged in???
            print("Class already logged in!")
        else:
            localtime = time.localtime()
            logTime = time.strftime("%d-%b-%Y %H:%M:%S", localtime)
            Klass.classes[ask].start = logTime
            Klass.classes[ask].status = "Class in session"
            print("Logged in Successfully at :", logTime)
            
                            
    def log_out(): 
        ask = int(input("Enter class Id to be logged out: "))
        localtime = time.localtime()
        logTime = time.strftime("%d-%b-%Y %H:%M:%S", localtime)
        Klass.classes[ask].stop = logTime
        Klass.classes[ask].status = "Not in session"

        print("Logged out  at: ", logTime)

    def list_classes():
        for key in Klass.classes:
            tally = Student.students_in_class(key)
            print ("{} - {} student(s) in class - {}".format( Klass.classes[key].name, tally, Klass.classes[key].status))


