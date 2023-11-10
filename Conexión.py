import mysql.connector

connection= mysql. connector. connect(
    user='root', 
    password='46497253', 
    host='localhost', 
    database='prueba1', 
    port= 3306
    )
print(connection)
print("Conexion exitosa")