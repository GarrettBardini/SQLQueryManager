###############################################################
#####     SQL QUERY MANAGER: SQL PYODBC DATA PULL         #####
#####     AUTHOR: GARRETT PETER BARDINI (GPB)             #####
#####     CREATE_DATE: 2021/12/05                         #####
#####     LAST_MODIFIED: 2021/12/28                       #####
###############################################################
import os
import pandas as pd
import pyodbc

class OpenDBConnection():
    def __init__(self, server, database):
        self.connection = pyodbc.connect('Driver=SQL Server;Server=' + server + ';Database=' + database + ';Trusted_Connection=yes;')
        # self.cursor = self.connection.cursor()
                 
    def __enter__(self):
        return self.connection
      
    def __exit__(self):
        self.connection.close()

def read_query(path):
    import os 
    if os.path.exists(os.path.dirname(path)):
        with open(path, "r") as f:
            query = ('SET NOCOUNT ON;\n' + f.read())
            return query 

working_dir = os.path.dirname(os.path.realpath(__file__)) # os.getcwd() # 
server = 'ServerName'
database = 'DataBase'
query = read_query(r"C:\Query.sql")

with OpenDBConnection(server, database) as conn:
    df = pd.io.sql.read_sql(query, conn)

print(df)