from random import randint
import time
from Klass import Klass
from Student import Student
from Reason import Reason



def main():

    command = ""
    count = 0
    while command != "exit":
        if count%4 == 0:
                command = input("Say 1 or 2 for managing classes\nSay 3 or 4 for managing students\n5 checks in students, 6 checks them out\
                                \n7 to log into class and 8 to log out\nSay 9 to list Classes or 0 to list Students: " )
        else:
                command = input("Enter 0-9 accordingly (Enter exit to exit)>")

        if command == "1":
                Klass.add_class()
        elif command == "2":
                Klass.remove_class()
        elif command == "3":
                Student.add_student()
        elif command == "4":
                Student.remove_student()
        elif command == "5":
                Student.checkIn()
        elif command == "6":
                Reason.checkOut()
        elif command == "7":
                Klass.log_in()
        elif command == "8":
                Klass.log_out()
                #Student.autocheckout()
        elif command == "9":
                Klass.list_classes()
        elif command == "0":
                Student.list_students()
        count += 1
                    
    exit()



if __name__ == '__main__':
    main()
