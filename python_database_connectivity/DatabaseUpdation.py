import mysql.connector as c
mydb = c.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "cvr"
)
print("Connected to the DataBase")
mycursor = mydb.cursor()
jersey_number = int(input("Enter the jersey number of the player you want to delete : "))
runs = int(input("Enter the runs you want to change : "))
mycursor.execute("update batsman set runs=%s WHERE jersey_number=%s",(runs,jersey_number))
print("Record updated")
mydb.commit()

#OUTPUT
"""
Connected to the DataBase
Enter the jersey number of the player you want to delete : 18
Enter the runs you want to change : 23000
Record updated

"""

"""
+---------------+-------------------+-----------+-------+
| jersey_number | player_name       | state     | runs  |
+---------------+-------------------+-----------+-------+
|             1 | KL Rahul          | Karnataka | 12000 |
|            18 | Virat Kohli       | Delhi     | 23000 |
|            45 | Rohit Sharma      | Mumbai    | 15000 |
|            63 | Surya Kumar Yadav | Mumbai    |  4000 |
+---------------+-------------------+-----------+-------+
"""