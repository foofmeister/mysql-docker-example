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

```shell
docker build -t local-mysql .
```

* Run Container

```shell
docker run -dp 3306:3306 local-mysql
```

##Ensure you have python requirements

* cd into folder where file instructions are kept, then run following command.  
* Depending on what version of python you are using, you might need to use pip3


```shell
pip install -r requirements
```


