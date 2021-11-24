

import sqlite3

fileList = ('information.docx' , 'Hello.txt' , 'myImage.png' , \
            'myMovie.mpg' , 'World.txt' , 'data.pdf' , 'myPhoto.jpg')

conn = sqlite3.connect('info.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtFiles\
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_fileName TEXT \
                )")
    for file in fileList:
        if file.endswith('.txt'):
            cur.execute("INSERT INTO tbl_txtFiles (col_fileName) VALUES (?)", (file,))
            print (file)
    conn.commit()
conn.close()
