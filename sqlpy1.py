# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 21:41:27 2020

@author: eric
"""
#DESKTOP-HJJ71OG\SQLEXPRESS
import pyodbc 
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=DESKTOP-HJJ1OG\SQLEXPRESS;'
                      'DATABASE=VIDEOTEK;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM [2MEDIA]')

for row in cursor:
    print(row)