import sqlite3

#connect to database

connection= sqlite3.connect("student.db")

#create cursor object(insertion,creation,deletion)

cursor= connection.cursor()

#create table

table_info= """ 
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);

"""

cursor.execute(table_info)

#insert records

cursor.execute(''' Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute(''' Insert Into STUDENT values('Arpan','Data Science','A',100)''')
cursor.execute(''' Insert Into STUDENT values('Harsh','Full Stack','A',50)''')
cursor.execute(''' Insert Into STUDENT values('Vedant','Machine Learning','A',35)''')
cursor.execute(''' Insert Into STUDENT values('OD','Data Science','A',48)''')
cursor.execute(''' Insert Into STUDENT values('Gaytri','Machine Learning','A',67)''')


#display records

print("The inserted records are")
data= cursor.execute(''' Select * from STUDENT ''')

for row in data:
    print(row)


connection.commit()
connection.close()