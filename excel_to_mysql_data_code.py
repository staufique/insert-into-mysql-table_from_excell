# first create database
# create tables columns according to your excells columns data

# for e.g i have created table for three columns because i have only three
# columns in my excell file

import openpyxl
import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="root",
    passwd="your_passwrod",
    database="db_name")

cur = conn.cursor()
# Load the workbook
workbook = openpyxl.load_workbook('data.xlsx')#insert your excel file name

# Select the sheet you want to work with
sheet = workbook.active  # or use workbook['SheetName']

# Iterating through rows
a=[]
# give min_row and then give max_row as per your excell rows
for row in sheet.iter_rows(min_row=1, max_row=3, values_only=True):
    a.append(row)

print(a)

# here is query to insert data into your table
q="insert into students(id,name,age) values(%s,%s,%s)"
cur.executemany(q,a)
conn.commit()

conn.close()
