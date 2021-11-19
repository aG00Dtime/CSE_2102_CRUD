import mysql.connector as mysql
from mysql.connector import errorcode


def db_conn(user_name, pass_word):
    try:
        db = mysql.connect(host='localhost',
                           username=user_name,
                           password=pass_word,
                           database='employees'

                           )

    except mysql.Error as err:
        # if login details are wrong
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            # return str
            return "Username or Password error"
        # if database error
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return "Database does not exist"
            # if host error
        elif err.errno == errorcode.ER_BAD_HOST_ERROR:
            return "Error connecting to host"
        else:
            # return any other errors
            return err
    else:
        # print if success and return db obj
        print("Success connected user : " + user_name)
        # print(type(db))
        # return db connection object
        return db
