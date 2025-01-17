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
mycursor.execute("delete from batsman WHERE jersey_number=%s",(jersey_number,))
print("Record deleted")
mydb.commit()

#OUTPUT
"""
Connected to the DataBase
Enter the jersey number of the player you want to delete : 17
Record deleted

Process finished with exit code 0
"""

"""
+---------------+-------------------+-----------+-------+
| jersey_number | player_name       | state     | runs  |
+---------------+-------------------+-----------+-------+
|             1 | KL Rahul          | Karnataka | 12000 |
|            18 | Virat Kohli       | Delhi     | 18000 |
|            45 | Rohit Sharma      | Mumbai    | 15000 |
|            63 | Surya Kumar Yadav | Mumbai    |  4000 |
+---------------+-------------------+-----------+-------+
"""