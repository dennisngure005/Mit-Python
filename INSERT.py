import sqlite3

conn = sqlite3.connect('example.db')
print("opened database successfully ")

conn.execute("INSERT INTO EMPLOYEES VALUES(1,'FAITH KARIMI',40,345000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(2,'BOB KURIA',32,15000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(3,'DENNIS NGANGA',23,125000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(4,'FAITH KARIMI',20,75000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(5,'MELODY WENDO',17,50000.00)")

conn.commit()
print("Records inserted successfully")
conn.close()