import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

cur = mydb.cursor()
cur.execute("USE DB")

sql_stmt = """
select a.name as Artist_Name,
	   view_url as Apple_URL, 
       g.name as Genre
from DB.artist a
	left outer join 
			(select * from (select ROW_NUMBER() OVER (partition by artist_id order by is_primary desc) 
					row_num,artist_id,genre_id,is_primary  from DB.genre_artist) a
			where row_num = 1 ) ga on a.artist_id = ga.artist_id
    left outer join DB.genre g on ga.genre_id = g.genre_id
    where a.is_actual_artist = 1"""

cur.execute(sql_stmt)
response = cur.fetchall()

for row in response:
    print(row[0], row[1],row[2],)

cur.close()
mydb.close()

