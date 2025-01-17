import mysql.connector as c
mydb = c.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "cvr"
)
print("Connected to the DataBase")
mycursor = mydb.cursor()
jersey_number = int(input("Enter the jersey number of the player : "))
player_name = input("Enter the player name : ")
state = input("Enter the state he plays for : ")
runs = int(input("Enter the runs he scored : "))
mycursor.execute("INSERT INTO batsman values (%s,%s,%s,%s)",(jersey_number,player_name,state,runs))
print("Record Inserted")
mydb.commit()




#OUTPUT
"""
+---------------+-------------------+-----------+-------+
| jersey_number | player_name       | state     | runs  |
+---------------+-------------------+-----------+-------+
|             1 | KL Rahul          | Karnataka | 12000 |
|            17 | MS Dhoni          | Jharkhand | 14000 |
|            18 | Virat Kohli       | Delhi     | 18000 |
|            45 | Rohit Sharma      | Mumbai    | 15000 |
|            63 | Surya Kumar Yadav | Mumbai    |  4000 |
+---------------+-------------------+-----------+-------+
"""



#Table Creation
#mycursor.execute("""CREATE TABLE batsman (
 #   jersey_number INT PRIMARY KEY,
  #  player_name VARCHAR(100),
   # state VARCHAR(50),
    #runs INT
#);
#""") """