#Max Instructions
###Ingest three different files into mysql server, and create queries to access data.

##Set up files: should contain

* view_sql.py
* Dockerfile
* max.py
* schemas.sql
* requirements.txt 

##Files to Import (unzipped)

* genre
* artist
* genre_artist

##Build Docker Image

* Start Docker Desktop

* Build Image in CLI

```shell
docker build -t local-mysql .
```

* Run Container

```shell
docker run -dp 3306:3306 local-mysql
```
