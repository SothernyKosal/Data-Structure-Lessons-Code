import psycopg2 as pg
choice = int(input("Enter Your choice:\n"
                   "1. Find\n"
                   "2. insert\n"
                   "3. delete\n"
                   "4. Quit\n"))
def Conneciton():
    connection = ""
    # use postgres
    try:
        connection = pg.connect(user="postgres",
                            password = "sotherny",
                            port="5432",
                            host ="127.0.0.1",
                            database = "DataStructure")
        # cursor = connection.cursor()
        # print("connected")

        return connection

    except (Exception) as e:
        print(e)


con = Conneciton()
cursor = con.cursor()
while choice!=0:
    if choice == 1:
        choice_find = input("Enter choice you want to find star:\n"
                                "a. by star's id\n"
                                "b. by star's name\n")
        if choice_find == 'a':
            id = input("Enter star's id:")
            cursor.execute(f"select star_name from star where id = '{id}'")
            con.commit()
            result = cursor.fetchone()
            print(result)
        if choice_find == 'b':
            name = input("Enter star's name:")
            cursor.execute(f"select star_name from star where name = '{name}'")
            con.commit()
            result = cursor.fetchone()
            print(result)

        # continue
    elif choice==2:
        id = input("Enter star's id:")
        star_name = input("Enter star's name:")
        cursor.execute(f"insert into star values('{id}','{star_name}')")
        con.commit()
        print("inserted successfully")
    elif choice==3:
        id = input("Enter star's id:")
        cursor.execute(f"delete from star where id = '{id}'")
        con.commit()
        print("deleted successfully")
    elif choice == 4:
        if (con):
            cursor.close()
            con.close
            print("connection is closed")
        break
    print("____________________________")
    choice = int(input("Enter Your choice:\n"
                       "1. Find\n"
                       "2. insert\n"
                       "3. delete\n"
                       "4. Quit\n"))

# finally:
#     if(connection):
#         cursor.close()
#         connection.close
#         print("connection is closed")
# li = [x for x in range(2)]
# print(li)