class Mexico():
    def capital(self):
        print("Mexico City is the capital of Mexico.")
 
    def language(self):
        print("Spanish is the most widely known language in the world.")
 
    def type(self):
        print("Mexico speaks the language of LOVE.")
 
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
 
    def language(self):
        print("English is the primary language of USA.")
 
    def type(self):
        print("USA is a developed country.")
 
obj_mex = Mexico()
obj_usa = USA()
for country in (obj_mex, obj_usa):
    country.capital()
    country.language()
    country.type()
