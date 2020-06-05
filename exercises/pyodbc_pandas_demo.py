import pyodbc
import pandas as pd
server = 'hdcu10dvdbsv106' 
database = 'a2w564sandbox01' 
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database)
thesql = "SELECT top 10 * from Datapoints;"
data = pd.read_sql(thesql,cnxn)