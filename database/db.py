import pymysql

endpoint = 'database-2.cdaagk0my793.us-east-2.rds.amazonaws.com'
user = 'ejercicio1'
passw = 'Baseejercicio2024*-'

try:
    pymysql.connect(
        host=endpoint,
        user=user,
        password=passw
    )

    print("conexion exitosa ")

except Exception as err:
    print("error:", err)