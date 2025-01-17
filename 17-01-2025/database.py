

import mysql.connector as c
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cvr"
)
print("Connected to the database")
mycursor = mydb.cursor() #creating a database object
#name = input("Enter the name of the student : ")
#roll = int(input("Enter the roll number you want to update : "))
mycursor.execute("select * from students")
student_list = mycursor.fetchall()
for student in student_list:
    print(student)
mydb.commit()






#delete from students WHERE rollno = 6718
#insert into students values('Hemanth',6717)
#update students set rollno = 6718 WHERE name = 'Hemanth'
#insert into students values (%s,%s)",(name,roll)
#update students set rollno=%s WHERE name=%s",(roll,name)
#delete from students WHERE rollno=%s",(roll,)