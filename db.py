import sqlite3
class database:
    def __init__ (self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        self.cur.execute( """ 
             CREATE TABLE IF NOT EXISTS dub(
               id INTEGER PRIMARY KEY,
               name text,
               age integer,
               doj text,
               email text,
               gender text,
               contact text,
               address text
        
             )
        
                """ )
            
        self.con.commit() 
    def insert(self,name,age,doj,email,gender,contact,address):
        self.cur.execute((""" INSERT INTO dub VALUES (NULL,?,?,?,?,?,?,?)"""),(name,age,doj,email,gender,contact,address))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT*from dub")
        rows=self.cur.fetchall()
       # print(rows)
        return rows

    def remove(self,id):
        self.cur.execute("""delete from dub where id=?""",(id,))
        self.con.commit()

    def update(self,id,name,age,doj,email,gender,contact,address):  
        self.cur.execute((""" update  dub set name=? ,age=?,doj=?,email=?,gender=?,contact=?,address=? where id = ?"""),(name,age,doj,email,gender,contact,address,id))
        self.con.commit()


