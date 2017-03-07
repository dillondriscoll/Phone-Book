import sqlite3

class Database:
    
    #Logic for starting and connecting to a mySQL database
    def __init__(self):
        conn=sqlite3.connect("phone.db") #Create a database table if there isn't one already
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS phone (id INTEGER PRIMARY KEY,firstName text, lastName text, location text, number integer)")
        conn.commit()
        conn.close()

    def insert(self,firstName,lastName,location,number):
        conn=sqlite3.connect("phone.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO phone VALUES (NULL,?,?,?,?)",(firstName,lastName,location,number))

        conn.commit()
        conn.close()

    def view(self):
        conn=sqlite3.connect("phone.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM phone")
        rows = cur.fetchall()
        conn.close()
        return rows

    def search(self,firstName="",lastName="",location="",number=""):
        conn=sqlite3.connect("phone.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM phone WHERE firstName=? OR lastName=? OR location=? OR number=?", (firstName,lastName,location,number))
        rows = cur.fetchall()
        conn.close()
        return rows

    def delete(self,id):
        conn=sqlite3.connect("phone.db")
        cur=conn.cursor()
        cur.execute("DELETE FROM phone WHERE id=?",(id,))
        conn.commit()
        conn.close()

    def update(self,id,firstName,lastName,location,number):
        conn=sqlite3.connect("phone.db")
        cur=conn.cursor()
        cur.execute("UPDATE phone SET firstName=?, lastName=?, location=?, number=? WHERE id=?", (firstName,lastName,location,number,id))
        conn.commit()
        conn.close()



