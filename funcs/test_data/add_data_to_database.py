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

# customers and employees
with open('people.json', "r") as people:
    data = json.load(people)

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

        # employees
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
print("Inserted Customers and employees")
db.commit()
db.close()

# suppliers
with open('suppliers.json', "r") as suppliers:
    cur = db.cursor()
    suppliers_data = json.load(suppliers)

    for supplier in suppliers_data:
        supplier_name = supplier['company']
        supplier_address = supplier['address']
        supplier_email = supplier['email']
        supplier_phone = supplier['phone']

        sql = f"""
        INSERT INTO SUPPLIERS
        (SUPPLIER_NAME,SUPPLIER_ADDRESS,SUPPLIER_EMAIL,SUPPLIER_TELEPHONE)
        VALUES('{supplier_name}','{supplier_address}','{supplier_email}','{supplier_phone}')
        """
        cur.execute(sql)

print("Inserted Suppliers")
db.commit()
db.close()

# devices
with open('devices.json', 'r') as devices:
    devices_data = json.load(devices)
    cur = db.cursor()

    for device in devices_data:
        device_name = device['device']
        device_serial = device['serial']
        device_desc = device['description']
        device_supplier = random.randint(14, 22)

        sql = f""" INSERT INTO DEVICES (DEVICE_NAME,DEVICE_SERIAL_NUMBER,DEVICE_DESCRIPTION,SUPPLIER_ID)
        VALUES ('{device_name}','{device_serial}','{device_desc}','{device_supplier}')

        """

        cur.execute(sql)

print("Inserted Devices")
db.commit()
db.close()
