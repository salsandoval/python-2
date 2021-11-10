Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> print(10 + 5)
15
>>> x = 5
>>> x+= 3
>>> print(x)
8
>>> x = 5
>>> y = 3
>>> print(x != y)
True
>>> print(x)> 3 and x < 10)
SyntaxError: unmatched ')'
>>> x = 5
>>> print(x)> 3 and x < 10)
SyntaxError: unmatched ')'
>>> print(x > 3 and x < 10)
True
>>> x = ["apple", "banana"]
>>> y = ["apple", "banana"]
>>> z = x
>>> print(x is z)
True
>>> print("banana in x)
      
SyntaxError: EOL while scanning string literal
>>> print("banana" in x)
True
>>> animal = ( 'zebra', 'alligator', 'giraffe', 'goat', 'ox' )
>>> 
>>> list of Animals = list(animal)
SyntaxError: invalid syntax
>>> listofAnimals = list(animal)
>>> print(listofAnimals)
['zebra', 'alligator', 'giraffe', 'goat', 'ox']
>>> listofAnimals.append ("honey badger")
>>> print(listofAnimals)
['zebra', 'alligator', 'giraffe', 'goat', 'ox', 'honey badger']
>>> myString = "Hello! I am pleased to meet you"
>>> newString = list(myString)
>>> print(newString)
['H', 'e', 'l', 'l', 'o', '!', ' ', 'I', ' ', 'a', 'm', ' ', 'p', 'l', 'e', 'a', 's', 'e', 'd', ' ', 't', 'o', ' ', 'm', 'e', 'e', 't', ' ', 'y', 'o', 'u']
>>> newString = myString.split(" ")
>>> print(newString)
['Hello!', 'I', 'am', 'pleased', 'to', 'meet', 'you']
>>> 
>>> 
>>> thisList = ["sandwich", "burrito", "pasta"]
>>> print(thisList)
['sandwich', 'burrito', 'pasta']
>>> 
>>> for x in thisList:
	print(x)

	
sandwich
burrito
pasta
>>> 
>>> thisList.append("chocolate")
>>> print(thisList)
['sandwich', 'burrito', 'pasta', 'chocolate']
>>> x = thisList.copy()
>>> print(x)
['sandwich', 'burrito', 'pasta', 'chocolate']
>>> list1 = ["A", "B", "C"]
>>> list2 = [1, 2, 3]
>>> list3 = list1 + list2
>>> print(list3)
['A', 'B', 'C', 1, 2, 3]
>>> thisList.reverse()
>>> 
>>> thisList = ["sandwich", "burrito", "pasta"]
>>> thisList.reverse()
>>> print(thisList)
['pasta', 'burrito', 'sandwich']
>>> thistuple = ("poop", "pee", "farts")
>>> print(thistuple)
('poop', 'pee', 'farts')
>>> for x in thistuple
SyntaxError: invalid syntax
>>> thistuple = ("poop", "pee", "farts")
>>> for x in thistuple:
	print x
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> print(x)
['sandwich', 'burrito', 'pasta', 'chocolate']
>>> thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
>>> 
>>> x thistuple.count(5)
SyntaxError: invalid syntax
>>> x thistuple.count(5)
SyntaxError: invalid syntax
>>> thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
>>> x = thistuple.count(5)
>>> print(x)
2
>>> x = thistuple.count(8)
>>> print(x)
2
>>> 