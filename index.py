import sqlite3 
#user_id =int(input("user id please ? "))
db = sqlite3.connect("elzero.db")
cr = db.cursor()
user_id = 0
try:
  while user_id < 5 :
    cr.execute("CREATE TABLE if not exists Data (user_id integer,name text, Birth_day text, email email)")
    name = input("'What\'s Your Name ? '").strip().capitalize()
    born_year = int(input(" Your Year Born ? "))
    month_born = int(input(" Month Born ? "))
    born_day = int(input(" What Is Yor "))
    gmail = input(" Your Emali ? ") 
    user_id +=1
    #print(user_id)
    cr.execute(f"insert into Data (user_id, name, Birth_day, email ) values({user_id}, '{name}', '{born_year}/{month_born}/{born_day}', '{gmail}')")
    a = cr.execute("select * from Data")

    #z = list(cr.fetchone())
    #print(z)
 # else:
    print(cr.fetchall())
except:
  print("gg")
#print(cr.fetchone())
#print(" ".join(z))
#print(z)

#print ( 3 > max(z))

#if x > max(z) :
 #   cr.execute(f"insert into Data(user_id, name) values({x}, 'Eslam')")
  #  print(type(cr.fetchall())) 
#else: 
 #       print("gg")
finally: 
  db.commit()