from Student import Student
from Klass import Klass
from dbManager import student_check_out

class Reason():

    reasons = {}

    def __init__(self, student_id, class_id, reason):
        self.student_id = student_id
        self.class_id = class_id
        self.reason = reason
                                    
                                    
    def checkOut(st_id, cl_id, reason):
        st_id = int(st_id)
        cl_id = int(cl_id)
        
        new_reason = Reason(st_id, cl_id, reason) 
        Reason.reasons[reason] = new_reason
        student_check_out(st_id, cl_id, reason)
