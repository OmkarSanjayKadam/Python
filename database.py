from table_metadata import tableList,con
from contextlib import contextmanager
import sqlite3

def db_setup(cur):
    for eachTable,allColumns in tableList.items:
        try:
            result= cur.execute("SELECT * FROM  eachTable")
        except sqlite3.OperationalError as e:
            if "no such table " in str(e):
                columnQuery = "(" + (",").join(allColumns)+ ")"
                finalQuery= "CREATE TABLE <tableName> (C!,C2)"
                cur.execute("CREATE TABLE" + eachTable +columnQuery)
                print(columnQuery)
                #print(finalQuery)
            
def insert_db(cur,query):
    cur.execute(query)
              
@contextmanager  
       
def cursor_handler():
     cur =con.cursor()    #using cursor to run the database and point out 
     yield cur
     cur.close() #closing the connection automatically when you come outside
     con.commit() #commit is important
 
 with cursor_handler() as cur   
    db_setup()
    
#in utilites.py file create a table.py which has the following content:

tableList ={
    "STACKEXCHANGE USER" : ["USerID", "REPUTATION"]
    "GITHUB_USER" : ["USERNAME"]
}

import sqlite3
con = sqlite3.connect("hushhush.db",check_same_thread= False)   #hushhush.db is the name of database and check same thread will allow only one to write or edit or insert 







#Another file name __init__ 

from db_handler import cursor_handler, insert_db





#stackoverflow.py file:
