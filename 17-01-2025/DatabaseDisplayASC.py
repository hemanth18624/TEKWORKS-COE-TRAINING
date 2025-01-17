import mysql.connector as c
mydb = c.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "cvr"
)
print("Connected to the DataBase")
mycursor = mydb.cursor()
mycursor.execute("select *from batsman ORDER BY player_name ASC")
batsman_list = mycursor.fetchall()
for batsman in batsman_list:
    print(batsman)
mydb.commit()


#OUTPUT
"""
Connected to the DataBase
(1, 'KL Rahul', 'Karnataka', 12000)
(45, 'Rohit Sharma', 'Mumbai', 15000)
(63, 'Surya Kumar Yadav', 'Mumbai', 4000)
(18, 'Virat Kohli', 'Delhi', 23000)
"""