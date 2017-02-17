from Student import Student
from Klass import Klass
from dbManager import student_check_out

class Reason():

    reasons = {}

    def __init__(self, student_id, class_id, reason):
        self.student_id = student_id
        self.class_id = class_id
        self.reason = reason
                                    
                                    
    def checkOut():
        cl_id = int(input("Which class to check out of(By ID please)? "))
        st_id = int(input("Which student(By ID please)?" ))	
        reason = input("Kindly state reason: ")
        
        new_reason = Reason(st_id, cl_id, reason) 
        Reason.reasons[reason] = new_reason
        student_check_out(st_id, cl_id, reason)
