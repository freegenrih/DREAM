

# Connect to the database
from settings import connection
'''
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `Users` (`username`,`email`, `password`, `stateadmin`) " \
              "VALUES ('NewsUser1', 'webmaster@python.org', 'very-secret', '0')"
        cursor.execute(sql)
        print('OK')

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `Users` "
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()
'''

def list_users():
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `Users` "
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        connection.close()


full_list_users = list_users()