# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 21:58:10 2020

@author: eric
"""

import pyodbc
price_data = [[2.00,3.00,1.00,2.40,100.00,'01/02/2020'],
              [3.00,3.00,5.00,9.40,300.00,'02/02/2020'],
              [4.00,2.00,1.00,2.40,200.00,'03/03/2020']]

for driver in pyodbc.drivers():
    print(driver)