import mysql.connector

conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3306)
mycursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()