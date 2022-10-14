import pandas

##Make Mysql Connection
import pandas as pd


def create_connection_sql():
    import mysql.connector
    mydb = None
    try:
        mydb = mysql.connector.connect(
            host='34.94.143.25',
            user='root',
            password='tBKsPvD20ndJ3thg',
            port='3306',
            database='db_forest',
            autocommit=False
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return mydb

##Artist Data
##Create Empty Data Frame

df = pd.DataFrame(columns = ['ID','NAME','URL'])

with open('artist', 'r') as file:
    importfile = file.read()

print(importfile.count('\n'))

importfile1 = importfile

df = pd.DataFrame([x.split("\x01")for x in importfile1.split("\x02\n")])
df = df.rename(columns=df.iloc[0]).drop(df.index[0])


df[,1]
        ID = line[0:20]
        ch = line.find("https")
        NAME = line[20:ch]
        URL = line[ch:]
        #data = {"ID": ID, "NAME": NAME, "URL": URL}
        df2 = pd.DataFrame({"ID": ID, "NAME": NAME, "URL": URL},index=[0])
        df = pd.concat([df,df2])

ascii(1)