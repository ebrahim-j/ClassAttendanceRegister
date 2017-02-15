class Reason():
    def __init__(self, student_id, class_id, reason):
        self.student_id = student_id
        self.class_id = class_id
        self.reason = reason
                                    
                                    
    def checkOut():
        cl_id = int(input("Which class to check out of(By ID please)? "))
        st_id = int(input("Which student(By ID please)?" ))	
        reason = input("Kindly state reason: ")
        
        if st_id not in students:
            print("Who is this dude? We don't know him!")
        elif cl_id not in classes:
            print("Ey bana! This class does not exist!")
        else:
            new_reason = Reason(st_id, cl_id, reason) #try to add a when eg by datetime
            reasons[reason] = new_reason
            students[st_id].status = "Not in class"
            print("{} is allowed to leave!".format(students[st_id].name)) 
