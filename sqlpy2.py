# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 22:38:55 2020

@author: eric
"""

import pyodbc
import pandas as pd
server = 'DESKTOP-HJJ71OG\SQLEXPRESS'
database = 'videotek'
con=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';trusted_connection=yes')
cursor = con.cursor()

cursor.execute("SELEct @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row= cursor.fetchone()
    
#affichage de toute la table    
#cursor = con.cursor()
#cursor.execute('SELECT * FROM [2MEDIA]')
#for row in cursor:
#    print(row)
    
# mode dataframe
df = pd.read_sql_query("select * from [2MEDIA]",con)
print(df)

df = pd.read_sql_query("select * from [2MEDIA] where column1 like'%xfiles%'",con)
print(df)

df = pd.read_sql("select * from [2MEDIA] where column1 like'%xfiles%'",con)
print(df)