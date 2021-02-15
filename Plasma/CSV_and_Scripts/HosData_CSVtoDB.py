import pandas as pd
import sqlite3
# Import CSV
data = pd.read_csv (r'CSV\\Hos.csv')   
df = pd.DataFrame(data, columns= ['HosId','HosName','Hname','pasw','Email','Location','Pin','Contact','DOE','TIME'])

# Connect to SQL Server
conn = sqlite3.connect('C:\\Users\\AdityaJha\\Desktop\\Recents\\Project Vaccine\\vacisearch.db')
cursor = conn.cursor()

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO Hospital(HosId,HosName,Hname,pasw,Email,Area,Pin,Contact,DOE,TIME)
                VALUES (?,?,?,?,?,?,?,?,?,?)
                ''',
                (row.HosId,row.HosName,row.Hname,row.pasw,row.Email,row.Location,row.Pin,row.Contact,row.DOE,row.TIME))
conn.commit()