import json
import random

import mysql.connector as con

# db details
db = con.connect(
    host='localhost',
    username='root',
    password='1234',
    database='isp'
)

# add
with open('data.json', "r") as file:
    data = json.load(file)
    cur = db.cursor()

    for person in data:
        first_name = person['first_name']
        first_name = first_name.strip("O'")

        last_name = person['last_name']
        last_name = last_name.strip("O'")

        email = person['email']
        address = person['address']
        phone = person['phone']
        plan = person['plan']

        cur.execute(f'''
        
        INSERT  INTO CUSTOMERS  (
        CUSTOMER_FIRST_NAME,
        CUSTOMER_LAST_NAME,
        CUSTOMER_EMAIL,
        CUSTOMER_ADDRESS,
        CUSTOMER_TELEPHONE,
        CUSTOMER_PLAN)

        VALUES ('{first_name}','{last_name}','{email}','{address}','{phone}','{plan}') 
        
        ''')

        cur.execute(f'''

                INSERT INTO EMPLOYEES (
                EMPLOYEE_FIRST_NAME,
                EMPLOYEE_LAST_NAME,
                EMPLOYEE_EMAIL,
                EMPLOYEE_ADDRESS,
                EMPLOYEE_TELEPHONE,
                EMPLOYEE_NIS,
                EMPLOYEE_DESIGNATION)

                VALUES ('{first_name}','{last_name}','{email}','{address}','{phone}','{random.randint(100000, 200000)}','{"STAFF"}') 

                ''')

    print("DONE")
    db.commit()
    db.close()
