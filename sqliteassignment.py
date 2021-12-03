

import sqlite3

connection = sqlite3.connect("C:\Users\guapo\Desktop\python 2/test_database.db")

c = connection.cursor()

c.execute("CREATE TABLE people  (FirstName TEXT, LastName TEXT, Age INT)")

