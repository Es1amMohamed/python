'''import string
import sqlite3 

db = sqlite3.connect("elzero2.db")
cr = db.cursor()
cr.execute("CREATE TABLE if not exists Data (user_id integer,name text, Birth_day text, email email)")
cr.execute("insert into Data (user_id, name, Birth_day, email ) values(1, 'Eslam', '1997/6/14', 'es@gmali')")
cr.execute("insert into Data (user_id, name, Birth_day, email ) values(2, 'Goda', '1997/6/14', 'es@gmali')")
cr.execute("insert into Data (user_id, name, Birth_day, email ) values(3, 'Aml', '1997/6/14', 'es@gmali')")
cr.execute("insert into Data (user_id, name, Birth_day, email ) values(4, 'Ahmed', '2004/6/14', 'es@gmali')")
cr.execute("insert into Data (user_id, name, Birth_day, email ) values(5, 'Gamal', '1996/9/11', 'es@gmali')")
cr.execute("select * from Data")
x = cr.fetchall()
#for row in x :
    #if row[0] == 5:
       # print(row)



db.commit()'''

class Student:
    def __init__(self,name):
        self.name = name
        print(f"Welcom {name}")
        
n = input("pleas Enter your Name").capitalize()
s = Student(n)