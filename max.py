
"""
dir_name = 'C:\\SomeDirectory'
extension = ".zip"

os.chdir(dir_name) # change directory from working dir to dir with files

for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = os.path.abspath(item) # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(dir_name) # extract file to dir
        zip_ref.close() # close file
        os.remove(file_name) # delete zipped file
"""

##Artist Data
##Create Empty Data Frame

import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

cur = mydb.cursor()
cur.execute("USE DB")

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
df = pd.DataFrame(columns = ['ID','NAME','URL'])
with open('artist', 'r') as file:
    importfile = file.read()

###Create dataframe and cleanup columns

df = pd.DataFrame([x.split("\x01")for x in importfile1.split("\x02\n")])
df = df.rename(columns=df.iloc[0]).drop(df.index[0])
df.columns = df.columns.str.replace("#", "")
a = df.loc[2].str.replace("#dbTypes:", "")

###Build Table using pre-defined function above

#drop table

sql_stmt = "DROP TABLE IF EXISTS "+table_name+";"
cur.execute(sql_stmt)
mydb.commit()

sql_stmt = create_table("artist",a)
cur.execute(sql_stmt)
mydb.commit()

conn_create_table = create_table_connection_mysql()
a.to_sql('Twitter_Price_Solana', conn_create_table, if_exists='append', index=False)

conn_create_table = create_table_connection_mysql()
a.to_sql('Twitter_Price_Solana', conn_create_table, if_exists='append', index=False)







"""DROP TABLE IF EXISTS `artist`;
CREATE TABLE `artist` (
"create table artists"



