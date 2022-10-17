
##Artist Data
##Create Empty Data Frame

import pandas as pd
import mysql.connector
#import pymysql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

cur = mydb.cursor()
cur.execute("USE DB")

###Create connection to mysql database for creating table
def create_table_connection_mysql():
    from sqlalchemy import create_engine
    my_conn = create_engine("mysql+pymysql://root:password@localhost/DB")
    return my_conn

###Function to create table
def create_table(table_name, table_def):
    str1 = ""
    for i in table_def.index:
        str1 = str1 + i+" "+table_def[i]+",\n"
    #str = "DROP TABLE IF EXISTS "+table_name+"; \n" \
    str = "CREATE TABLE "+table_name+" (\n" \
    ""+str1[:-2] + "\n" \
    ");"
    return str

### Read File

file_name_list = ["artist","genre","genre_artist"]

for item in file_name_list:
    file_name = item

    df = pd.DataFrame(columns = ['ID','NAME','URL'])
    with open(file_name, 'r') as file:
        importfile = file.read()

    ###Create dataframe and cleanup columns

    df = pd.DataFrame([x.split("\x01")for x in importfile.split("\x02\n")])
    df = df.rename(columns=df.iloc[0]).drop(df.index[0])
    df.columns = df.columns.str.replace("#", "")
    db_types = df.loc[2].str.replace("#dbTypes:", "")
    df = df[df['export_date'].astype(str).str[0] != "#"].reset_index()
    del df['index']
    df = df.dropna()

    #df = df.loc[0:480000]

    ###Build Table using pre-defined function above
    #drop table

    sql_stmt = "DROP TABLE IF EXISTS "+file_name+";"
    cur.execute(sql_stmt)
    mydb.commit()

    #Create Table

    sql_stmt = create_table(file_name, db_types)
    cur.execute(sql_stmt)
    mydb.commit()

    conn_create_table = create_table_connection_mysql()
    df.to_sql(file_name, conn_create_table, if_exists='append', index=False)
