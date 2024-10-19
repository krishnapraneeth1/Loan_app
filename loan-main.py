import tkinter
#import python ,tkinter, mysql and other libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk
import re
import tkinter as tk
from tkinter import ttk
import webbrowser
import math
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
from tkinter import filedialog
import datetime



#connecting to the database
loan_management_systemdb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Croatia@24",
    #database="loan_management_system"
)

#create if not exists the database and the tables
cursor = loan_management_systemdb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS loan_management_sys")
cursor.execute("USE loan_management_sys")
cursor = loan_management_systemdb.cursor()

# Create the loan table
cursor.execute("""
CREATE TABLE IF NOT EXISTS loan(
    loan_id INT AUTO_INCREMENT PRIMARY KEY, 
    loan_name VARCHAR(45), 
    loan_type VARCHAR(45), 
    loan_amount INT, 
    interest_rate DECIMAL(5,2), 
    loan_term INT, 
    collateral_required VARCHAR(45), 
    min_age INT, 
    max_age INT, 
    min_income INT, 
    credit_score INT, 
    collateral_value INT
)
""")
cursor.execute("CREATE TABLE IF NOT EXISTS user(user_id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), email VARCHAR(255), phoneno VARCHAR(15), address VARCHAR(255), password VARCHAR(255))")
cursor.execute("CREATE TABLE IF NOT EXISTS loan_application(application_id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), email VARCHAR(255), phoneno VARCHAR(15),dob DATE, street_address VARCHAR(255), city VARCHAR(45), state VARCHAR(45), zip_code INT, amount INT, interest_rate DECIMAL(5,2), repayment_schedule VARCHAR(45), collateral_type VARCHAR(45), collateral_value INT, employer_name VARCHAR(45), years_employed INT, annual_income INT, credit_score INT, loan_id INT,user_id INT, loan_decision VARCHAR(45),CONSTRAINT fk_loan FOREIGN KEY (loan_id) REFERENCES loan(loan_id),CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES user(user_id))")
cursor.execute("CREATE TABLE IF NOT EXISTS repayment(repayment_id INT AUTO_INCREMENT PRIMARY KEY, application_id INT, repayment_date DATE, amount_paid DECIMAL(15,2), remaining_balance DECIMAL(15,2), CONSTRAINT fk_application_id FOREIGN KEY (application_id) REFERENCES loan_application(application_id))")

