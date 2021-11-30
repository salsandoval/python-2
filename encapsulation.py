


class safe:
    def __init__(self):
        self._privateVar = 6

    def getprivate(self):
        print(self._privateVar)

    def setprivate(self, private):
        self._privateVar = private

obj = safe()
obj.getprivate()
obj.setprivate(14)
obj.getprivate()

                 
                 
