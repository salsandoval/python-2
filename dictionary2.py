Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> wars_dictionary = {'fname': 'Luke':, 'lname': 'Skywalker', 'Home': 'Earth'}
SyntaxError: invalid syntax
>>> wars_dictionary = {'fname': 'Luke', 'lname': 'Skywalker', 'Home': 'Earth'}
>>> x = wars_dictionary.values()
>>> print(x)
dict_values(['Luke', 'Skywalker', 'Earth'])
>>> wars_dictionary['Earth'] = mundo
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    wars_dictionary['Earth'] = mundo
NameError: name 'mundo' is not defined
>>> wars_dictionary['Earth'] = 'mundo'
>>> print(wars_dictionary)
{'fname': 'Luke', 'lname': 'Skywalker', 'Home': 'Earth', 'Earth': 'mundo'}
>>> wars_dictionary.update({'level': 'jedi'})
>>> print(wars_dictionary)
{'fname': 'Luke', 'lname': 'Skywalker', 'Home': 'Earth', 'Earth': 'mundo', 'level': 'jedi'}
>>> mykids = {
	"Kid1" : {
	  "name" : "Isaak",
	  "level" : "14"
	},
	"Kid2" : {
	  "name" : "Makai",
	  "Level" : "12",
	},
	"Kid3" : {
	  "name" : "Hazel",
	  "Level" : "7",
	}
       }
>>> print(mykids)
{'Kid1': {'name': 'Isaak', 'level': '14'}, 'Kid2': {'name': 'Makai', 'Level': '12'}, 'Kid3': {'name': 'Hazel', 'Level': '7'}}
>>> 
>>> 
>>> x = ('key1', 'key2', 'key3')
>>> y = 0
>>> mydict = dict.fromkeys(x, y)
>>> print(mydict)
{'key1': 0, 'key2': 0, 'key3': 0}
>>> cars = ['Dodeg', 'Viper', 'Mustang', 'Nissan', 'Honda']
>>> 