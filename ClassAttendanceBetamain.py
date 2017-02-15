from random import randint
import time
import Class
import Student

class_id = []
student_id = []
classes = {}
students = {}
reasons ={}

def main():

    command = ""

    while command != "exit":
        command = input("Say 1 or 2 for managing classes\nSay 3 or 4 for managing students\n5 checks in students, 6 checks them out\
                        \n7 to log into class and 8 to log out\nSay 9 to list Classes or 0 to list Students: " )
        if command == "1":
                Class.add_class()
        elif command == "2":
                Class.remove_class()
        elif command == "3":
                Student.add_student()
        elif command == "4":
                Student.remove_student()
        elif command == "5":
                Student.checkIn()
        elif command == "6":
                Reason.checkOut()
        elif command == "7":
                Class.log_in()
        elif command == "8":
                Class.log_out()
        elif command == "9":
                Class.list_classes()
        elif command == "0":
                Student.list_students()
                    
    exit()



if __name__ == '__main__':
    main()
