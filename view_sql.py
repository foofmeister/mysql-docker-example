import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

cur = mydb.cursor()
cur.execute("USE DB")

#sql_stmt = f"SELECT * FROM artist"

#cur.execute(sql_stmt)
#response = cur.fetchall()

#for row in response:
#    print(row[0], row[1],row[2],)

#cur.close()
#mydb.close()


df = pd.read_sql_query(
        "select * from artist", mydb)



df2 = pd.read_sql_query(
        "select * from genre", mydb)

df3 = pd.read_sql_query(
        "select * from genre_artist", mydb)