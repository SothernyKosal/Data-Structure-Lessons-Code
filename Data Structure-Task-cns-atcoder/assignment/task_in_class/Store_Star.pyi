import psycopg2 as pg

try:
    connection = pg.connect(user="postgre",
                            password = "sotherny",
                            port="5432",
                            host ="127.0.0.1",
                            database = "DataStructure")
    cursor = connection.cursor()
    print("connected")
except (Exception) as e:
    print(e)
finally:
    if(connection):
        cursor.close()
        connection.close
        print("cconnection is closed")

print("")