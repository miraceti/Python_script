# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 18:43:31 2020

@author: eric
"""


import pyodbc
import pandas as pd
server = 'DESKTOP-HJJ71OG\SQLEXPRESS'
database = 'videotek'
con=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';trusted_connection=yes')
cursor = con.cursor()

#la version du driver
#cursor.execute("SELEct @@version;")
#row = cursor.fetchone()
#while row:
#    print('d:'+row[0])
#    row= cursor.fetchone()
# fin version driver    
    
# mode dataframe
#df = pd.read_sql_query("select * from [2MEDIA]",con)
#print(df)
#
#df = pd.read_sql_query("select * from [2MEDIA] where column1 like'%xfiles%'",con)
#print(df)

df = pd.read_sql("select * from [2MEDIA] where column1 like'%xfiles%'",con)
#print(df)

print(df.dtypes)
print(df.head())

