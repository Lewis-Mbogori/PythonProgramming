# 1. Create a database connection to
# 2. confirm the connection

# 3. create 3 variables to hold username, password, phone

# 4. create a cursor to your connection
# 5. write sql to save username, password and phone on users table
# 6. execute your sql
# 7. commit your connection
# 8. notify that record has been saved.

import pymysql

connection = pymysql.connect(host='localhost', user='root', password='', database='mpesatestdb')
print("Database connected succesfully")



# connection = pymysql.connect(host='localhost', user='root', password='', database='assignment')
# print("Database Connected Successfully")

username = "Sarah Ann Conor"
password = "qwerty12345"
phone = "0792322047"

cursor = connection.cursor()

sql = "insert into assignment (username, password, phone) values (%s, %s, %s)"

data = (username, password, phone)
cursor.execute(sql, data)

connection.commit()

print("User Saved Successfully")







# SELECT: Login, Ecommerce
# Update
# Delete