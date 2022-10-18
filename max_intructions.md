#Max Instructions
###Ingest three different files into mysql server, and create queries to access data.

##Set up files: should contain

* view_sql.py
* Dockerfile
* max.py
* schemas.sql
* requirements.txt 

##Files to Import (make sure to unzip files first)

* genre
* artist
* genre_artist

##File Instructions

* Put all files in one folder

##Build Docker Image

* Start Docker Desktop

* Build Image in CLI

* cd into folder where file instructions are kept

```shell
docker build -t local-mysql .
```

* Run Container

```shell
docker run -dp 3306:3306 local-mysql
```

##Ensure you have python requirements
 
* Depending on what version of python you are using, you might need to use pip3


```shell
pip install -r requirements
```

##Run Script

* Script is written in python3.
* You can also run script from an IDE such as pycharm or Visual Studio Code
 
```shell
python3 max.py
```
##Check Results 

* There are several ways you can do this:
  * Open your favorite sql editor such as phpmyadmin or MySQLWorkbench
  * Connect using :
    * Hostname: localhost
    * Username: root
    * Password: password
    * Port: 3306
  
```sqlite-psql

select a.name as Artist_Name,
	   view_url as Apple_URL, 
       g.name as Genre
from DB.artist a
	left outer join 
			(select * from (select ROW_NUMBER() OVER (partition by artist_id order by is_primary desc) 
					row_num,artist_id,genre_id,is_primary  from DB.genre_artist) a
			where row_num = 1 ) ga on a.artist_id = ga.artist_id
    left outer join DB.genre g on ga.genre_id = g.genre_id
    where a.is_actual_artist = 1
```
 * Or, run 

```shell
python3 view_sql.py
```