from abc import ABC, abstractmethod
class mortgage(ABC):
    def bill(self, amount):
        print("Your mortgage amount: ",amount)
# function tells us to pass in an argument,
    @abstractmethod
    def payment(self, amount):
        pass

class CheckPayment(mortgage):
#defined how to implement payment function from parent class.
    def payment(self, amount):
        print('Your limit of {} is more than your $500 limit '.format(amount))

obj = CheckPayment()
obj.bill("$1,300")
obj.payment("$1,300")
    
