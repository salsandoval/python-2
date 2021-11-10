Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1 = 1
>>> num2 = 2
>>> 
>>> 
>>> print(num1 + num2)
3
>>> num1 = 1.2
>>> num2 = 2.1
>>> num2 = 2.1
>>> print(num1 + num2)
3.3
>>> myString = "hello world"
>>> myString
'hello world'
>>> len(myString)
11
>>> myString[0]
'h'
>>> myString[1]
'e'
>>> fName = "Daniel'
SyntaxError: EOL while scanning string literal
>>> Fname = "Daniel"
>>> lName = "Christie"
>>> print(fName + lName)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(fName + lName)
NameError: name 'fName' is not defined
>>> print(Fname + lName)
DanielChristie
>>> print(Fname + " " + lName)
Daniel Christie
>>> print("Hello {} {}, welcome to Python!".format(Fname,lName))
Hello Daniel Christie, welcome to Python!
>>> a = "WAZZUUPP!!"
>>> print(a)
WAZZUUPP!!
>>> a = """This is my first try at Python and i think im going"""
>>> print(a)
This is my first try at Python and i think im going
>>> b = "yo, mama!"
>>> print(b[2:5])
, m
>>> myList = ["water", "food", "soda"]
>>> x = len(myList)
>>> print(x)
3
>>> txt = "     tofu     "
>>> x = txt.strip()
>>> print("of all thefood", x, "is my favorite")
of all thefood tofu is my favorite
>>> txt = "Hello im trapper in here"
>>> x = txt.upper()
>>> print(x)
HELLO IM TRAPPER IN HERE
>>> tct = "the water in the tub is crazy cold"
>>> x = "poop" in txt
>>> print(x)
False
>>> x = "sal is "
>>> y = "the best"
>>> z = x + y
>>> print(z)
sal is the best
>>> txt = "Sal is the one we-call \"DA ONE"\"when we game"
SyntaxError: unexpected character after line continuation character
>>> txt = "Sal is the one we-call \"DA ONE\"when we game"
>>> print(txt)
Sal is the one we-call "DA ONE"when we game
>>> 