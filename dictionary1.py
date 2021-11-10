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
>>> print(num1 + num2)
3.3
>>> num1 = "one"
>>> print(num1 + num2)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(num1 + num2)
TypeError: can only concatenate str (not "float") to str
>>> num1 = "1"
>>> print(num1 + num2)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(num1 + num2)
TypeError: can only concatenate str (not "float") to str
>>> print(int(num1) + num2)
3.1
>>> myList = [2,3,4]
>>> len(myList)
3
>>> for i in myList;
SyntaxError: invalid syntax
>>> for i in myList:
	print(i)

	
2
3
4
>>> myList[2]
4
>>> myList[0]
2
>>> myList.append(5)
>>> for i in myList:
	print(i)

	
2
3
4
5
>>> len(myList)
4
>>> print(myList)
[2, 3, 4, 5]
>>> myDictionary = {' index': 1,: 'index2' 'index3': 355}
SyntaxError: invalid syntax
>>> myDictionary = {'index1': 1, 'index2': 2, 'index3': 355}
>>> myDictionary
{'index1': 1, 'index2': 2, 'index3': 355}
>>> myDictionary['index2']
2
>>> dic_users = {'em_1234': {'fname': 'bob', 'lname': 'smith', 'phone': '123-456-7890'}, 'em_1235':  {'fname':, 'mary', 'lname',: 'jones', 'phone': '152-364-5746'} }
SyntaxError: invalid syntax
>>> dic_users = {'em_1234': {'fname': 'bob', 'lname': 'smith', 'phone': '123-456-7890'}, 'em_1235':  {'fname': 'mary', 'lname',: 'jones', 'phone': '152-364-5746'} }
SyntaxError: invalid syntax
>>> dic_users = {'em_1234': {'fname': 'bob', 'lname': 'smith', 'phone': '123-456-7890'}, 'em_1235':  {'fname': 'mary', 'lname': 'jones', 'phone': '152-364-5746'} }
>>> print(dic_users['em_1235'])
{'fname': 'mary', 'lname': 'jones', 'phone': '152-364-5746'}
>>> print(dic_users['em_1235']['phone'])
152-364-5746
>>> print('User: {}  {} \nphone: {}'.format(dic_users['em_1235']['fname'],dic_users['em_1235']['lname'],dic_users['em_1235']['phone']))
User: mary  jones 
phone: 152-364-5746
>>> 