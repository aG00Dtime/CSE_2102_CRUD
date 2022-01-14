import mysql.connector as mysql
from mysql.connector import errorcode
import json
import os
from cryptography.fernet import Fernet

# paths
root = os.path.abspath(os.curdir)
json_path = os.path.join(root,'host_config.json')


def db_conn():

    try:
        # read file
        if os.path.exists(json_path) and not os.stat(json_path).st_size == 0:

            # open file if it exists and isn't empty
            with open(json_path, "r") as file:

                # load file
                data = json.load(file)
                # key would be saved to a file somewhere secure
                # decrypt key
                with open(os.path.join(root, 'k.key'), 'rb') as key:
                    key = key.read()

                f = Fernet(key)
                pwe = (data['PASSWORD'].encode())
                pwd = f.decrypt(pwe)

        db = mysql.connect(host=data["HOST"],
                           username=data["USERNAME"],
                           password=str(pwd).strip("b").strip("'").strip("'"),
                           database=data["DATABASE"]

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
        # return db connection object
        return db
