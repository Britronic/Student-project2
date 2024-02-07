import sqlite3
conn=sqlite3.connect('MoyaleBus.db')
cursor=conn.cursor()

#createTable="""
#CREATE TABLE  RemarksTable(
#remarks TEXT,
#phoneno INTEGER
#)
#"""


cursor.execute("SELECT * FROM RemarksTable")
print(cursor.fetchall())
conn.commit()
conn.close
