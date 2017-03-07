import sqlite3

class Database:  
    #Logic for starting and connecting to a mySQL database
    def __init__(self,db):
        self.conn=sqlite3.connect(db) #Create a database table if there isn't one already
        self.cur= self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS phone (id INTEGER PRIMARY KEY,firstName text, lastName text, location text, number integer)")
        self.conn.commit()
        
    def insert(self,firstName,lastName,location,number):
        self.cur.execute("INSERT INTO phone VALUES (NULL,?,?,?,?)",(firstName,lastName,location,number))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM phone")
        rows = self.cur.fetchall()
        return rows

    def search(self,firstName="",lastName="",location="",number=""): 
        self.cur.execute("SELECT * FROM phone WHERE firstName=? OR lastName=? OR location=? OR number=?", (firstName,lastName,location,number))
        rows = self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM phone WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,firstName,lastName,location,number):  
        self.cur.execute("UPDATE phone SET firstName=?, lastName=?, location=?, number=? WHERE id=?", (firstName,lastName,location,number,id))
        self.conn.commit()
    def __del__(self): #destructor
        self.conn.close()




