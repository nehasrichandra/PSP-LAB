# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 11:30:21 2021

@author: neha
"""

#Let's load and read the 'yelp.xlsx' file

import pandas as pd
xls = pd.ExcelFile('C:/Users/neha/Downloads/yelp.xlsx')
df = xls.parse('yelp_data')
'''print(df)
#df is a data frame
print(type(df))'''
'''#to count rows
print(len(df))
#get the size(rows,columns)
print(df.shape)

###Inspecting Data- DataFrame
#Get a count of values in each column
print(df.count())
#You can look at the column headers by accessing the column attributes
print(df.columns)
#And the type of data stored in each column by accessing the dtypes attribute
#print(df.dtypes)
#Provides various summary statistics for the numerical values in DataFrame
print(df.describe)
#quickly examine the first 5 rows of data
print(df.head())
#or the first 100 rows
print(df.head(100))'''
#drop the duplicates(based on all columns)from df
df = df.drop_duplicates()
print(df)

'''###QUERYING DATA
#Selecting just the business names using the 'name' attribute in between square brackets[]
print(df["name"],'\n') #returns name for every record
#Query the location for the first 100 businesses
atts = ['name','city_id','state_id']
print(df[atts].head(100))'''


