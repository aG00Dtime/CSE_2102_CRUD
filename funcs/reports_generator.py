import os
from tkinter import messagebox
from tkinter.filedialog import askdirectory

from fpdf import FPDF

from funcs.connector import db_conn

root = os.path.abspath(os.curdir)


def report():
    db = db_conn()
    cur = db.cursor()

    cur.execute('SELECT * FROM USER_ACTIVITY_CUSTOMER')

    customer_table_activity = cur.fetchall()

    cur.execute("SELECT * FROM user_activity_employee")
    employee_table_activity = cur.fetchall()

    cur.execute('SELECT * FROM ACTIVE_CUSTOMERS')
    active_customers = cur.fetchall()

    cur.execute('select * from plan_count')
    plan_count = cur.fetchall()

    db.close()

    pdf = FPDF(format='letter', unit='in')
    pdf.add_page()
    pdf.set_font('Times', '', 12.0)
    epw = pdf.w - 2 * pdf.l_margin
    col_width = epw / 6

    pdf.set_font('Times', 'B', 20.0)
    pdf.cell(epw, 0.0, 'Employee Activity Report', align='C')

    pdf.set_font('Times', '', 10.0)

    pdf.ln(0.7)

    # customer table activity
    pdf.set_font('Times', 'B', 12.0)
    pdf.cell(epw, 0.0, 'Customer Records Activity Report', align='C')

    pdf.set_font('Times', 'B', 10.0)
    pdf.ln(0.2)

    th = pdf.font_size
    headers = ['EMPLOYEE ID', 'USER ID', 'USERNAME', 'FIRST NAME', 'LAST NAME', 'ACTIVITY COUNT']
    for col in headers:
        pdf.cell(col_width, 2 * th, str(col), border=1)
    pdf.ln(2 * th)

    pdf.set_font('Times', '', 10.0)
    for row in customer_table_activity:
        for col in row:
            pdf.cell(col_width, 2 * th, str(col), border=1)
        pdf.ln(2 * th)

    pdf.ln(0.8)

    pdf.set_font('Times', 'B', 12.0)
    pdf.cell(epw, 0.0, 'Employee Records Activity Report', align='C')

    pdf.set_font('Times', 'B', 10.0)
    pdf.ln(0.2)

    th = pdf.font_size

    for col in headers:
        pdf.cell(col_width, 2 * th, str(col), border=1)
    pdf.ln(2 * th)

    pdf.set_font('Times', '', 10.0)
    for row in employee_table_activity:
        for col in row:
            pdf.cell(col_width, 2 * th, str(col), border=1)
        pdf.ln(2 * th)
    pdf.ln(th)

    pdf.add_page()
    pdf.set_font('Times', 'B', 20.0)
    pdf.cell(epw, 0.0, 'Customer Count and subscription Report', align='C')

    pdf.set_font('Times', '', 10.0)

    pdf.ln(0.7)

    col_width = epw / 2
    # active customers
    pdf.set_font('Times', 'B', 12.0)
    pdf.cell(epw, 0.0, 'Customer Report', align='C')
    pdf.ln(0.3)

    headers = ['CUSTOMER COUNT', 'ACTIVE SUBSCRIPTIONS']
    for col in headers:
        pdf.cell(col_width, 2 * th, str(col), border=1)
    pdf.ln(2 * th)

    pdf.set_font('Times', '', 10.0)
    for row in active_customers:
        for col in row:
            pdf.cell(col_width, 2 * th, str(col), border=1)
        pdf.ln(2 * th)
    pdf.ln(2 * th)
    # plans
    pdf.set_font('Times', 'B', 12.0)
    pdf.cell(epw, 0.0, 'Subscription Report', align='C')
    pdf.ln(0.3)
    headers = ['PLAN NAME', 'SUBSCRIPTION COUNT']

    for col in headers:
        pdf.cell(col_width, 2 * th, str(col), border=1)
    pdf.ln(2 * th)
    pdf.set_font('Times', '', 10.0)
    for row in plan_count:
        for col in row:
            pdf.cell(col_width, 2 * th, str(col), border=1)
        pdf.ln(2 * th)
    pdf.ln(2 * th)

    save_dir = askdirectory()

    save_path = os.path.join(save_dir, "SMJ-REPORT.pdf")

    if save_path:
        pdf.output(save_path)
        messagebox.showinfo(title="Done", message="Report created")
