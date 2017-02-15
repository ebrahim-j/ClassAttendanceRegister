class Class():

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
        while id in class_id or id == 0:
            id = randint(100,999)
        class_id.append(id)
        new_class = Class(id, name, start, stop, status)
        classes[id] = new_class
        print("Done Successfully!\nYour class ID is: ", id)
            
            
    def remove_class():
        ask = int(input("Which class do you want to remove? "))
        if ask in classes:
            del classes[ask]
            print("Deleted!")
        else:
            print("This class was not in our system anyway!")

    def log_in():
        ask = int(input("Enter class ID to log in: ")) #what if already logged in???
        localtime = time.localtime()
        logTime = time.strftime("%d-%b-%Y %r", localtime)
        classes[ask].start = logTime
        classes[ask].status = "Class in session"
        print("Logged in Successfully")
            
                            
    def log_out(): 
        ask = int(input("Enter class Id to be logged out: "))
        localtime = time.localtime()
        logTime = time.strftime("%d-%b-%Y %r", localtime)
        classes[ask].stop = logTime
        classes[ask].status = "Not in session"
        print("Logged out Successfully")

    def list_classes():
        for key in classes:
            tally = Student.students_in_class(key)
            print ("{} - {}", classes[key].name, tally)

