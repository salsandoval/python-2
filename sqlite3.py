Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> connection = sqlite3.connect(':memory')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    connection = sqlite3.connect(':memory')
NameError: name 'sqlite3' is not defined
>>> import sqlite3
>>> connection = sqlite3.connect(':memory')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    connection = sqlite3.connect(':memory')
sqlite3.OperationalError: unable to open database file
>>> connection = sqlite3.connect("C:/Users/guapo/Desktop/python 2/test_database.db")
>>> connection = sqlite3.connect(':memory')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    connection = sqlite3.connect(':memory')
sqlite3.OperationalError: unable to open database file
>>> c.connection.cursor()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    c.connection.cursor()
NameError: name 'c' is not defined
>>> c = connection.cursor()
>>> connection = sqlite3.connect(':memory')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    connection = sqlite3.connect(':memory')
sqlite3.OperationalError: unable to open database file
>>> connection = sqlite3.connect(':memory:')
>>> c.excute("DROP TABLE IF EXIST people")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    c.excute("DROP TABLE IF EXIST people")
AttributeError: 'sqlite3.Cursor' object has no attribute 'excute'
>>> c.execute("DROP TABLE IF EXIST people")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    c.execute("DROP TABLE IF EXIST people")
sqlite3.OperationalError: near "EXIST": syntax error
>>> c.execute("DROP TABLE IF EXISTS people")
<sqlite3.Cursor object at 0x0000016413D91C70>
>>> connection.close()
>>> with sqlite3.connect("test_databse.db") as connection:
	# perform any SQL operations using connection here
import sqlite3
SyntaxError: expected an indented block
>>> import sqlite3
>>> with sqlite3.connect('test_database.db') as connection:
	c = connection.cursor()
	c.executescript("""DROP TABLE IF EXIST people;
			CREATE TABLE people(FirstName TEXT, LastName TEXT, Age INT);
			INSERT INTO people VALUES('Ron', 'Obvious', '42',);
			""")

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    with sqlite3.connect('test_database.db') as connection:
sqlite3.OperationalError: unable to open database file
>>>  with sqlite3.connect('test_database.db') as connection:
	c = connection.cursor()
	c.executescript("""DROP TABLE IF EXIST people;
			CREATE TABLE people(FirstName TEXT, LastName TEXT, Age INT);
			INSERT INTO people VALUES('Ron', 'Obvious', '42',);
			""")
	
SyntaxError: unexpected indent
>>> with sqlite3.connect('test_database.db') as connection:
	c = connection.cursor()
	c.executescript("""DROP TABLE IF EXIST people;
			CREATE TABLE people(FirstName TEXT, LastName TEXT, Age INT);
			INSERT INTO people VALUES('Ron', 'Obvious', '42',);
			""")
	peopleValues = (("Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))
			 
SyntaxError: EOL while scanning string literal
>>> peopleValues = (("Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))
		 
SyntaxError: EOL while scanning string literal
>>> peopleValues = (('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))
>>> c.executemany("INSERT INTO people VALUES(?, ?, ?)",peopleValues)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    c.executemany("INSERT INTO people VALUES(?, ?, ?)",peopleValues)
sqlite3.OperationalError: no such table: people
>>> c.executemany("INSERT INTO people VALUES(?, ?, ?)",peopleValues)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    c.executemany("INSERT INTO people VALUES(?, ?, ?)",peopleValues)
sqlite3.OperationalError: no such table: people
>>> 
============================ RESTART: C:/Users/guapo/Desktop/python 2/parameterized.py ============================
Enter your first name: sal
Enter your last name: sandoval
Enter your age: 38
Traceback (most recent call last):
  File "C:/Users/guapo/Desktop/python 2/parameterized.py", line 14, in <module>
    c.execute(line)
sqlite3.OperationalError: no such table: people
>>> 
============================ RESTART: C:/Users/guapo/Desktop/python 2/parameterized.py ============================
Enter your first name: 
============================ RESTART: C:/Users/guapo/Desktop/python 2/parameterized.py ============================
Enter your first name: s
Enter your last name: s
Enter your age: s
Traceback (most recent call last):
  File "C:/Users/guapo/Desktop/python 2/parameterized.py", line 7, in <module>
    age = int(input("Enter your age: "))
ValueError: invalid literal for int() with base 10: 's'
>>> 
============================ RESTART: C:/Users/guapo/Desktop/python 2/parameterized.py ============================
Enter your first name: s
Enter your last name: s
Enter your age: 2
Traceback (most recent call last):
  File "C:/Users/guapo/Desktop/python 2/parameterized.py", line 14, in <module>
    c.execute(line)
sqlite3.OperationalError: no such table: people
>>> 
============================ RESTART: C:/Users/guapo/Desktop/python 2/parameterized.py ============================
Enter your first name: s
Enter your last name: s
Enter your age: 5
Traceback (most recent call last):
  File "C:/Users/guapo/Desktop/python 2/parameterized.py", line 14, in <module>
    c.execute(line)
sqlite3.OperationalError: no such table: people
>>> 
============================ RESTART: C:/Users/guapo/Desktop/python 2/parameterized.py ============================
Enter your first name: s
Enter your last name: s
Enter your age: 5
Traceback (most recent call last):
  File "C:/Users/guapo/Desktop/python 2/parameterized.py", line 14, in <module>
    c.execute(line)
sqlite3.OperationalError: no such table: People
>>> 
============================ RESTART: C:/Users/guapo/Desktop/python 2/parameterized.py ============================
Enter your first name: d
Enter your last name: d
Enter your age: 3
Traceback (most recent call last):
  File "C:/Users/guapo/Desktop/python 2/parameterized.py", line 14, in <module>
    c.execute(line)
sqlite3.OperationalError: no such table: people
>>> 
============================ RESTART: C:/Users/guapo/Desktop/python 2/parameterized.py ============================
Traceback (most recent call last):
  File "C:/Users/guapo/Desktop/python 2/parameterized.py", line 10, in <module>
    c.execute("DROP TABLE IF EXIST people")
sqlite3.OperationalError: near "EXIST": syntax error
>>> 
============================ RESTART: C:/Users/guapo/Desktop/python 2/parameterized.py ============================
('Ron', 'Obvious')
('Luigi', 'Vercotti')
>>> 
============================ RESTART: C:/Users/guapo/Desktop/python 2/parameterized.py ============================
Traceback (most recent call last):
  File "C:/Users/guapo/Desktop/python 2/parameterized.py", line 5, in <module>
    c.execute("SELECT FirstName, LastName FROM people WHERE Age > 30")
NameError: name 'c' is not defined
>>> 
============================ RESTART: C:/Users/guapo/Desktop/python 2/parameterized.py ============================
('Ron', 'Obvious')
('Luigi', 'Vercotti')
>>> 