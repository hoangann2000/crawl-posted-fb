import mysql.connector

cnx = mysql.connector.connect(user='root', password='123456',
                              host='127.0.0.1',
                              database='data_fb')

# create_db = 'create database `test_py`'

data_employee = ("INSERT INTO users "
               "(user_comment, content_comment) "
               f"VALUES (%s,%s)")
x = 'an'
y = 'y'


add_employee = (x, y)
a = cnx.cursor()
a.execute(data_employee, add_employee)
cnx.commit()
cnx.close()