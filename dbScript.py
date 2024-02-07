import sqlite3
from datetime import datetime
conn = sqlite3.connect('MoyaleBus.db')
cursor=conn.cursor()
#cursor.execute("INSERT INTO transactionTable VALUES ('74673','343','343','435','4343')")
cursor.execute("SELECT * FROM parcelTable")
#cursor.execute('ALTER TABLE parcelTable ADD COLUMN status text')


print("done")
print(cursor.fetchall())

conn.commit()
#Close Database connection
conn.close()
