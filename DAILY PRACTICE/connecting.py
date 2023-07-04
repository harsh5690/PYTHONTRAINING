"""
Database : Database which is contain data in the form of the table

pymysql

pip install <packagename>

pip install pymysql-

"""

import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="")
mycursor = mydb.cursor()

# execute respective query
mycursor.execute("create database IF NOT EXISTS mydb2023")

# to save this statement
mydb.commit()

# db connection 
mydb = pymysql.connect(host="localhost",user="root",password="",database="mydb2023")
mycursor = mydb.cursor()

mycursor.execute("create table IF NOT EXISTS student (id int primary key auto_increment, name varchar(20),subject varchar(20))")
mydb.commit()