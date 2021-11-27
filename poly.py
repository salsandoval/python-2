# Create two classes that inherit from another class.



class User:
    name = 'unknown'
    email = 'unknown'
    password = 'unknown'

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

# The parent class should have at least one method (function).

       
    def greeting(self):
        msg = "Hello there {} !".format(self.name)
        return msg

        
# Both child classes should utilize polymorphism on the parent class method. 
#Each child should have at least two of their own attributes. 
        
class Employee(User):   
    base_pay = 15.00
    department = 'retail'

        
class Customer(User):
    mailing_address = ''
    mailing_list = True


# assign values to all of the attributes from the user class

if __name__ == "__main__":
    newUser = User('Mark', 'mark@gmail.com', '123abc')
    print(newUser.name, newUser.email, newUser.password)
    print(newUser.greeting())

