# SQL Query Manager # 

## Purpose ## 
The purpose of this script is to read a SQL query from a file to pull data and load it to a pandas data frame. 

## Requirements ## 
Pandas: ```pip install pandas```

PYODBC: ```pip install pyodbc```

## SQL Query Manager Usage ## 
```python
server = 'ServerName'
database = 'DataBase'
query = read_query(r"C:\Query.sql")

with OpenDBConnection(server, database) as conn:
    df = pd.io.sql.read_sql(query, conn)
```