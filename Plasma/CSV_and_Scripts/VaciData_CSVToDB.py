import pandas as pd
import sqlite3
# Import CSV
data = pd.read_csv (r'CSV_and_Scripts\\Vaccine.csv')   
df = pd.DataFrame(data, columns= ['Vacci_Product_ID','product_TBL','CVX_Short_Description','CVX_Code','manufacturer_TBL','manufacturer_TBL_MVX_CODE','MVX_status','product_name_status','product_TBL_Update_date'])

 #Connect to SQL Server
conn = sqlite3.connect('C:\\Users\\AdityaJha\\Desktop\\Recents\\Project Vaccine\\vacisearch.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS vaci_info (Vacci_Product_ID,product_TBL,CVX_Short_Description,CVX_Code,manufacturer_TBL,manufacturer_TBL_MVX_CODE,MVX_status,product_name_status,product_TBL_Update_date)')

# Insert DataFrame to Table
for row in df.itertuples():
   cursor.execute('''
                INSERT INTO vaci_info(Vacci_Product_ID,product_TBL,CVX_Short_Description,CVX_Code,manufacturer_TBL,manufacturer_TBL_MVX_CODE,MVX_status,product_name_status,product_TBL_Update_date)
                VALUES (?,?,?,?,?,?,?,?,?)
                ''',
                (row.Vacci_Product_ID,row.product_TBL,row.CVX_Short_Description,row.CVX_Code,row.manufacturer_TBL,row.manufacturer_TBL_MVX_CODE,row.MVX_status,row.product_name_status,row.product_TBL_Update_date))
conn.commit()
