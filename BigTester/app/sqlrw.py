import pymysql.cursors



def list_users():
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='GHRRich',
                                     db='BigTester',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `Users` "
            cursor.execute(sql)
            result = cursor.fetchall()
            print('read Users')

            return result
    finally:
        connection.close()


def crt_users(username, email, password, stateadmin):
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='GHRRich',
                                     db='BigTester',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `Users` (`username`,`email`, `password`, `stateadmin`) " \
                  "VALUES ('{}','{}','{}','{}')".format(str(username), str(email), str(password), int(stateadmin))
            cursor.execute(sql)

            print('Create Users')

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        connection.close()


def delet_users(iduser):
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='GHRRich',
                                     db='BigTester',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            # Create a new record
            sql = "DELETE FROM `Users` WHERE `Users`.`id` = {}".format(iduser)
            cursor.execute(sql)

            print('Create Users')

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        connection.close()
