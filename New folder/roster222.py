import sqlite3

connection = sqlite3.connect(':memory:')  # one time use database memory ,  also changed conn to connection

c = connection.cursor() # changed conn to connection

c.execute("CREATE TABLE IF NOT EXISTS Roster( Name TEXT, Species TEXT, IQ INT)")  #moved everything to a single line

connection.commit()  # changed conn to connection

