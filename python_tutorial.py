#
# Python:    3.9.7
#
# Author:   Sal T. Sandoval
#
# Purpose:  The Tech Academy - Python course, Creating our first program together.
#           Demonstrating how to pass Variables from function to function
#           While producing a functional game.
#
#           Remember, function_name(Variable) _means that we pass in the Variable.
#           return Variable_means that we are returning the Variable to
#           back to the calling function.



def start():
    f_name = "Sarah"
    l_name = "Connor"
    age = 28
    gender = "Female"
    get_info(f_name,l_name,age,gender)



def get_info(f_name,l_name,age,gender):
    print("My name is {} {}. I am {} years old {}.".format(f_name,l_name,age,gender))
   


















if __name__ == "__main__":
    start()
