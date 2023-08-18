# READ OPERATION(SELCT): Retreiving Data from the database

# Step 1. Database connection
import pymysql

connection = pymysql.connect(host='localhost', user='root', password='', database='mpesatestdb')
print("Database connected succesfully")

# Step 2. Create connection cursor
cursor = connection.cursor()

# Step 3. Sql to read data 
sql = "select * from employees"

# Execute Sql
cursor.execute(sql)

# Step 4. Check Whether Its Empty(rowcount)
count = cursor.rowcount
print(count)


if count == 0:
    print("No Records Found")
else:
    data = cursor.fetchall()
    print(data)