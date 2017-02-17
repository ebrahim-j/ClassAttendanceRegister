from random import randint
import time
from Student import Student
from dbManager import add_to_class
from dbManager import remove_from_class
from dbManager import log_into_class
from dbManager import log_out_class
from dbManager import list_all_classes

class Klass():

    class_id = [] 
    classes = {}

    def __init__(self, id, name, start, stop, status ):
        self.id = id
        self.name = name
        self.start = start
        self.stop = stop
        self.status = status #1 or 0 when db implimented
            
            
    def add_class(name):
        #name =str(name)
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
            
            
    def remove_class(ask):
        ask = int(ask)
        try:
            #del Klass.classes[ask]
            remove_from_class(ask)
            print("Deleted!")
        except:
            print("This class was not in our system anyway!")

    def log_in(ask):
        ask = int(ask)
        log_into_class(ask)
		
		
    def log_out(ask):
        ask = int(ask)
        log_out_class(ask)
		
    def list_classes():
        list_all_classes()
