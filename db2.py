# UPDATE: Modify an already existing record\
import pymysql

connection = pymysql.connect(host='localhost', user='root', password='', database='mpesatestdb')
print("Database connected succesfully")

# cursor
cursor = connection.cursor()

# data
salary = 600000
emp_id = 9

# sql
sql = "Update employees set salary = %s where emp_id = %s"

# execution
data = (salary, emp_id)
cursor.execute(sql, data)
connection.commit()

# notify user
print(f"Employee ID {emp_id} salary updated successfully with{salary}")