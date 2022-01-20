drop database if exists ISP;

create database ISP;
use ISP;
    
CREATE TABLE users (
    user_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    username VARCHAR(45) NOT NULL UNIQUE,
    password BLOB NOT NULL,
    access_level VARCHAR(20) NOT NULL
);




CREATE TABLE employees (

    employee_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    employee_first_name VARCHAR(45) NOT NULL,
    employee_last_name VARCHAR(45) NOT NULL,
    employee_telephone VARCHAR(45) NOT NULL,
    employee_email VARCHAR(45),
    employee_address VARCHAR(45),
    employee_designation VARCHAR(45),
    employee_nis VARCHAR(45),
    
    created_on DATETIME,
    modified_on DATETIME,
    modified_by VARCHAR(45)

);
  
CREATE TABLE employee_logins (
    login_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    login_user_id INT NOT NULL UNIQUE,
    login_employee_id INT NOT NULL UNIQUE,
    FOREIGN KEY (login_user_id)
        REFERENCES users (user_id),
    FOREIGN KEY (login_employee_id)
        REFERENCES employees (employee_id)
);

CREATE TABLE plans (
    plan_id INT AUTO_INCREMENT PRIMARY KEY,
    plan_name VARCHAR(45) NOT NULL,
    plan_burst_speed VARCHAR(45) NOT NULL,
    plan_upload_speed VARCHAR(45) NOT NULL,
    plan_download_speed VARCHAR(45) NOT NULL,
    plan_cost VARCHAR(45) NOT NULL
);

CREATE TABLE suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_name VARCHAR(45) NOT NULL,
    supplier_address VARCHAR(45) NOT NULL,
    supplier_email VARCHAR(45) NOT NULL,
    supplier_telephone VARCHAR(45) NOT NULL
);

CREATE TABLE devices (
    device_id INT AUTO_INCREMENT PRIMARY KEY,
    device_name VARCHAR(45),
    device_serial_number VARCHAR(45),
    device_description TEXT,
    supplier_id INT,

    FOREIGN KEY (supplier_id)
        REFERENCES suppliers (supplier_id)
);

CREATE TABLE customers (

    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_first_name VARCHAR(45) NOT NULL,
    customer_last_name VARCHAR(45) NOT NULL,
    customer_telephone VARCHAR(10) NOT NULL,
    customer_email VARCHAR(45),
    customer_address VARCHAR(45),
    customer_plan INT,    

    created_on DATETIME,
    modified_on DATETIME,
    modified_by VARCHAR(45),

    FOREIGN KEY (customer_plan)
        REFERENCES plans (plan_id),

    FOREIGN KEY (modified_by)
        REFERENCES users (username)
        
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_price INT,
    order_quotation INT,
    
    FOREIGN KEY (customer_id)
        REFERENCES customers (customer_id)
);

-- add some plans
insert into plans (plan_name,plan_burst_speed,plan_cost,plan_download_speed,plan_upload_speed)values('GOLD','1000GB/s',"$30,000","99999MB/s",'10,000MB/s');
insert into plans (plan_name,plan_burst_speed,plan_cost,plan_download_speed,plan_upload_speed)values('SILVER','50GB/s',"$20,000","88888MB/s",'10,000MB/s');
insert into plans (plan_name,plan_burst_speed,plan_cost,plan_download_speed,plan_upload_speed)values('BRONZE','10GB/s',"$10,000","55555MB/s",'10,000MB/s');

-- create user in user table
insert into users (username,password,access_level) values ('admin',aes_encrypt('1234','osEpkGsvkk3ErQ0bTatcjq8T97njRuL04YLV0O6QG_c='),'admin');


-- add suppliers
insert into suppliers (supplier_name,supplier_email,supplier_address,supplier_telephone) value ("CISCO",'CISCO@EMAIL.COM','SOMEWHERE',"209-2929121");
insert into suppliers (supplier_name,supplier_email,supplier_address,supplier_telephone) value ("SOMEONE",'SOMEONE@EMAIL.COM','SOMEWHERE',"201-2929121");

-- add some devices
insert into devices (device_name,device_serial_number,device_description,supplier_id)values("MODEM","19293919292","a modem","1");
insert into devices (device_name,device_serial_number,device_description,supplier_id)values("MODEM","222222","a modem","1");

create view `customer_details` as
select customer_id,customer_first_name,customer_last_name,customer_telephone,customer_email,customer_address,plan_name,modified_by
from customers
join plans on customer_plan = plan_id;


create view `customer_update`as
select customer_id,customer_first_name,customer_last_name,customer_telephone,customer_email,customer_address,plan_id
from customers
join plans on customer_plan=plan_id;

create view `employee_details` as
select employee_id,employee_first_name,employee_last_name,employee_telephone,employee_email,employee_address,employee_NIS,employee_designation,modified_by
from employees;

-- triggers
create trigger `customer_create`
before insert
on customers for each row
set new.created_on = now();

create trigger `customer_update`
before update
on customers for each row
set new.modified_on = now();

create trigger `employee_create`
before insert
on employees for each row
set new.created_on = now();

create trigger `employee_update`
before update
on employees for each row
set new.modified_on = now();

-- view

create view `employee_login` as
select login_id,username,access_level,employee_first_name,employee_last_name
from employee_logins
join employees on login_employee_id=employee_id
join users on login_user_id=user_id;

select * from employee_login;

SELECT * FROM EMPLOYEE_LOGINs;

SELECT user_id,USERNAME,EMPLOYEE_ID,employee_first_name,employee_last_name
FROM EMPLOYEE_LOGINS
JOIN users on login_user_id=user_id
join employees on login_employee_id =employee_id;

select * from users;