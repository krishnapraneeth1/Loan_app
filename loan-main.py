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


#connecting to the database
# loan_management_systemdb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Croatia@24",
#     database="loan_management_system"
# )


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
        self.bg = Image.open("Loan_app\login.png")
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
        self.login_button = Button(self.login_frame, text="Login", font=("calibri", 15,"bold"), bg="#4b5ee5", fg="black", bd=1, cursor="hand2",activebackground="#4b5ee5", command=self.adminpage)
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
        self.bg = Image.open("Loan_app\register.png")
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
        self.adminpage()
        e_username = self.username_entry.get()
        e_password = self.password_entry.get()

        if e_username == "" or e_password == "":
            messagebox.showerror(title="Fields are empty", message="Please enter your username and password")
        else:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Croatia@24",
                database="loan_management_system"
            )
            cursor = con.cursor()
            cursor.execute("SELECT * FROM user WHERE email = %s AND password = %s", (e_username, e_password))
            self.user = cursor.fetchone()

            if self.user:
                messagebox.showinfo(title="Login successful", message="Welcome, " + e_username)
                if self.user[3] == 'admin':
                    self.adminpage()
                else:
                    self.catalog()
            else:
                messagebox.showinfo(title="Login Unsuccessful", message="Username or Password are incorrect. If you are a new user, create a new account")
            con.commit()
            con.close()
        
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
        self.view_loan_button = Button(self.admin_frame, image=self.view_loan_image, bg="white", bd=0, cursor="hand2")
        self.view_loan_button.place(x=670, y=500)
        
        # add text to the view loan button
        self.view_loan_label = Label(self.admin_frame, text="View Loan", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.view_loan_label.place(x=650, y=570)

        # add image as button for logout
        self.logout_image = Image.open("Loan_app/logout.png")
        self.logout_image = self.logout_image.resize((70, 70), Image.LANCZOS)
        self.logout_image = ImageTk.PhotoImage(self.logout_image)
        self.logout_button = Button(self.admin_frame, image=self.logout_image, bg="white", bd=0, cursor="hand2")
        self.logout_button.place(x=1050, y=650)
        
    def loan_application(self):
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

        self.loan_term_label = Label(self.loan_frame, text="Loan Term", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.loan_term_label.place(x=400, y=470)
        self.loan_term_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.loan_term_entry.place(x=600, y=470)

        self.loan_interest_rate_label = Label(self.loan_frame, text="Interest Rate", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.loan_interest_rate_label.place(x=400, y=515)
        self.loan_interest_rate_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.loan_interest_rate_entry.place(x=600, y=515)

        self.loan_repayment_schedule_label = Label(self.loan_frame, text="Repayment Schedule", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.loan_repayment_schedule_label.place(x=400, y=560)
        self.loan_repayment_schedule_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.loan_repayment_schedule_entry.place(x=600, y=560)
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
        self.submit_loan_button = Button(self.loan_frame, image=self.submit_loan_image, bg="white", bd=0, cursor="hand2")
        self.submit_loan_button.place(x=950, y=670)
        
        
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
        self.submit_loan_details_button = Button(self.add_loan_frame, image=self.submit_loan_details_image, bg="white", bd=0, cursor="hand2")
        self.submit_loan_details_button.place(x=690, y=440)
        
        # add image as button for back to admin page
        self.back_to_admin_image = Image.open("Loan_app/back.png")
        self.back_to_admin_image = self.back_to_admin_image.resize((70, 70), Image.LANCZOS)
        self.back_to_admin_image = ImageTk.PhotoImage(self.back_to_admin_image)
        self.back_to_admin_button = Button(self.add_loan_frame, image=self.back_to_admin_image, bg="white", bd=0, cursor="hand2", command=self.adminpage)
        self.back_to_admin_button.place(x=1050, y=650)
        
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
        

        
        
        
        
        
        

        
if __name__ == "__main__":
    root = Tk()
    app = loan_managnment_system(root)
    root.mainloop()
