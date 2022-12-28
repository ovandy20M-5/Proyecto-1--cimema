import mysql.connector

conexion = mysql.connector.connect(user='root', password='ovandy10',
                                    host='localhost'),
                                    database='bdmysql',
                                    port='3307'
print(conexion)