class loan_managnment_system:
        #initializing the class
    def __init__(self, root):
        self.root = root
        self.root.title("FinServe Financial")
        self.root.geometry("1200x750")
        self.root.config(bg="white")
        self.loginscreen()
    
    #function to destroy all the widgets on the screen
    def loginscreen(self):
        for i in self.root.winfo_children():
            i.destroy()
            
        self.login_frame = Frame(self.root, bg="white")
        self.login_frame.place(x=0, y=0, width=1200, height=750)
        
        self.show_pass_var = tk.IntVar()
        self.password_visible = False
        # adding Logindogpage1 image
        self.bg = Image.open("Loan_app/login.png")
        self.bg = self.bg.resize((1200, 750), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg)
        self.bg_image = Label(self.login_frame, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        #adding Welcome text on the top
        self.welcome_label = Label(self.login_frame, text="Welcome to FinServe Financial", font=("calibri", 40,"bold"), bg="#4b5ee5", fg="white")
        self.welcome_label.place(x=30, y=40)
        
        #adding login text to the login page right side
        self.login_label = Label(self.login_frame, text="Login", font=("calibri", 20,"bold"), bg="#4b5ee5", fg="black")
        self.login_label.place(x=900, y=150)
        
        # adding username labels and entry boxes
        self.username_label = Label(self.login_frame, text="Username", font=("calibri", 15,"bold"), bg="#4b5ee5", fg="black")
        self.username_label.place(x=850, y=200)
        self.username_entry = Entry(self.login_frame, font=("calibri", 15), bg="white", fg="black")
        self.username_entry.place(x=850, y=230)
        
        # adding password labels and entry boxes
        self.password_label = Label(self.login_frame, text="Password", font=("calibri", 15,"bold"), bg="#4b5ee5", fg="black")
        self.password_label.place(x=850, y=270)
        self.password_entry = Entry(self.login_frame, font=("calibri", 15), bg="white", fg="black", show="*")
        self.password_entry.place(x=850, y=300)
        
        # adding show password check button
        self.show_pass = Checkbutton(self.login_frame, text="Show Password", variable=self.show_pass_var, onvalue=1, offvalue=0,bg="#4b5ee5", fg="black",activebackground="#4b5ee5")#command=self.show_password
        self.show_pass.place(x=850, y=330)
        
        # adding forgot password button
        self.forgot_pass = Button(self.login_frame, text="Forgot Password?", font=("calibri", 10), bg="#4b5ee5", fg="black", bd=0, cursor="hand2") #command=self.forgot_password
        self.forgot_pass.place(x=850, y=360)
        
        # adding login button with button shape outline
        self.login_button = Button(self.login_frame, text="Login", font=("calibri", 15,"bold"), bg="#4b5ee5", fg="black", bd=1, cursor="hand2",activebackground="#4b5ee5", command=self.login_screen)
        self.login_button.place(x=950, y=390)
        
        # adding register button
        self.register_button = Button(self.login_frame, text="Register", font=("calibri", 15,"bold"), bg="#4b5ee5", fg="black", bd=1, cursor="hand2", activebackground="#4b5ee5", command=self.registerscreen)
        self.register_button.place(x=938, y=440)
        #creating singnup page
        
    def registerscreen(self):
        for i in self.root.winfo_children():
            i.destroy()
        
        self.register_frame = Frame(self.root, bg="white")
        self.register_frame.place(x=0, y=0, width=1200, height=750)
        #adding Registerdogpage1 image
        self.bg = Image.open("Loan_app/register.png")
        self.bg = self.bg.resize((1200, 750), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg)
        self.bg_image = Label(self.register_frame, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        #adding Register text on the
        self.register_lable = Label(self.register_frame, text="Register", font=("calibri", 20,"bold"), bg="white", fg="black")
        self.register_lable.place(x=720, y=100)
        
    
        self.fname_label = Label(self.register_frame, text="First Name", font=("calibri", 15,"bold"), bg="white", fg="black")
        self.fname_label.place(x=550, y=150)
        self.fname_entry = Entry(self.register_frame, font=("calibri", 15), bg="white", fg="black")
        self.fname_entry.place(x=550, y=180)
        
        self.lname_label = Label(self.register_frame, text="Last Name", font=("calibri", 15,"bold"), bg="white", fg="black")
        self.lname_label.place(x=850, y=150)
        self.lname_entry = Entry(self.register_frame, font=("calibri", 15), bg="white", fg="black")
        self.lname_entry.place(x=850, y=180)
        
        self.email_label = Label(self.register_frame, text="Email", font=("calibri", 15,"bold"), bg="white", fg="black")
        self.email_label.place(x=550, y=220)
        self.email_entry = Entry(self.register_frame, font=("calibri", 15), bg="white", fg="black")
        self.email_entry.place(x=550, y=250)
        
        self.address_label = Label(self.register_frame, text="Home Address", font=("calibri", 15,"bold"), bg="white", fg="black")
        self.address_label.place(x=550, y=290)
        self.address_entry = Entry(self.register_frame, font=("calibri", 15), bg="white", fg="black")
        self.address_entry.place(x=550, y=320)
        
        self.phone_label = Label(self.register_frame, text="Phone Number", font=("calibri", 15,"bold"), bg="white", fg="black")
        self.phone_label.place(x=850, y=290)
        self.phone_entry = Entry(self.register_frame, font=("calibri", 15), bg="white", fg="black")
        self.phone_entry.place(x=850, y=320)
        
   
        self.password_label = Label(self.register_frame, text="Password", font=("calibri", 15,"bold"), bg="white", fg="black")
        self.password_label.place(x=550, y=360)
        self.password_entry = Entry(self.register_frame, font=("calibri", 15), bg="white", fg="black", show="*")
        self.password_entry.place(x=550, y=390)
        
        self.confirm_password_label = Label(self.register_frame, text="Confirm Password", font=("calibri", 15,"bold"), bg="white", fg="black")
        self.confirm_password_label.place(x=850, y=360)
        self.confirm_password_entry = Entry(self.register_frame, font=("calibri", 15), bg="white", fg="black", show="*")
        self.confirm_password_entry.place(x=850, y=390)
                 
        self.register_button = Button(self.register_frame, text="Register", font=("calibri", 15,"bold"), bg="white", fg="black", bd=1, cursor="hand2", command=self.register_screen)
        self.register_button.place(x=750, y=450)
        self.login_button = Button(self.register_frame, text="Back to Login", font=("calibri", 15,"bold"), bg="white", fg="black", bd=1, cursor="hand2", command=self.loginscreen)
        self.login_button.place(x=730, y=520)

        #Database connection and adding the signup data to the database
        
    def register_screen(self):
        pass
        firstname = self.fname_entry.get()
        lastname = self.lname_entry.get()
        phoneno = self.phone_entry.get()
        address = self.address_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        # email validation
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror(title="Invalid Email", message="Please enter a valid email address")

        # password validation for length and special characters
        elif not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", password):
            messagebox.showerror(title="Invalid Password", message="Password must contain at least 8 characters, one letter, one number and one special character")

        # phone number validation
        elif not re.match(r"[0-9]{10}", phoneno) and len(phoneno) != 10:
            messagebox.showerror(title="Invalid Phone Number", message="Please enter a valid phone number")

        elif email == "" or password == "":
            messagebox.showerror(title="Fields are empty", message="Create a username and password for your account")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_system")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM user WHERE email = %s", (email,))
            user = cursor.fetchone()
            if user:
                messagebox.showinfo(title="Username exists", message="Username already exists, please try another")
            else:
                # Insert data into the table
                cursor.execute("INSERT INTO user (first_name, last_name, phoneno, address, email, password) VALUES (%s, %s, %s, %s, %s, %s)", (firstname, lastname, phoneno, address, email, password))

                con.commit()
                messagebox.showinfo(title="Account Created", message="Account created successfully")
                con.close()

        # Function for login
    def login_screen(self):
        self.email = self.username_entry.get()
        password = self.password_entry.get()
        
        # checking the email and password with the database
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_system")
        cursor = con.cursor()
        select_data = f"SELECT * FROM user WHERE email = '{self.email}' AND password = '{password}'"
        cursor.execute(select_data)
        user = cursor.fetchone()

        if user:
            self.user_id = user[0]
            self.first_name = user[1]
            self.last_name = user[2]
            self.email = user[3]
            self.phoneno = user[4]
            self.address = user[5]
            self.password = user[6]
            self.user_dashboard()
        elif self.email == "admin" and password == "admin":
             self.adminpage()
        else:
            messagebox.showerror("Error", "Invalid Email or Password")
            return

        
    def adminpage(self):
        for i in self.root.winfo_children():
            i.destroy()

        
        self.admin_frame = Frame(self.root, bg="white")
        self.admin_frame.place(x=0, y=0, width=1200, height=750)
        # Adding Admin Page Background Image
        self.bg_admin = Image.open("Loan_app/adminpage.png")
        self.bg_admin = self.bg_admin.resize((1200, 750), Image.LANCZOS)
        self.bg_admin = ImageTk.PhotoImage(self.bg_admin)
        self.bg_admin_image = Label(self.admin_frame, image=self.bg_admin).place(x=0, y=0, relwidth=1, relheight=1)
        self.admin_frame.place(x=0, y=0, width=1200, height=750)

        self.admin_frame.place(x=0, y=0, width=1200, height=750)
        
        self.admin_label = Label(self.admin_frame, text="Welcome Admin", font=("calibri", 20,"bold"), bg="white", fg="black")
        self.admin_label.place(x=500, y=50)
        
        # Add image as button for add loan
        self.add_loan_image = Image.open("Loan_app/add_loan.png")
        self.add_loan_image = self.add_loan_image.resize((70, 70), Image.LANCZOS)
        self.add_loan_image = ImageTk.PhotoImage(self.add_loan_image)
        self.add_loan_button = Button(self.admin_frame, image=self.add_loan_image, bg="white", bd=0, cursor="hand2",command=self.add_loan)
        self.add_loan_button.place(x=670, y=200)
        
        # add text to the add loan button
        self.add_loan_label = Label(self.admin_frame, text="Add Loan", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.add_loan_label.place(x=660, y=270)

        # add image as button for delete loan
        self.delete_loan_image = Image.open("Loan_app/delete_loan.png")
        self.delete_loan_image = self.delete_loan_image.resize((70, 70), Image.LANCZOS)
        self.delete_loan_image = ImageTk.PhotoImage(self.delete_loan_image)
        self.delete_loan_button = Button(self.admin_frame, image=self.delete_loan_image, bg="white", bd=0, cursor="hand2",command=self.delete_loan)
        self.delete_loan_button.place(x=670, y=350)
        
        # add text to the delete loan button
        self.delete_loan_label = Label(self.admin_frame, text="Delete Loan", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.delete_loan_label.place(x=650, y=420)

        # add image as button for view loan
        self.view_loan_image = Image.open("Loan_app/view_loans.png")
        self.view_loan_image = self.view_loan_image.resize((70, 70), Image.LANCZOS)
        self.view_loan_image = ImageTk.PhotoImage(self.view_loan_image)
        self.view_loan_button = Button(self.admin_frame, image=self.view_loan_image, bg="white", bd=0, cursor="hand2",command=self.manage_loan_applications)
        self.view_loan_button.place(x=670, y=500)
        
        #add image as button for report to the right of the add loan button
        self.report_image = Image.open("Loan_app/report.png")
        self.report_image = self.report_image.resize((70, 70), Image.LANCZOS)
        self.report_image = ImageTk.PhotoImage(self.report_image)
        self.report_button = Button(self.admin_frame, image=self.report_image, bg="white", bd=0, cursor="hand2",command=self.report_page)
        self.report_button.place(x=670, y=640)
        
        #add text to the report button
        self.report_label = Label(self.admin_frame, text="Reports", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.report_label.place(x=670, y=690)
        

        
        # add text to the view loan button
        self.view_loan_label = Label(self.admin_frame, text="View Loan", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.view_loan_label.place(x=650, y=570)

        # add image as button for logout
        self.logout_image = Image.open("Loan_app/logout.png")
        self.logout_image = self.logout_image.resize((70, 70), Image.LANCZOS)
        self.logout_image = ImageTk.PhotoImage(self.logout_image)
        self.logout_button = Button(self.admin_frame, image=self.logout_image, bg="white", bd=0, cursor="hand2",command=self.loginscreen)
        self.logout_button.place(x=1050, y=650)
        
        
    def manage_loan_applications(self):
        # Destroy all widgets in the root window
        for i in self.root.winfo_children():
            i.destroy()
        
        # Create a new frame for managing loan applications
        self.manage_loan_frame = Frame(self.root, bg="white")
        self.manage_loan_frame.place(x=0, y=0, width=1200, height=750)
        
        # Add a label for the frame
        self.manage_loan_label = Label(self.manage_loan_frame, text="Manage Loan Applications", font=("calibri", 20,"bold"), bg="white", fg="black")
        self.manage_loan_label.place(x=500, y=50)
        
        # Back to admin button with image
        self.back_to_admin_image = Image.open("Loan_app/back.png")
        self.back_to_admin_image = self.back_to_admin_image.resize((80, 80), Image.LANCZOS)
        self.back_to_admin_image = ImageTk.PhotoImage(self.back_to_admin_image)
        self.back_to_admin_button = Button(self.manage_loan_frame, image=self.back_to_admin_image, bg="white", bd=0, cursor="hand2", command=self.adminpage)
        self.back_to_admin_button.place(x=1050, y=650)
        
        # Fetch loan applications from the database
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_system")
        cursor = con.cursor()
        cursor.execute("SELECT application_id,loan_id, first_name, last_name, amount, interest_rate, collateral_value, loan_term, repayment_schedule FROM loan_application")
        loans = cursor.fetchall()
        
        y = 150
        for loan in loans:
            print(loan)
            application_id = loan[0]  # application_id is at index 0
            loan_id = loan[1]  # loan_id is at index 1
            first_name = loan[2]  # first_name is at index 2
            last_name = loan[3]  # last_name is at index 3
            loan_amount = loan[4]  # amount is at index 4
            interest_rate = loan[5]  # interest_rate is at index 5
            collateral_value = loan[6]  # collateral_value is at index 6
            loan_term = loan[7]  # loan_term is at index 7
            repayment_schedule = loan[8]  # repayment_schedule is at index 8
            
            loan_details = f"Loan ID: {loan_id}, Amount: ${loan_amount}"
            
            loan_button = Button(self.manage_loan_frame, text=loan_details, font=("calibri", 15), bg="white", fg="black", bd=1, cursor="hand2", command=lambda application_id=application_id: self.loan_decision_details(application_id))
            loan_button.place(x=400, y=y)
            
            y += 50
            
        con.close()

    def loan_decision_details(self,application_id):
        # Clear the frame for loan decision details
        for widget in self.manage_loan_frame.winfo_children():
            widget.destroy()

        # Fetch the specific loan details from the database
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_system")
        cursor = con.cursor()
        cursor.execute("SELECT application_id,loan_id, first_name, last_name, amount, interest_rate, collateral_value, loan_term, repayment_schedule FROM loan_application WHERE application_id = %s", (application_id,))
        loan = cursor.fetchone()
        con.close()
        
        # Display loan decision details
        decision_details = f"""
        APPLICATION ID: {loan[0]}
        Loan ID: {loan[1]}
        Loan Amount: ${loan[4]}
        First Name: {loan[2]}
        Last Name: {loan[3]}
        Interest Rate: {loan[5]}%
        Collateral Value: ${loan[6]}
        Loan Term: {loan[7]} months
        Repayment Schedule: {loan[8]}
        """
        decision_details_label = Label(self.manage_loan_frame, text=decision_details, font=("calibri", 15), bg="white", fg="black")
        decision_details_label.place(x=400, y=150)
        
        # Approve and Reject buttons
        approve_button = Button(self.manage_loan_frame, text="Approve", font=("calibri", 15), bg="green", fg="white", command=lambda: self.process_loan(application_id, "approved"))
        approve_button.place(x=400, y=300)
        
        reject_button = Button(self.manage_loan_frame, text="Reject", font=("calibri", 15), bg="red", fg="white", command=lambda: self.process_loan(application_id, "rejected"))
        reject_button.place(x=550, y=300)
        
        #back to manage loan applications button
        back_to_manage_loan_button = Button(self.manage_loan_frame, text="Back to Manage Loan Applications", font=("calibri", 15), bg="white", fg="black", command=self.manage_loan_applications)
        back_to_manage_loan_button.place(x=400, y=400)

    def process_loan(self, application_id, decision):
        # Update loan decision in the database based on application_id
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_system")
        cursor = con.cursor()
        
        # Update the loan decision (approved/rejected) for the application
        cursor.execute("UPDATE loan_application SET loan_decision = %s WHERE application_id = %s", (decision, application_id))
        con.commit()

        # Fetch the user's email and loan details based on application_id
        cursor.execute("SELECT email, amount, interest_rate, loan_term FROM loan_application WHERE application_id = %s", (application_id,))
        loan_data = cursor.fetchone()
        user_email = loan_data[0]
        loan_amount = loan_data[1]
        interest_rate = loan_data[2]
        loan_term = loan_data[3]
        con.close()

        # Send email to the user with loan details
        self.send_email(user_email, decision, application_id, loan_amount, interest_rate, loan_term)

        # Show confirmation popup for admin
        self.confirmation_popup(decision)

    def send_email(self, recipient_email, decision, application_id, loan_amount, interest_rate, loan_term):
        # Email setup
        sender_email = "apploan99@gmail.com"
        sender_password = "utxn kqpn yoly veqq"  # Use app-specific password

        # Compose the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        
        # Update the subject to include the application_id
        if decision == "approved":
            msg['Subject'] = f"Loan Approved - Application ID: {application_id}"
            body = f"Congratulations! Your loan has been approved.\n\n"
        else:
            msg['Subject'] = f"Loan Rejected - Application ID: {application_id}"
            body = f"We regret to inform you that your loan application has been rejected.\n\n"
        
        # Include loan details in the email body
        body += f"Loan Details:\n" \
                f"Application ID: {application_id}\n" \
                f"Loan Amount: ${loan_amount}\n" \
                f"Interest Rate: {interest_rate}%\n" \
                f"Loan Term: {loan_term} months\n"

        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()

    def confirmation_popup(self, decision):
        popup = Toplevel(self.root)
        popup.title("Confirmation")
        popup.geometry("300x150")
        if decision == "approved":
            Label(popup, text="Email sent! Loan approved.", font=("calibri", 12)).pack(pady=20)
        else:
            Label(popup, text="Email sent! Loan rejected.", font=("calibri", 12)).pack(pady=20)
        Button(popup, text="OK", command=popup.destroy).pack(pady=10)

        
            
        
    def loan_application(self,loan_id):
        self.loan_id = loan_id

        
        for i in self.root.winfo_children():
            i.destroy()
        
        self.loan_frame = Frame(self.root, bg="white")
        self.loan_frame.place(x=0, y=0, width=1200, height=750)
        
        
        # Adding Loan Application Background Image
        self.bg_loan_app = Image.open("Loan_app/loan_appliaction.jpg")
        self.bg_loan_app = self.bg_loan_app.resize((1200, 750), Image.LANCZOS)
        self.bg_loan_app = ImageTk.PhotoImage(self.bg_loan_app)
        self.bg_loan_app_image = Label(self.loan_frame, image=self.bg_loan_app).place(x=0, y=0, relwidth=1, relheight=1)
        
        self.loan_app_label = Label(self.loan_frame, text="Fill Out Loan Application", font=("calibri", 30,"bold"), bg="white", fg="black")
        self.loan_app_label.place(x=40, y=40)
        
        #add borrower deatils to the right of the loan application page
        self.borrower_details_label = Label(self.loan_frame, text="Borrower Details", font=("calibri", 15), bg="white", fg="black")
        self.borrower_details_label.place(x=400, y=120)

        # adding first name label
        self.first_name_label = Label(self.loan_frame, text="First Name", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.first_name_label.place(x=400, y=155)
        self.first_name_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.first_name_entry.place(x=600, y=156)

        self.last_name_label = Label(self.loan_frame, text="Last Name", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.last_name_label.place(x=400, y=200)
        self.last_name_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.last_name_entry.place(x=600, y=200)

        self.email_label = Label(self.loan_frame, text="Email", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.email_label.place(x=400, y=245)
        self.email_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.email_entry.place(x=600, y=245)

        self.phone_number_label = Label(self.loan_frame, text="Phone Number", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.phone_number_label.place(x=400, y=290)
        self.phone_number_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.phone_number_entry.place(x=600, y=290)

        self.street_address_label = Label(self.loan_frame, text="Street Address", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.street_address_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.street_address_label.place(x=820, y=155)
        self.street_address_entry.place(x=970, y=156)

        self.city_label = Label(self.loan_frame, text="City", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.city_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.city_label.place(x=820, y=200)
        self.city_entry.place(x=970, y=200)

        self.state_label = Label(self.loan_frame, text="State", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.state_label.place(x=820, y=245)
        self.state_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.state_entry.place(x=970, y=245)

        self.zip_code_label = Label(self.loan_frame, text="Zip Code", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.zip_code_label.place(x=820, y=290)
        self.zip_code_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.zip_code_entry.place(x=970, y=290)


        self.dob_label = Label(self.loan_frame, text="Date of Birth", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.dob_label.place(x=400, y=335)
        self.dob_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.dob_entry.place(x=600, y=335)

        self.loan_details_label = Label(self.loan_frame, text="Loan Details", font=("calibri", 15), bg="white", fg="black")
        self.loan_details_label.place(x=400, y=380)

        self.loan_amount_label = Label(self.loan_frame, text="Amount", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.loan_amount_label.place(x=400, y=425)
        self.loan_amount_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.loan_amount_entry.place(x=600, y=425)

        # self.loan_term_label = Label(self.loan_frame, text="Loan Term", font=("calibri", 15, "bold"), bg="white", fg="black")
        # self.loan_term_label.place(x=400, y=470)
        # self.loan_term_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        # self.loan_term_entry.place(x=600, y=470)

        self.loan_interest_rate_label = Label(self.loan_frame, text="Interest Rate", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.loan_interest_rate_label.place(x=400, y=515)
        self.loan_interest_rate_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.loan_interest_rate_entry.place(x=600, y=515)

        # self.loan_repayment_schedule_label = Label(self.loan_frame, text="Repayment Schedule", font=("calibri", 15, "bold"), bg="white", fg="black")
        # self.loan_repayment_schedule_label.place(x=400, y=560)
        # self.loan_repayment_schedule_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        # self.loan_repayment_schedule_entry.place(x=600, y=560)
        # add collateral details below the loan details
        self.collateral_details_label = Label(self.loan_frame, text="Collateral Details", font=("calibri", 15), bg="white", fg="black")
        self.collateral_details_label.place(x=400, y=605)
        
        self.collateral_type_label = Label(self.loan_frame, text="Collateral Type", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.collateral_type_label.place(x=400, y=650)
        self.collateral_type_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.collateral_type_entry.place(x=600, y=650)
        
        self.collateral_value_label = Label(self.loan_frame, text="Collateral Value", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.collateral_value_label.place(x=400, y=695)
        self.collateral_value_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.collateral_value_entry.place(x=600, y=695)
        
        # add employment details to the right of the loan application page below the zip code
        self.employment_details_label = Label(self.loan_frame, text="Employment Details", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.employment_details_label.place(x=820, y=380)

        self.employer_name_label = Label(self.loan_frame, text="Employer Name", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.employer_name_label.place(x=820, y=425)
        self.employer_name_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.employer_name_entry.place(x=970, y=425)

        # add years employed label and entry box
        self.years_employed_label = Label(self.loan_frame, text="Years Employed", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.years_employed_label.place(x=820, y=470)
        self.years_employed_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.years_employed_entry.place(x=970, y=470)

        # add annual income label and entry box
        self.annual_income_label = Label(self.loan_frame, text="Annual Income", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.annual_income_label.place(x=820, y=515)
        self.annual_income_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.annual_income_entry.place(x=970, y=515)
        
        # add credit score label and entry box
        self.credit_score_label = Label(self.loan_frame, text="Credit Score", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.credit_score_label.place(x=820, y=560)
        self.credit_score_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.credit_score_entry.place(x=970, y=560)
        
        # add image as button for back to login
        self.back_to_login_image = Image.open("Loan_app/back.png")
        self.back_to_login_image = self.back_to_login_image.resize((80, 80), Image.LANCZOS)
        self.back_to_login_image = ImageTk.PhotoImage(self.back_to_login_image)
        self.back_to_login_button = Button(self.loan_frame, image=self.back_to_login_image, bg="white", bd=0, cursor="hand2", command=self.loginscreen)
        self.back_to_login_button.place(x=1050, y=650)
        
        # add image as button for submit loan application
        self.submit_loan_image = Image.open("Loan_app/submit.png")
        self.submit_loan_image = self.submit_loan_image.resize((60, 60), Image.LANCZOS)
        self.submit_loan_image = ImageTk.PhotoImage(self.submit_loan_image)
        self.submit_loan_button = Button(self.loan_frame, image=self.submit_loan_image, bg="white", bd=0, cursor="hand2",command=self.submit_loan)
        self.submit_loan_button.place(x=950, y=670)
        

    def submit_loan(self):
        # Get user-entered details
        self.first_name = self.first_name_entry.get()
        self.last_name = self.last_name_entry.get()
        self.email = self.email_entry.get()
        self.phone_number = self.phone_number_entry.get()
        self.street_address = self.street_address_entry.get()
        self.city = self.city_entry.get()
        self.state = self.state_entry.get()
        self.zip_code = self.zip_code_entry.get()
        self.dob = self.dob_entry.get()
        self.loan_amount = float(self.loan_amount_entry.get())
        # self.loan_term = int(self.loan_term_entry.get())  # Loan term in months
        self.collateral_type = self.collateral_type_entry.get()
        self.collateral_value = float(self.collateral_value_entry.get())
        self.employer_name = self.employer_name_entry.get()
        self.years_employed = self.years_employed_entry.get()
        self.annual_income = float(self.annual_income_entry.get())
        self.credit_score = int(self.credit_score_entry.get())

        # Assuming the following details were already fetched during loan display
        loan_id = self.loan_id  # Ensure `loan_id` is stored when the user selects a loan
        loan_details = self.show_loan_details(loan_id)

        # Extract loan requirements
        self.min_age = loan_details["min_age"]
        self.max_age = loan_details["max_age"]
        self.min_income = loan_details["min_income"]
        self.required_credit_score = loan_details["credit_score"]
        self.required_collateral_value = loan_details["collateral_value"]

        # Validation Logic
        errors = []
        
        # Validate age (assuming dob is provided in YYYY-MM-DD format)
        import datetime
        today = datetime.date.today()
        dob_date = datetime.datetime.strptime(self.dob, "%Y-%m-%d").date()
        self.dob = dob_date
        age = (today - dob_date).days // 365

        if not (self.min_age <= age <= self.max_age):
            errors.append(f"Applicant's age must be between {self.min_age} and {self.max_age} years.")

        # Validate annual income
        if self.annual_income < self.min_income:
            errors.append(f"Applicant's annual income must be at least {self.min_income}.")

        # Validate credit score
        if self.credit_score < self.required_credit_score:
            errors.append(f"Applicant's credit score must be at least {self.required_credit_score}.")

        # Validate collateral value
        if self.collateral_value < self.required_collateral_value:
            errors.append(f"Collateral value must be at least {self.required_collateral_value}.")

        # If there are any errors, display them
        if errors:
            error_message = "\n".join(errors)
            messagebox.showerror("Loan Application Error", error_message)
            return

        # Determine the interest rate and loan term based on credit score and income
        interest_rate, repayment_schedule = self.calculate_loan_quote(self.loan_amount, self.credit_score, self.annual_income)

        self.interest_rate = interest_rate
        self.repayment_schedule = repayment_schedule
        print(f"Repayment Schedule : {repayment_schedule}%")
        # Show the loan quote with repayment plan
        self.show_quote_screen(self.loan_amount, interest_rate, repayment_schedule,self.loan_term)

    def calculate_loan_quote(self, loan_amount, credit_score, annual_income):
        """
        Calculate the interest rate and repayment schedule based on the user's credit score, loan amount, and income.
        """
        # Determine interest rate based on credit score
        if credit_score >= 700:
            interest_rate = 5.0  # Lower rate for good credit
        elif 600 <= credit_score < 700:
            interest_rate = 8.0  # Medium rate for average credit
        else:
            interest_rate = 12.0  # Higher rate for low credit

        # Adjust loan term based on loan amount and income
        if loan_amount >= 100000 and annual_income >= 100000:
            loan_term = 360  # Long term for high income and large loan (30 years)
        elif 50000 <= loan_amount < 100000 and annual_income >= 50000:
            loan_term = 180  # Medium term (15 years)
        else:
            loan_term = 60  # Short term for small loan (5 years)

        # Calculate monthly repayment using the amortization formula
        monthly_interest_rate = (interest_rate / 100) / 12
        repayment_schedule = self.calculate_repayment_plan(loan_amount, monthly_interest_rate, loan_term)
        self.loan_term = loan_term
        return interest_rate, repayment_schedule

    def calculate_repayment_plan(self, loan_amount, monthly_interest_rate, loan_term):
        """
        Calculate the monthly payment using the loan amortization formula.
        """
        if monthly_interest_rate == 0:
            monthly_payment = loan_amount / loan_term
        else:
            monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term) / ((1 + monthly_interest_rate) ** loan_term - 1)

        return f"${round(monthly_payment, 2)} per month for {loan_term} months"

    def show_quote_screen(self, loan_amount, interest_rate, repayment_schedule,loan_term):
        """
        Show the loan quote screen with the calculated loan amount, term, interest rate, and repayment schedule.
        """
        # Destroy previous screen elements
        for i in self.root.winfo_children():
            i.destroy()

        # Create the quote screen frame
        self.quote_frame = Frame(self.root, bg="white")
        self.quote_frame.place(x=0, y=0, width=1200, height=750)

        # Display the loan quote details
        quote_text = f"""
        Your Loan Quote:
        -----------------
        Loan Amount: ${loan_amount}
        Loan Term: {loan_term} months
        Interest Rate: {interest_rate}%
        Repayment Schedule: {repayment_schedule}
        """

        self.quote_label = Label(self.quote_frame, text=quote_text, font=("calibri", 20), bg="white", fg="black")
        self.quote_label.place(x=400, y=200)

        # Add Agree button
        self.agree_button = Button(self.quote_frame, text="Agree", font=("calibri", 15), bg="green", fg="white", command=self.agree_to_loan)
        self.agree_button.place(x=500, y=400)

        # Add Cancel button
        self.cancel_button = Button(self.quote_frame, text="Cancel", font=("calibri", 15), bg="red", fg="white", command=self.userpage)
        self.cancel_button.place(x=700, y=400)

    def agree_to_loan(self):
        # Once the user agrees, we submit the loan application to the database
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_system")
            cursor = con.cursor()

            # Insert loan application into the loan_application table
            cursor.execute("""
                INSERT INTO loan_application (
                    first_name, last_name, email, phone_number, dob, street_address, city, state, zip_code,
                    amount, loan_term, interest_rate, repayment_schedule, collateral_type, collateral_value,
                    employer_name, years_employed, annual_income, credit_score, loan_id, user_id
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                self.first_name, self.last_name, self.email, self.phone_number,
                self.dob, self.street_address, self.city, self.state, self.zip_code,
                self.loan_amount, self.loan_term, self.interest_rate,self.repayment_schedule,
                self.collateral_type, self.collateral_value,
                self.employer_name, self.years_employed, self.annual_income,
                self.credit_score, self.loan_id, self.user_id
            ))
            print(f"Repayment Schedule : {self.repayment_schedule}%")
            # Commit the transaction
            con.commit()
            con.close()

            # Show confirmation message
            messagebox.showinfo("Submitted", "Application has been submitted successfully.The final decision will be sent to your email.")
            self.userpage()  # Go back to user screen

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error occurred: {err}")
            
                
        #creating add loan page
    def add_loan(self):
        for i in self.root.winfo_children():
            i.destroy()
        
        self.add_loan_frame = Frame(self.root, bg="white")
        self.add_loan_frame.place(x=0, y=0, width=1200, height=750)
        
        # Adding Add Loan Background Image
        self.bg_add_loan = Image.open("Loan_app/add_loan_details.png")
        self.bg_add_loan = self.bg_add_loan.resize((1200, 750), Image.LANCZOS)
        self.bg_add_loan = ImageTk.PhotoImage(self.bg_add_loan)
        self.bg_add_loan_image = Label(self.add_loan_frame, image=self.bg_add_loan).place(x=0, y=0, relwidth=1, relheight=1)
        
        self.add_loan_label = Label(self.add_loan_frame, text="Add Loan Details", font=("calibri", 30, "bold"), bg="white", fg="black")
        self.add_loan_label.place(x=40, y=50)

        # add loan name label and entry box
        self.loan_name_label = Label(self.add_loan_frame, text="Loan Name", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.loan_name_label.place(x=500, y=120)
        self.loan_name_entry = Entry(self.add_loan_frame, font=("calibri", 15), bg="white", fg="black", width=20)
        self.loan_name_entry.place(x=650, y=120)

        # add loan type label and drop down box
        self.loan_type_label = Label(self.add_loan_frame, text="Loan Type", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.loan_type_label.place(x=500, y=170)
        self.loan_type_entry = ttk.Combobox(self.add_loan_frame, font=("calibri", 15), state="readonly", width=8)
        self.loan_type_entry["values"] = ["Personal Loan", "Home Loan", "Car Loan", "Business Loan"]
        self.loan_type_entry.place(x=650, y=170)

        # add loan amount label and entry box
        self.loan_amount_label = Label(self.add_loan_frame, text="Loan Amount", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.loan_amount_label.place(x=500, y=220)
        self.loan_amount_entry = Entry(self.add_loan_frame, font=("calibri", 15), bg="white", fg="black", width=8)
        self.loan_amount_entry.place(x=650, y=220)

        # add loan interest rate label and entry box
        self.loan_interest_rate_label = Label(self.add_loan_frame, text="Interest Rate", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.loan_interest_rate_label.place(x=500, y=270)
        self.loan_interest_rate_entry = Entry(self.add_loan_frame, font=("calibri", 15), bg="white", fg="black", width=8)
        self.loan_interest_rate_entry.place(x=650, y=270)

        # add loan term label and entry box
        self.loan_term_label = Label(self.add_loan_frame, text="Loan Term", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.loan_term_label.place(x=500, y=320)
        self.loan_term_entry = Entry(self.add_loan_frame, font=("calibri", 15), bg="white", fg="black", width=8)
        self.loan_term_entry.place(x=650, y=320)

        # collateral required label and drop down box
        self.collateral_required_label = Label(self.add_loan_frame, text="Collateral Required", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.collateral_required_label.place(x=500, y=370)
        self.collateral_required_entry = ttk.Combobox(self.add_loan_frame, font=("calibri", 15), state="readonly", width=8)
        self.collateral_required_entry["values"] = ["Yes", "No"]
        self.collateral_required_entry.place(x=670, y=370)
        
        # add conditions label to the right of the page
        self.conditions_label = Label(self.add_loan_frame, text="Loan Conditions", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.conditions_label.place(x=950, y=80)
        
        # add minimum age label and entry box
        self.min_age_label = Label(self.add_loan_frame, text="Minimum Age", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.min_age_label.place(x=870, y=120)
        self.min_age_entry = Entry(self.add_loan_frame, font=("calibri", 15), bg="white", fg="black", width=8)
        self.min_age_entry.place(x=1040, y=120)

        # add maximum age label and entry box
        self.max_age_label = Label(self.add_loan_frame, text="Maximum Age", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.max_age_label.place(x=870, y=170)
        self.max_age_entry = Entry(self.add_loan_frame, font=("calibri", 15), bg="white", fg="black", width=8)
        self.max_age_entry.place(x=1040, y=170)

        # add minimum income label and entry box
        self.min_income_label = Label(self.add_loan_frame, text="Minimum Income", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.min_income_label.place(x=870, y=220)
        self.min_income_entry = Entry(self.add_loan_frame, font=("calibri", 15), bg="white", fg="black", width=8)
        self.min_income_entry.place(x=1040, y=220)

        # add credit score label and entry box
        self.credit_score_label = Label(self.add_loan_frame, text="Credit Score", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.credit_score_label.place(x=870, y=270)
        self.credit_score_entry = Entry(self.add_loan_frame, font=("calibri", 15), bg="white", fg="black", width=8)
        self.credit_score_entry.place(x=1040, y=270)
        # add collateral value label and entry box
        self.collateral_value_label = Label(self.add_loan_frame, text="Collateral Value", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.collateral_value_label.place(x=870, y=320)
        self.collateral_value_entry = Entry(self.add_loan_frame, font=("calibri", 15), bg="white", fg="black", width=8)
        self.collateral_value_entry.place(x=1040, y=320)
        # add image as button for submit loan details
        self.submit_loan_details_image = Image.open("Loan_app/submit.png")
        self.submit_loan_details_image = self.submit_loan_details_image.resize((70, 70), Image.LANCZOS)
        self.submit_loan_details_image = ImageTk.PhotoImage(self.submit_loan_details_image)
        self.submit_loan_details_button = Button(self.add_loan_frame, image=self.submit_loan_details_image, bg="white", bd=0, cursor="hand2", command=self.publish_loan)
        self.submit_loan_details_button.place(x=690, y=440)
        
        # add image as button for back to admin page
        self.back_to_admin_image = Image.open("Loan_app/back.png")
        self.back_to_admin_image = self.back_to_admin_image.resize((70, 70), Image.LANCZOS)
        self.back_to_admin_image = ImageTk.PhotoImage(self.back_to_admin_image)
        self.back_to_admin_button = Button(self.add_loan_frame, image=self.back_to_admin_image, bg="white", bd=0, cursor="hand2", command=self.adminpage)
        self.back_to_admin_button.place(x=1050, y=650)
    
    # report page
    def report_page(self):
        for i in self.root.winfo_children():
            i.destroy()
        
        self.report_frame = Frame(self.root, bg="white")
        self.report_frame.place(x=0, y=0, width=1200, height=750)
        
        # Adding Report Background Image
        self.bg_report = Image.open("Loan_app/reports_page.jpg")
        self.bg_report = self.bg_report.resize((1200, 750), Image.LANCZOS)
        self.bg_report = ImageTk.PhotoImage(self.bg_report)
        self.bg_report_image = Label(self.report_frame, image=self.bg_report).place(x=0, y=0, relwidth=1, relheight=1)
        
        self.report_label = Label(self.report_frame, text="Loan Applications", font=("calibri", 30, "bold"), bg="white", fg="black")
        self.report_label.place(x=40, y=30)
        
        #add image as button for back to admin page
        self.back_to_admin_image = Image.open("Loan_app/apply.png")
        self.back_to_admin_image = self.back_to_admin_image.resize((70, 70), Image.LANCZOS)
        self.back_to_admin_image = ImageTk.PhotoImage(self.back_to_admin_image)
        self.back_to_admin_button = Button(self.report_frame, image=self.back_to_admin_image, bg="white", bd=0, cursor="hand2", command=self.adminpage)
        self.back_to_admin_button.place(x=1050, y=650)
        
        #generte a report of loan applications from the database saying which user applied for which loan
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_system")
        cursor = con.cursor()
        cursor.execute("SELECT application_id, loan_id, user_id, first_name, amount, interest_rate, repayment_schedule FROM loan_application")
        loan_applications = cursor.fetchall()
        con.close()
        
        # Display the loan applications in a table
        self.report_table = ttk.Treeview(self.report_frame, columns=("Application ID" ,"Loan ID", "User ID", "First name","Amount", "Interest Rate", "Repayment Schedule"), show="headings", height=20)
        self.report_table.place(x=40, y=120)
        self.report_table.heading("Application ID", text="Application ID")
        self.report_table.heading("Loan ID", text="Loan ID")
        self.report_table.heading("User ID", text="User ID")
        self.report_table.heading("First name", text="First name")
        self.report_table.heading("Amount", text="Amount")
        self.report_table.heading("Interest Rate", text="Interest Rate")
        self.report_table.heading("Repayment Schedule", text="Repayment Schedule")
        
        for loan_application in loan_applications:
            self.report_table.insert("", "end", values=loan_application)
        
            
        #download the report as a csv file
        self.download_button = Button(self.report_frame, text="Download Report", font=("calibri", 15), bg="green", fg="white", command=self.download_report)
        self.download_button.place(x=40, y=650)
        
        #add timestamp to the report beside the heading
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.timestamp_label = Label(self.report_frame, text=f"Report generated at: {timestamp}", font=("calibri", 15), bg="white", fg="black")
        self.timestamp_label.place(x=40, y=90)
        
        
    
    def download_report(self):
    # Connect to the database and fetch loan applications
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_system")
        cursor = con.cursor()
        
        # Corrected SQL query
        cursor.execute("SELECT application_id, loan_id, user_id, first_name, amount, interest_rate, repayment_schedule FROM loan_application")
        loan_applications = cursor.fetchall()
        con.close()

        # Ask the user for a file location to save the CSV file
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            # Get the current timestamp
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # Write the loan applications to the CSV file with the timestamp at the top
            with open(file_path, "w", newline="") as file:
                csv_writer = csv.writer(file)
                
                # Write the timestamp as the first row
                csv_writer.writerow([f"Timestamp: {timestamp}"])
                
                # Write the header row
                csv_writer.writerow(["Application ID", "Loan ID", "User ID", "First name", "Amount", "Interest Rate", "Repayment Schedule"])
                
                # Write the loan application rows
                csv_writer.writerows(loan_applications)
            
            # Show success message
            messagebox.showinfo("Report Downloaded", "Report has been downloaded successfully.")

  
    def repayment_page(self):
        for i in self.root.winfo_children():
            i.destroy()
        
        self.repayment_frame = Frame(self.root, bg="white")
        self.repayment_frame.place(x=0, y=0, width=1200, height=750)
        
        # Adding Repayment Background Image
        self.bg_repayment = Image.open("Loan_app/repayment_screen.jpg")
        self.bg_repayment = self.bg_repayment.resize((1200, 750), Image.LANCZOS)
        self.bg_repayment = ImageTk.PhotoImage(self.bg_repayment)
        self.bg_repayment_image = Label(self.repayment_frame, image=self.bg_repayment).place(x=0, y=0, relwidth=1, relheight=1)
        
        self.repayment_label = Label(self.repayment_frame, text="Repayment Schedule", font=("calibri", 30, "bold"), bg="white", fg="black")
        self.repayment_label.place(x=40, y=50)
 
        # add image as button for back to admin page
        self.back_to_admin_image = Image.open("Loan_app/back.png")
        self.back_to_admin_image = self.back_to_admin_image.resize((70, 70), Image.LANCZOS)
        self.back_to_admin_image = ImageTk.PhotoImage(self.back_to_admin_image)
        self.back_to_admin_button = Button(self.repayment_frame, image=self.back_to_admin_image, bg="white", bd=0, cursor="hand2", command=self.loginscreen)
        self.back_to_admin_button.place(x=1050, y=650)
    
    
    def publish_loan(self):
        loan_name = self.loan_name_entry.get()
        loan_type = self.loan_type_entry.get()
        loan_amount = self.loan_amount_entry.get()
        loan_interest_rate = self.loan_interest_rate_entry.get()
        loan_term = self.loan_term_entry.get()
        collateral_required = self.collateral_required_entry.get()
        min_age = self.min_age_entry.get()
        max_age = self.max_age_entry.get()
        min_income = self.min_income_entry.get()
        credit_score = self.credit_score_entry.get()
        collateral_value = self.collateral_value_entry.get()
        
        if loan_name == "" or loan_type == "" or loan_amount == "" or loan_interest_rate == "" or loan_term == "" or collateral_required == "" or min_age == "" or max_age == "" or min_income == "" or credit_score == "" or collateral_value == "":
            messagebox.showerror(title="Empty Fields", message="Please fill out all fields")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_system")
            cursor = con.cursor()
            cursor.execute("INSERT INTO loan (loan_name, loan_type, loan_amount, interest_rate, loan_term, collateral_required, min_age, max_age, min_income, credit_score, collateral_value) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (loan_name, loan_type, loan_amount, loan_interest_rate, loan_term, collateral_required, min_age, max_age, min_income, credit_score, collateral_value))
            con.commit()
            messagebox.showinfo(title="Loan Added", message="Loan details added successfully")
            con.close()
            
        

        
        # creating delete loan page
    def delete_loan(self):
        for i in self.root.winfo_children():
            i.destroy()
        
        self.delete_loan_frame = Frame(self.root, bg="white")
        self.delete_loan_frame.place(x=0, y=0, width=1200, height=750)
        
        # Adding Delete Loan Background Image
        self.bg_delete_loan = Image.open("Loan_app\delete_loan_deatils.jpg")
        self.bg_delete_loan = self.bg_delete_loan.resize((1200, 750), Image.LANCZOS)
        self.bg_delete_loan = ImageTk.PhotoImage(self.bg_delete_loan)
        self.bg_delete_loan_image = Label(self.delete_loan_frame, image=self.bg_delete_loan).place(x=0, y=0, relwidth=1, relheight=1)
        
        self.delete_loan_label = Label(self.delete_loan_frame, text="Delete Loan Details", font=("calibri", 30, "bold"), bg="white", fg="black")
        self.delete_loan_label.place(x=40, y=50)

        # add loan name label and entry box
        self.loan_name_label = Label(self.delete_loan_frame, text="Loan Name", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.loan_name_label.place(x=500, y=120)
        self.loan_name_entry = Entry(self.delete_loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.loan_name_entry.place(x=650, y=120)
        
        # add image as button for submit loan details
        self.submit_loan_details_image = Image.open("Loan_app/submit.png")
        self.submit_loan_details_image = self.submit_loan_details_image.resize((70, 70), Image.LANCZOS)
        self.submit_loan_details_image = ImageTk.PhotoImage(self.submit_loan_details_image)
        self.submit_loan_details_button = Button(self.delete_loan_frame, image=self.submit_loan_details_image, bg="white", bd=0, cursor="hand2")
        self.submit_loan_details_button.place(x=690, y=200)
        
        # add image as button for back to admin page
        self.back_to_admin_image = Image.open("Loan_app/back.png")
        self.back_to_admin_image = self.back_to_admin_image.resize((70, 70), Image.LANCZOS)
        self.back_to_admin_image = ImageTk.PhotoImage(self.back_to_admin_image)
        self.back_to_admin_button = Button(self.delete_loan_frame, image=self.back_to_admin_image, bg="white", bd=0, cursor="hand2", command=self.adminpage)
        self.back_to_admin_button.place(x=1050, y=650)
        

        #creating user page
    def userpage(self):
        for i in self.root.winfo_children():
            i.destroy()
        
        self.user_frame = Frame(self.root, bg="white")
        self.user_frame.place(x=0, y=0, width=1200, height=750)
        
        # Adding User Page Background Image
        self.bg_user = Image.open("Loan_app/user_page.jpg")
        self.bg_user = self.bg_user.resize((1200, 750), Image.LANCZOS)
        self.bg_user = ImageTk.PhotoImage(self.bg_user)
        self.bg_user_image = Label(self.user_frame, image=self.bg_user).place(x=0, y=0, relwidth=1, relheight=1)
        
        self.user_label = Label(self.user_frame, text="Welcome User", font=("calibri", 20, "bold"), bg="white", fg="black")
        self.user_label.place(x=500, y=50)
        
        # Fetch published loans from the database
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_system")
        cursor = con.cursor()
        cursor.execute("SELECT loan_id, loan_name, loan_type FROM loan")
        loans = cursor.fetchall()
        con.close()
        print(loans)
        # Display the loans as clickable buttons
        y_offset = 150
        for loan in loans:
            loan_id = loan[0]
            loan_name = loan[1]
            loan_type = loan[2]
            
            loan_button = Button(self.user_frame, text=f"{loan_name} ({loan_type})", font=("calibri", 15), bg="white", fg="black", cursor="hand2", command=lambda loan_id=loan_id: self.show_loan_details(loan_id))
            loan_button.place(x=500, y=y_offset)
            y_offset += 50
            
        
        
        # Add image as button for back to login
        self.back_to_login_image = Image.open("Loan_app/back.png")
        self.back_to_login_image = self.back_to_login_image.resize((80, 80), Image.LANCZOS)
        self.back_to_login_image = ImageTk.PhotoImage(self.back_to_login_image)
        self.back_to_login_button = Button(self.user_frame, image=self.back_to_login_image, bg="white", bd=0, cursor="hand2", command=self.user_dashboard)
        self.back_to_login_button.place(x=1050, y=650)
        
        
        
        
    def show_loan_details(self, loan_id):
         # Implementation of the show_loan_details method as described earlier
        for i in self.root.winfo_children():
            i.destroy()
        
        self.loan_details_frame = Frame(self.root, bg="white")
        self.loan_details_frame.place(x=0, y=0, width=1200, height=750)
        
        
        
        # Fetch loan details from the database using the loan_id
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_system")
        cursor = con.cursor()
        cursor.execute("SELECT loan_name, loan_type, loan_amount, interest_rate, loan_term, min_age, max_age, min_income, credit_score, collateral_value FROM loan WHERE loan_id = %s", (loan_id,))
        loan = cursor.fetchone()
        con.close()

        # Display loan details
        loan_name = loan[0]
        loan_type = loan[1]
        loan_amount = loan[2]
        interest_rate = loan[3]
        loan_term = loan[4]
        min_age = loan[5]
        max_age = loan[6]
        min_income = loan[7]
        credit_score = loan[8]
        collateral_value = loan[9]
        
        self.loan_details_label = Label(self.loan_details_frame, text=f"Loan Details for {loan_name}", font=("calibri", 20, "bold"), bg="white", fg="black")
        self.loan_details_label.place(x=500, y=50)
        
        details_text = f"""
        Loan Type: {loan_type}
        Loan Amount: {loan_amount}
        Interest Rate: {interest_rate}%
        Loan Term: {loan_term} months
        Minimum Age: {min_age}
        Maximum Age: {max_age}
        Minimum Income: {min_income}
        Required Credit Score: {credit_score}
        Collateral Value: {collateral_value}
        """

        self.loan_details = Label(self.loan_details_frame, text=details_text, font=("calibri", 15), bg="white", fg="black", justify=LEFT)
        self.loan_details.place(x=500, y=120)
        
        #add a note to the user saying details may vary based on user profile and details
        self.note_label = Label(self.loan_details_frame, text="Note: Loan details may vary based on user profile and details", font=("calibri", 15), bg="white", fg="black")
        self.note_label.place(x=500, y=500)
        
        
      
       # Add apply loan image as a button (positioned after loan details)
        self.apply_loan_image = Image.open("Loan_app/apply.png")
        self.apply_loan_image = self.apply_loan_image.resize((70, 70), Image.LANCZOS)
        self.apply_loan_image = ImageTk.PhotoImage(self.apply_loan_image)
        self.apply_loan_button = Button(self.loan_details_frame, image=self.apply_loan_image, bg="white", bd=0, cursor="hand2", command=lambda: self.loan_application(loan_id))
        self.apply_loan_button.place(x=900, y=300)  # Adjust the position as needed# Add apply loan image as a button (positioned after loan details)
        
        # Add back to user page button
        self.back_to_user_image = Image.open("Loan_app/back.png")
        self.back_to_user_image = self.back_to_user_image.resize((70, 70), Image.LANCZOS)
        self.back_to_user_image = ImageTk.PhotoImage(self.back_to_user_image)
        self.back_to_user_button = Button(self.loan_details_frame, image=self.back_to_user_image, bg="white", bd=0, cursor="hand2", command=self.userpage)
        self.back_to_user_button.place(x=1050, y=650)
        
        return {
        "loan_name": loan_name,
        "loan_type": loan_type,
        "loan_amount": loan_amount,
        "interest_rate": interest_rate,
        "loan_term": loan_term,
        "min_age": min_age,
        "max_age": max_age,
        "min_income": min_income,
        "credit_score": credit_score,
        "collateral_value": collateral_value
    }
        
    #creating a user dashboard
    def user_dashboard(self):
        for i in self.root.winfo_children():
            i.destroy()
        
        self.user_dashboard_frame = Frame(self.root, bg="white")
        self.user_dashboard_frame.place(x=0, y=0, width=1200, height=750)
        
        # Adding User Dashboard Background Image
        self.bg_user_dashboard = Image.open("Loan_app/dashboard.jpg")
        self.bg_user_dashboard = self.bg_user_dashboard.resize((1200, 750), Image.LANCZOS)
        self.bg_user_dashboard = ImageTk.PhotoImage(self.bg_user_dashboard)
        self.bg_user_dashboard_image = Label(self.user_dashboard_frame, image=self.bg_user_dashboard).place(x=0, y=0, relwidth=1, relheight=1)
        
        self.user_dashboard_label = Label(self.user_dashboard_frame, text="User Dashboard", font=("calibri", 20, "bold"), bg="white", fg="black")
        self.user_dashboard_label.place(x=500, y=50)
        
        # Add image as button for view loans
        self.view_loans_image = Image.open("Loan_app/loan.png")
        self.view_loans_image = self.view_loans_image.resize((70, 70), Image.LANCZOS)
        self.view_loans_image = ImageTk.PhotoImage(self.view_loans_image)
        self.view_loans_button = Button(self.user_dashboard_frame, image=self.view_loans_image, bg="white", bd=0, cursor="hand2", command=self.userpage)
        self.view_loans_button.place(x=500, y=200)
        
        # Add image as button for view loan applications
        self.view_loan_applications_image = Image.open("Loan_app/personal.png")
        self.view_loan_applications_image = self.view_loan_applications_image.resize((70, 70), Image.LANCZOS)
        self.view_loan_applications_image = ImageTk.PhotoImage(self.view_loan_applications_image)
        self.view_loan_applications_button = Button(self.user_dashboard_frame, image=self.view_loan_applications_image, bg="white", bd=0, cursor="hand2",command=self.view_loan_applications)
        self.view_loan_applications_button.place(x=700, y=200)
        

        
        
        # Add image as button for logout
        self.logout_image = Image.open("Loan_app/logout.png")
        self.logout_image = self.logout_image.resize((70, 70), Image.LANCZOS)
        self.logout_image = ImageTk.PhotoImage(self.logout_image)
        self.logout_button = Button(self.user_dashboard_frame, image=self.logout_image, bg="white", bd=0, cursor="hand2", command=self.loginscreen)
        self.logout_button.place(x=1050, y=650)
        
    def view_loan_applications(self):
        for i in self.root.winfo_children():
            i.destroy()
            
        self.user_dashboard_frame = Frame(self.root, bg="white")
        self.user_dashboard_frame.place(x=0, y=0, width=1200, height=750)
        
        
        # fetch loan details from loan_application table for the user with status of the loan
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_system")
        cursor = con.cursor()
        cursor.execute("SELECT loan_id, amount, loan_decision,application_id FROM loan_application WHERE user_id = %s", (self.user_id,))
        loan_applications = cursor.fetchall()
        con.close()
        print(loan_applications)
        # Display the loan applications as clickable buttons
        y_offset = 150
        for loan_application in loan_applications:
            loan_id = loan_application[0]
            loan_amount = loan_application[1]
            loan_decision = loan_application[2]
            application_id = loan_application[3]
            
            loan_application_button = Button(self.user_dashboard_frame, text=f" ({loan_amount}) - {loan_decision}", font=("calibri", 15), bg="white", fg="black", cursor="hand2", command=lambda application_id=application_id: self.show_loan_application(application_id))
            loan_application_button.place(x=500, y=y_offset)
            y_offset += 50
            
    def show_loan_application(self, application_id):
        # Fetch loan application details from the database using the loan_id
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_system")
        cursor = con.cursor()
        
        cursor.execute("SELECT amount, interest_rate, loan_term, repayment_schedule, collateral_type, collateral_value, employer_name, years_employed, annual_income, credit_score, loan_decision FROM loan_application WHERE application_id = %s", (application_id,))
        loan_application = cursor.fetchone()
        con.close()
        
        print(loan_application)
        
        loan_amount = loan_application[0]
        interest_rate = loan_application[1]
        loan_term = loan_application[2]
        repayment_schedule = loan_application[3]
        collateral_type = loan_application[4]
        collateral_value = loan_application[5]
        employer_name = loan_application[6]
        years_employed = loan_application[7]
        annual_income = loan_application[8]
        credit_score = loan_application[9]
        loan_decision = loan_application[10]
        
        
        
        self.loan_application_frame = Frame(self.root, bg="white")
        self.loan_application_frame.place(x=0, y=0, width=1200, height=750)
        
        self.loan_application_label = Label(self.loan_application_frame, text=f"Loan Application for {application_id}\\", font=("calibri", 20, "bold"), bg="white", fg="black")
        self.loan_application_label.place(x=500, y=50)
        
        
        
        application_text = f"""
        Loan Amount: {loan_amount}
        Interest Rate: {interest_rate}%
        Loan Term: {loan_term} months
        Repayment Schedule: {repayment_schedule}
        Collateral Type: {collateral_type}
        Collateral Value: {collateral_value}
        Employer Name: {employer_name}
        Years Employed: {years_employed}
        Annual Income: {annual_income}
        Credit Score: {credit_score}
        loan_decision: {loan_decision}
        """
        
        self.loan_application_details = Label(self.loan_application_frame, text=application_text, font=("calibri", 15), bg="white", fg="black", justify=LEFT)
        self.loan_application_details.place(x=500, y=120)
        
        #add button for repaymeny page
        self.repayment_image = Image.open("Loan_app/repayment.png")
        self.repayment_image = self.repayment_image.resize((70, 70), Image.LANCZOS)
        self.repayment_image = ImageTk.PhotoImage(self.repayment_image)
        self.repayment_button = Button(self.loan_application_frame, image=self.repayment_image, bg="white", bd=0, cursor="hand2", command=self.repayment_page)
        self.repayment_button.place(x=500, y=500)
        
        
        
        # Add back to user dashboard button
        self.back_to_user_dashboard_image = Image.open("Loan_app/back.png")
        self.back_to_user_dashboard_image = self.back_to_user_dashboard_image.resize((70, 70), Image.LANCZOS)
        self.back_to_user_dashboard_image = ImageTk.PhotoImage(self.back_to_user_dashboard_image)
        self.back_to_user_dashboard_button = Button(self.loan_application_frame, image=self.back_to_user_dashboard_image, bg="white", bd=0, cursor="hand2", command=self.user_dashboard)
        self.back_to_user_dashboard_button.place(x=1050, y=650)
        
        
        

        
if __name__ == "__main__":
    root = Tk()
    app = loan_managnment_system(root)
    root.mainloop()
