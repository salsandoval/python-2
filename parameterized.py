import sqlite3

# get personal data from user
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))


# execute insert statement for supplied person data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    line = "INSERT INTO people VALUES ('"+ firstName +"', '"+ lastName +"', " +str(age) +")"
    c.execute(line)


# get personal data from user and insert into tuple
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personalData = (firstName, lastName, age)

# execute insert statement for supplied person data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO people VALUES(?, ?, ?)", personData)

    c.execute("UPDATE people SET Age=? WHERE FirstName=? AND LastName=?",
              (45, 'Luigi', 'Vercotti'))


peopleValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS people")
    c.execute("CREATE TABLE people(FirstName TEXT, LastName TEXT, Age INT)")
    c.executemany("INSERT INTO people VALUES(?, ?, ?)",
                  peopleValues)

# select all first and last names from people over age 30
    c.execute("SELECT FirstName, LastName FROM people WHERE Age > 30")
    for row in c.fetchall():
        print (row)


c.execute("SELECT FirstName, LastName FROM people WHERE Age > 30")
while True:
    row = c.fetchone()
    if row is None:
        break
        print(row)

        
    
    
    
