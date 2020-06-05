import pyodbc 
server = 'hdcu10dvdbsv106' 
database = 'a2w564sandbox01' 
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database)
cursor = cnxn.cursor()
thesql = "SELECT top 10 * from Datapoints;"
cursor.execute(thesql) 
row = cursor.fetchone() 
while row: 
    print(row)
    row = cursor.fetchone()