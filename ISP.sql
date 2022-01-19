drop database ISP;
create database if not exists ISP;
use ISP;
    
    CREATE TABLE user (
    user_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    username VARCHAR(45) NOT NULL UNIQUE,
    password VARCHAR(45) NOT NULL,
    access_level VARCHAR(20) NOT NULL
    
);

CREATE TABLE employee (

    employee_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    employee_first_name VARCHAR(45) NOT NULL,
    employee_last_name VARCHAR(45) NOT NULL,
    employee_telephone VARCHAR(45) NOT NULL,
    employee_email VARCHAR(45),
    employee_address VARCHAR(45),
    employee_designation VARCHAR(45),
    Employee_NIS VARCHAR(45),
    
    created_on DATETIME,
    modified_on DATETIME,
    modified_by VARCHAR(45)

);


CREATE TABLE plan (
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

CREATE TABLE customer (

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
        REFERENCES plan (plan_id),

    FOREIGN KEY (modified_by)
        REFERENCES user (username)
        
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_price INT,
    order_quototation INT,
    
    
    FOREIGN KEY (customer_id)
        REFERENCES customer (customer_id)
);

-- create user in user table
insert into user (username,password,access_level) values ('admin','1234','admin');
insert into user (username,password,access_level) values ('user','1234','user');

-- add suppliers
insert into suppliers (supplier_name,supplier_email,supplier_address,supplier_telephone) value ("CISCO",'CISCO@EMAIL.COM','SOMEWHERE',"209-2929121");
insert into suppliers (supplier_name,supplier_email,supplier_address,supplier_telephone) value ("SOMEONE",'SOMEONE@EMAIL.COM','SOMEWHERE',"201-2929121");

-- add some devices
insert into devices (device_name,device_serial_number,device_description,supplier_id)values("MODEM","19293919292","a modem","1");
insert into devices (device_name,device_serial_number,device_description,supplier_id)values("MODEM","222222","a modem","1");

-- add some plans
insert into plan (plan_name,plan_burst_speed,plan_cost,plan_download_speed,plan_upload_speed)values('FAST','1000GB/s',"$30,000","99999MB/s",'10,000MB/s');
insert into plan (plan_name,plan_burst_speed,plan_cost,plan_download_speed,plan_upload_speed)values('MEDIUM','50GB/s',"$20,000","88888MB/s",'10,000MB/s');
insert into plan (plan_name,plan_burst_speed,plan_cost,plan_download_speed,plan_upload_speed)values('SLOW','10GB/s',"$10,000","55555MB/s",'10,000MB/s');

drop view `customer_details`;
create view `customer_details` as
select customer_id,customer_first_name,customer_last_name,customer_telephone,customer_email,customer_address,plan_name
from customer
join plan on customer_plan = plan_id;

drop view `customer_update`;
create view `customer_update`as
select customer_id,customer_first_name,customer_last_name,customer_telephone,customer_email,customer_address,plan_id
from customer
join plan on customer_plan=plan_id;

drop view `employee_details`;
create view `employee_details` as
select employee_id,employee_first_name,employee_last_name,employee_telephone,employee_email,employee_address,employee_NIS,employee_designation
from employee;

select * from customer_details;
select * from customer_update;
select * from employee_details;


