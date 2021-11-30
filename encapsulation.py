

# create class
class safe:
    def __init__(self):
        self._protectVar = 0
        self.__privateVar = 6

    def getprivate(self):
        print(self.__privateVar)

    def setprivate(self, private):
        self.__privateVar = private
        
# get data
obj = safe()
obj.getprivate()
obj.setprivate(14)
obj.getprivate()

                 
                 
