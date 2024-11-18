import tkinter
#import python ,tkinter, mysql and other libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk
import customtkinter as tk
import re
import tkinter as tk
from tkinter import ttk
import webbrowser
import customtkinter as ctk
import math
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
from tkinter import filedialog
import datetime
from tkcalendar import DateEntry
from tkinter import Toplevel, StringVar, Radiobutton, Entry, messagebox


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
        self.mainscreen()
    
    
    #adding main screen
    def mainscreen(self):
        for i in self.root.winfo_children():
            i.destroy()
            
        self.main_frame = Frame(self.root, bg="white")
        self.main_frame.place(x=0, y=0, width=1200, height=750)
        #adding Maindogpage1 image
       # Set up the main screen background image
        self.bg_image = Image.open("Loan_app/images/mainscreen.png")  # Replace with the path to your image
        self.bg_image = self.bg_image.resize((1200, 750), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        self.bg_image_label = Label(self.main_frame, image=self.bg_image)
        self.bg_image_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Add the description text, centered and styled
        # Main screen description with enhanced appearance
      # Main screen welcome title
        self.welcome_label = Label(
            self.main_frame,
            text="Welcome to Finserve Financial!",
            font=("Calibri", 30, "bold"),  # Larger font for emphasis
            bg="#F1C9C2",  # Background color for readability on the light background
            fg="#F13737"
        )
        self.welcome_label.place(x=550, y=150)  # Position above the main description

        # Main screen description text
        self.description_label = Label(
            self.main_frame,
            text=(
                "Simplify your loan management with our secure, user-friendly platform. "
                "Apply for loans, track repayments, and confidently manage your financial journey.\n\n"
                "Trust Finserve Financial to support your goals with transparency and reliability."
            ),
            font=("Calibri", 16,),  # Standard font size for the main message
            bg="#F1C9C2",  # Subtle background to enhance readability
            fg="black",
            wraplength=400,
            justify="center"
        )
        self.description_label.place(x=600, y=210)  # Position below the welcome label
        
        import customtkinter as ctk

    # Initialize customtkinter
       # Assuming your background color is the same as the application background
        background_color = "#f4cdc3"  # This is the color of the background in your image

        # Set the main frame background color to match the application background
        self.main_frame.configure(bg=background_color)

        # Create Login Button with rounded corners and no border
        import customtkinter as customtkinter
        self.login_button = customtkinter.CTkButton(
            self.main_frame,
            text="Login",
            font=("Calibri", 15, "bold"),
            fg_color="#333333",  # Button color (dark color for contrast)
            text_color="white",
            width=150,
            height=50,
            corner_radius=20,
            border_width=0,  # Removes border to eliminate edge white spaces
            bg_color=background_color,  # Match the frame's background color
            command=self.loginscreen
        )
        self.login_button.place(x=620, y=500)

        # Create Register Button with the same style
        self.register_button = customtkinter.CTkButton(
            self.main_frame,
            text="Register",
            font=("Calibri", 15, "bold"),
            fg_color="#333333",
            text_color="white",
            width=150,
            height=50,
            corner_radius=20,
            border_width=0,
            bg_color=background_color,
            command=self.registerscreen
        )
        self.register_button.place(x=820, y=500)




    
    #function to destroy all the widgets on the screen
    def loginscreen(self):
        for i in self.root.winfo_children():
            i.destroy()
            
        self.login_frame = Frame(self.root, bg="white")
        self.login_frame.place(x=0, y=0, width=1200, height=750)
        
        self.show_pass_var = tk.IntVar()
        self.password_visible = False
        # adding Logindogpage1 image
        self.bg = Image.open("Loan_app/images/login.png")
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
        
        def toggle_password():
            if self.show_pass_var.get():
                self.password_entry.config(show="")
            else:
                self.password_entry.config(show="*")
        
        # adding show password check button
        self.show_pass = Checkbutton(self.login_frame, text="Show Password", variable=self.show_pass_var, onvalue=1, offvalue=0,bg="#4b5ee5", fg="black",activebackground="#4b5ee5", command=toggle_password)
        self.show_pass.place(x=850, y=330)
        
        # adding forgot password button
        self.forgot_pass = Button(self.login_frame, text="Forgot Password?", font=("calibri", 10), bg="#4b5ee5", fg="black", bd=0, cursor="hand2",command=self.forgot_password)
        self.forgot_pass.place(x=850, y=360)
        
        # adding login button with customtkinter button
        import customtkinter as customtkinter
        self.login_button = customtkinter.CTkButton(
            self.login_frame,
            text="Login",
            font=("calibri", 15, "bold"),
            fg_color="#333333",  # Button color (dark color for contrast)
            text_color="white",
            width=150,
            height=50,
            corner_radius=20,
            border_width=0,  # Removes border to eliminate edge white spaces
            bg_color="#4b5ee5",  # Match the frame's background color
            command=self.login_screen
        )
        self.login_button.place(x=880, y=390)
        
        # # adding register button
        # self.register_button = Button(self.login_frame, text="Register", font=("calibri", 15,"bold"), bg="#4b5ee5", fg="black", bd=1, cursor="hand2", activebackground="#4b5ee5", command=self.registerscreen)
        # self.register_button.place(x=938, y=440)
        # #creating singnup page
        
        #add back image button to the main page
        self.back = Image.open("Loan_app/images/back.png")
        self.back = self.back.resize((70, 70), Image.LANCZOS)
        self.back = ImageTk.PhotoImage(self.back)
        self.back_button = Button(self.login_frame, image=self.back,bg= "#495DE5",bd=0, cursor="hand2",command=self.mainscreen)
        self.back_button.place(x=1000, y=600)
    
    
    #forgot password screen
    def forgot_password(self):
        for i in self.root.winfo_children():
            i.destroy()

        self.forgot_password_frame = Frame(self.root, bg="white")
        self.forgot_password_frame.place(x=0, y=0, width=1200, height=750)

        # Add background image to the forgot password page
        self.bg = Image.open("Loan_app/images/forgot password screen.jpg")
        self.bg = self.bg.resize((1200, 750), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg)
        self.bg_image = Label(self.forgot_password_frame, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        # Add "Forgot Password" text to the left side
        self.forgot_password_label = Label(self.forgot_password_frame, text="Forgot your Password ?", font=("calibri", 30, "bold"), bg="white", fg="black")
        self.forgot_password_label.place(x=100, y=80)

        # Add email label and entry box
        self.email_label = Label(self.forgot_password_frame, text="Current Email", font=("calibri", 15, "bold"), bg="#01273C", fg="white")
        self.email_label.place(x=210, y=179)
        self.email_entry = Entry(self.forgot_password_frame, font=("calibri", 15), bg="#01273C", fg="white")
        self.email_entry.place(x=170, y=220)

        # Add verify button
        self.verify_button = Button(self.forgot_password_frame, text="Verify", font=("calibri", 15, "bold"), bg="#01273C", fg="white", bd=1, cursor="hand2", command=self.verify_email)
        self.verify_button.place(x=235, y=270)

        # Initialize the password fields (they will be shown only after email verification)
        self.new_password_label = Label(self.forgot_password_frame, text="New Password", font=("calibri", 15, "bold"), bg="#01273C", fg="white")
        self.new_password_entry = Entry(self.forgot_password_frame, font=("calibri", 15), bg="#01273C", fg="white", show="*")

        self.new_confirm_password_label = Label(self.forgot_password_frame, text="Confirm Password", font=("calibri", 15, "bold"), bg="#01273C", fg="white")
        self.new_confirm_password_entry = Entry(self.forgot_password_frame, font=("calibri", 15), bg="#01273C", fg="white", show="*")
        
        #back button to the login page
        self.back = Image.open("Loan_app/images/back.png")
        self.back = self.back.resize((70, 70), Image.LANCZOS)
        self.back = ImageTk.PhotoImage(self.back)
        self.back_button = Button(self.forgot_password_frame, image=self.back,bg= "white",bd=0, cursor="hand2",command=self.loginscreen)
        self.back_button.place(x=400, y=600)

        # Initialize the reset button
        self.reset_button = Button(self.forgot_password_frame, text="Reset Password", font=("calibri", 15, "bold"), bg="#01273C", fg="white", command=self.submit_new_password)
        
        #add image back to login page
        self.back = Image.open("back.png")
        self.back = self.back.resize((70, 70), Image.LANCZOS)
        self.back = ImageTk.PhotoImage(self.back)
        self.back_button = Button(self.forgot_password_frame, image=self.back,bg= "white",bd=0, cursor="hand2",command=self.loginscreen)
        self.back_button.place(x=1000, y=600)
        self.back_button.config(command=self.loginscreen)
        
        

    def verify_email(self):
        # Verify if the entered email exists in the database
        current_email = self.email_entry.get()

        cursor = loan_management_systemdb.cursor()
        select_data = "SELECT email FROM user WHERE email = %s"
        cursor.execute(select_data, (current_email,))
        result = cursor.fetchone()

        if result is None:
            messagebox.showerror("Error", "Invalid Email")
        else:
            # If email is valid, show password fields for reset
            self.new_password_label.place(x=200, y=330)
            self.new_password_entry.place(x=180, y=360)
            self.new_confirm_password_label.place(x=200, y=400)
            self.new_confirm_password_entry.place(x=180, y=430)
            self.reset_button.place(x=200, y=470)

    def submit_new_password(self):
        # Get the new password and confirm password
        new_password = self.new_password_entry.get()
        confirm_password = self.new_confirm_password_entry.get()
        current_email = self.email_entry.get()

        # Check if password and confirm password are the same
        if new_password != confirm_password:
            messagebox.showerror("Error", "Password and Confirm Password should be the same")
            
        # if password and confirm password entry is empty show error
        elif new_password == "" or confirm_password == "":
            messagebox.showerror("Error", "All fields are required")
        elif len(new_password) < 8 or not re.search("[a-z]", new_password) or not re.search("[A-Z]", new_password) or not re.search("[0-9]", new_password):
            messagebox.showerror("Error", "Password must contain at least 8 characters, including letters and numbers")
        else:
            # Update the password in the database
            cursor = loan_management_systemdb.cursor()
            update_password = "UPDATE user SET password = %s WHERE email = %s"
            cursor.execute(update_password, (new_password, current_email))
            loan_management_systemdb.commit()

            messagebox.showinfo("Success", "Password Reset Successful")
            self.loginscreen()  # Redirect to login screen
        
    
    
    
    
        
    def registerscreen(self):
        for i in self.root.winfo_children():
            i.destroy()
            
        self.show_pass_var = tk.IntVar()
        self.password_visible = False
        
        self.register_frame = Frame(self.root, bg="white")
        self.register_frame.place(x=0, y=0, width=1200, height=750)
        #adding Registerdogpage1 image
        self.bg = Image.open("Loan_app/images/register.png")
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
        self.email_entry = Entry(self.register_frame, font=("calibri", 15), bg="white", fg="grey",width=30)
        self.email_entry.place(x=550, y=250)
        self.email_entry.insert(0, "example@domain.com")
        self.email_entry.bind("<FocusIn>", self.email_in)
        self.email_entry.bind("<FocusOut>", self.email_out)
        
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
        self.password_entry = Entry(self.register_frame, font=("calibri", 15), bg="white", fg="grey", show="")
        self.password_entry.place(x=550, y=390)
        self.password_entry.insert(0, "5+ characters,@,1")
        self.password_entry.bind("<FocusIn>", self.password_in)
        self.password_entry.bind("<FocusOut>", self.password_out)
        
        self.confirm_password_label = Label(self.register_frame, text="Confirm Password", font=("calibri", 15,"bold"), bg="white", fg="black")
        self.confirm_password_label.place(x=850, y=360)
        self.confirm_password_entry = Entry(self.register_frame, font=("calibri", 15), bg="white", fg="grey", show="")
        self.confirm_password_entry.place(x=850, y=390)
        self.confirm_password_entry.insert(0, "Re-enter password")
        # Bind focus events for confirm password field
        self.confirm_password_entry.bind('<FocusIn>', self.confirm_in)
        self.confirm_password_entry.bind('<FocusOut>', self.confirm_out)
        def toggle_password():
            if  self.show_pass_var.get():
                self.password_entry.config(show="")
                self.confirm_password_entry.config(show="")
            else:
                self.password_entry.config(show="*")
                self.confirm_password_entry.config(show="*")
                
        self.show_pass = Checkbutton(self.register_frame, text="Show Password", variable=self.show_pass_var, onvalue=1, offvalue=0, bg="#fffcf5", fg="black", command=toggle_password)
        self.show_pass.place(x=870, y=420)
                    
       
                 
        self.register_button = ctk.CTkButton(
            self.register_frame,
            text="Register",
            font=("calibri", 15, "bold"),
            fg_color="#333333",
            text_color="white",
            width=150,
            height=50,
            corner_radius=20,
            border_width=0,
            bg_color="white",
            command=self.register_screen
        )
        self.register_button.place(x=600, y=480)

        self.login_button = ctk.CTkButton(
            self.register_frame,
            text="Back to Login",
            font=("calibri", 15, "bold"),
            fg_color="#333333",
            text_color="white",
            width=150,
            height=50,
            corner_radius=20,
            border_width=0,
            bg_color="white",
            command=self.loginscreen
        )
        self.login_button.place(x=800, y=480)
    def email_in(self, event):
        if self.email_entry.get() == "example@domain.com":
            self.email_entry.delete(0, END)
            self.email_entry.config(fg="black")
            
    def email_out(self, event):
        if self.email_entry.get() == "":
            self.email_entry.insert(0, "example@domain.com")
            self.email_entry.config(fg="grey")
            
    def password_in(self, event):
        # If the default text is shown, clear it and hide the characters with "*"
        if self.password_entry.get() == "5+ characters,@,1":
            self.password_entry.delete(0, "end")
            self.password_entry.config(fg="black", show="*")

    def password_out(self, event):
        # If the entry is empty, show the default text again and remove the mask
        if self.password_entry.get() == "":
            self.password_entry.insert(0, "5+ characters,@,1")
            self.password_entry.config(fg="grey", show="")
            
    def confirm_in(self, event):
    # If the default text is shown, clear it and hide the characters with "*"
        if self.confirm_password_entry.get() == "Re-enter password":
            self.confirm_password_entry.delete(0, "end")
            self.confirm_password_entry.config(fg="black", show="*")

    # Method for focus-out event on confirm password entry
    def confirm_out(self, event):
        # If the entry is empty, show the default text again and remove the mask
        if self.confirm_password_entry.get() == "":
            self.confirm_password_entry.insert(0, "Re-enter password")
            self.confirm_password_entry.config(fg="grey", show="")
     # adding show password check button right side of the confirm password entry box
   


            
            
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
            con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_sys")
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
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_sys")
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
        self.bg_admin = Image.open("Loan_app/images/adminpage.png")
        self.bg_admin = self.bg_admin.resize((1200, 750), Image.LANCZOS)
        self.bg_admin = ImageTk.PhotoImage(self.bg_admin)
        self.bg_admin_image = Label(self.admin_frame, image=self.bg_admin).place(x=0, y=0, relwidth=1, relheight=1)
        self.admin_frame.place(x=0, y=0, width=1200, height=750)

        self.admin_frame.place(x=0, y=0, width=1200, height=750)
        
        self.admin_label = Label(self.admin_frame, text="Welcome Admin", font=("calibri", 30,"bold"), bg="white", fg="black")
        self.admin_label.place(x=740, y=70)
        
        # Add image as button for add loan
        self.add_loan_image = Image.open("Loan_app/images/add_loan.png")
        self.add_loan_image = self.add_loan_image.resize((70, 70), Image.LANCZOS)
        self.add_loan_image = ImageTk.PhotoImage(self.add_loan_image)
        self.add_loan_button = Button(self.admin_frame, image=self.add_loan_image, bg="white", bd=0, cursor="hand2",command=self.add_loan)
        self.add_loan_button.place(x=670, y=200)
        
        # add text to the add loan button
        self.add_loan_label = Label(self.admin_frame, text="Add Loan", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.add_loan_label.place(x=660, y=270)

        # add image as button for delete loan
        self.delete_loan_image = Image.open("Loan_app/images/delete_loan.png")
        self.delete_loan_image = self.delete_loan_image.resize((70, 70), Image.LANCZOS)
        self.delete_loan_image = ImageTk.PhotoImage(self.delete_loan_image)
        self.delete_loan_button = Button(self.admin_frame, image=self.delete_loan_image, bg="white", bd=0, cursor="hand2",command=self.delete_loan)
        self.delete_loan_button.place(x=670, y=350)
        
        # add text to the delete loan button
        self.delete_loan_label = Label(self.admin_frame, text="Delete Loan", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.delete_loan_label.place(x=650, y=420)

        # add image as button for view loan
        self.view_loan_image = Image.open("Loan_app/images/view_loans.png")
        self.view_loan_image = self.view_loan_image.resize((70, 70), Image.LANCZOS)
        self.view_loan_image = ImageTk.PhotoImage(self.view_loan_image)
        self.view_loan_button = Button(self.admin_frame, image=self.view_loan_image, bg="white", bd=0, cursor="hand2",command=self.manage_loan_applications)
        self.view_loan_button.place(x=965, y=200)
        
        #add image as button for report to the right of the add loan button
        self.report_image = Image.open("Loan_app/images/report.png")
        self.report_image = self.report_image.resize((70, 70), Image.LANCZOS)
        self.report_image = ImageTk.PhotoImage(self.report_image)
        self.report_button = Button(self.admin_frame, image=self.report_image, bg="white", bd=0, cursor="hand2",command=self.report_page)
        self.report_button.place(x=963, y=347)
        
        #add text to the report button
        self.report_label = Label(self.admin_frame, text="Reports", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.report_label.place(x=965, y=418)
        

        
        # add text to the view loan button
        self.view_loan_label = Label(self.admin_frame, text="View Loan", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.view_loan_label.place(x=950, y=270)

        # add image as button for logout
        self.logout_image = Image.open("Loan_app/images/logout.png")
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
        
        # Add image to the manage loan applications page
        self.manage_loan_image = Image.open("Loan_app/images/Admin_manage_loan.jpg")
        self.manage_loan_image = self.manage_loan_image.resize((1200, 750), Image.LANCZOS)
        self.manage_loan_image = ImageTk.PhotoImage(self.manage_loan_image)
        self.manage_loan_image_label = Label(self.manage_loan_frame, image=self.manage_loan_image).place(x=0, y=0, relwidth=1, relheight=1)
        
        # Add a label for the frame
        self.manage_loan_label = Label(self.manage_loan_frame, text="Manage Loan Applications", font=("calibri", 30, "bold"), bg="white", fg="black")
        self.manage_loan_label.place(x=400, y=150)
        
        # Back to admin button with image
        self.back_to_admin_image = Image.open("Loan_app/images/back.png")
        self.back_to_admin_image = self.back_to_admin_image.resize((80, 80), Image.LANCZOS)
        self.back_to_admin_image = ImageTk.PhotoImage(self.back_to_admin_image)
        self.back_to_admin_button = Button(self.manage_loan_frame, image=self.back_to_admin_image, bg="white", bd=0, cursor="hand2", command=self.adminpage)
        self.back_to_admin_button.place(x=1050, y=650)
        
        # Fetch pending loan applications (exclude approved or rejected loans)
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_sys")
        cursor = con.cursor()
        cursor.execute("""
            SELECT application_id, loan_id, first_name, last_name, amount, interest_rate, collateral_value, loan_term, repayment_schedule 
            FROM loan_application 
            WHERE loan_decision IS NULL
        """)
        loans = cursor.fetchall()
        con.close()
        
        # Display loan applications as buttons
        y = 320
        for loan in loans:
            application_id = loan[0]  # application_id is at index 0
            loan_id = loan[1]  # loan_id is at index 1
            loan_amount = loan[4]  # amount is at index 4
            
            loan_details = f"Application ID: {application_id}, Amount: ${loan_amount}"
            
            loan_button = Button(
                self.manage_loan_frame, 
                text=loan_details, 
                font=("calibri", 15), 
                bg="#3D4151", 
                fg="white", 
                bd=1, 
                cursor="hand2", 
                command=lambda application_id=application_id: self.loan_decision_details(application_id)
            )
            loan_button.place(x=500, y=y)
            
            y += 50


    def loan_decision_details(self, application_id):
        # Clear the frame for loan decision details
        for widget in self.manage_loan_frame.winfo_children():
            widget.destroy()
        
        # Add image to the loan decision details page
        self.loan_decision_image = Image.open("Loan_app/images/user_agree_screen.jpg")
        self.loan_decision_image = self.loan_decision_image.resize((1200, 750), Image.LANCZOS)
        self.loan_decision_image = ImageTk.PhotoImage(self.loan_decision_image)
        self.loan_decision_image_label = Label(self.manage_loan_frame, image=self.loan_decision_image).place(x=0, y=0, relwidth=1, relheight=1)
        
        # Add label for the loan decision details page
        self.loan_decision_label = Label(self.manage_loan_frame, text="Loan Decision", font=("calibri", 30, "bold"), bg="#85C1F5", fg="black")
        self.loan_decision_label.place(x=500, y=50)
        
        # Fetch the specific loan details from the database
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_sys")
        cursor = con.cursor()
        cursor.execute(
            "SELECT application_id, loan_id, first_name, last_name, amount, interest_rate, collateral_value, loan_term, repayment_schedule FROM loan_application WHERE application_id = %s",
            (application_id,)
        )
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
        decision_details_label = Label(self.manage_loan_frame, text=decision_details, font=("calibri", 15), bg="#85C1F5", fg="black")
        decision_details_label.place(x=500, y=150)
        
        decision_color = "#86C2F6" 
        
        self.manage_loan_frame.configure(bg=decision_color)
        
        # Approve and Reject buttons using customtkinter
        approve_button = ctk.CTkButton(
            self.manage_loan_frame,
            text="Approve",
            font=("calibri", 15, "bold"),
            fg_color="green",
            text_color="white",
            width=150,
            height=50,
            corner_radius=20,
            bg_color=decision_color,
            border_width=0,
            command=lambda: self.process_loan(application_id, "approved")
        )
        approve_button.place(x=650, y=500)
        
        reject_button = ctk.CTkButton(
            self.manage_loan_frame,
            text="Reject",
            font=("calibri", 15, "bold"),
            fg_color="red",
            text_color="white",
            width=150,
            height=50,
            corner_radius=20,
            border_width=0,
            bg_color=decision_color,
            command=lambda: self.process_loan(application_id, "rejected")
        )
        reject_button.place(x=850, y=500)
        
        # Back image button to the manage loan applications page
        self.back_to_manage_loans_image = Image.open("Loan_app/images/back.png")
        self.back_to_manage_loans_image = self.back_to_manage_loans_image.resize((80, 80), Image.LANCZOS)
        self.back_to_manage_loans_image = ImageTk.PhotoImage(self.back_to_manage_loans_image)
        self.back_to_manage_loans_button = Button(
            self.manage_loan_frame,
            image=self.back_to_manage_loans_image,
            bg="#85C1F5",
            bd=0,
            cursor="hand2",
            command=self.manage_loan_applications
        )
        self.back_to_manage_loans_button.place(x=1050, y=650)

        

    def process_loan(self, application_id, decision):
        try:
            # Update loan decision in the database based on application_id
            con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_sys")
            cursor = con.cursor()
            cursor.execute("UPDATE loan_application SET loan_decision = %s WHERE application_id = %s", (decision, application_id))
            con.commit()
            con.close()
            
            # Show confirmation message
            if decision == "approved":
                messagebox.showinfo("Success", f"Loan Application ID {application_id} has been approved.")
            elif decision == "rejected":
                messagebox.showinfo("Success", f"Loan Application ID {application_id} has been rejected.")
            
            # Refresh the loan management page
            self.manage_loan_applications()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while processing the loan: {e}")


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
        self.manage_loan_applications()

        
            
        
   
    def loan_application(self,loan_id,collateral_required):
        self.loan_id = loan_id
        self.collateral_required = collateral_required

        
        for i in self.root.winfo_children():
            i.destroy()
        
        self.loan_frame = Frame(self.root, bg="white")
        self.loan_frame.place(x=0, y=0, width=1200, height=750)
        
        
        # Adding Loan Application Background Image
        self.bg_loan_app = Image.open("Loan_app/images/loan_appliaction.jpg")
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


        # self.dob_label = Label(self.loan_frame, text="Date of Birth", font=("calibri", 15, "bold"), bg="white", fg="black")
        # self.dob_label.place(x=400, y=335)
        # self.dob_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        # self.dob_entry.place(x=600, y=335)
        # Add calendar widget for date of birth
        self.dob_label = Label(self.loan_frame, text="Date of Birth", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.dob_label.place(x=400, y=335)
        
        self.dob_entry = DateEntry(self.loan_frame, font=("calibri", 15), bg="white", fg="black", date_pattern='y-mm-dd')
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
        if self.collateral_required.lower() == "yes":
            self.collateral_details_label = Label(self.loan_frame, text="Collateral Details", font=("calibri", 15), bg="white", fg="black")
            self.collateral_details_label.place(x=400, y=605)
            
            self.collateral_type_label = Label(self.loan_frame, text="Collateral Type", font=("calibri", 15, "bold"), bg="white", fg="black")
            self.collateral_type_label.place(x=400, y=650)
            self.collateral_type_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
            self.collateral_type_entry.place(x=600, y=650)

            # add collateral value label and entry box
            #if collateral is yes only then the collateral value will be asked
            
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
        self.back_to_login_image = Image.open("Loan_app/images/back.png")
        self.back_to_login_image = self.back_to_login_image.resize((80, 80), Image.LANCZOS)
        self.back_to_login_image = ImageTk.PhotoImage(self.back_to_login_image)
        self.back_to_login_button = Button(self.loan_frame, image=self.back_to_login_image, bg="white", bd=0, cursor="hand2", command=lambda: self.show_loan_details(self.loan_id)) # Pass loan_id here)
        self.back_to_login_button.place(x=1050, y=650)
        
        # add image as button for submit loan application
        self.submit_loan_image = Image.open("Loan_app/images/submit.png")
        self.submit_loan_image = self.submit_loan_image.resize((60, 60), Image.LANCZOS)
        self.submit_loan_image = ImageTk.PhotoImage(self.submit_loan_image)
        self.submit_loan_button = Button(self.loan_frame, image=self.submit_loan_image, bg="white", bd=0, cursor="hand2",command=self.submit_loan)
        self.submit_loan_button.place(x=950, y=670)
        
        
    def get_loan_details(self, loan_id):
        # Fetch loan details from the database using the loan_id
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_sys")
        cursor = con.cursor()
        cursor.execute("SELECT loan_name, loan_type, loan_amount, interest_rate, loan_term, min_age, max_age, min_income, credit_score,collateral_required, collateral_value FROM loan WHERE loan_id = %s", (loan_id,))
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
        collateral_required=loan[9]
        collateral_value = loan[10]
        
        # self.loan_details_label = Label(self.loan_details_frame, text=f"Loan Details for {loan_name}", font=("calibri", 20, "bold"), bg="#85C1F5", fg="black")
        # self.loan_details_label.place(x=600, y=50)
        
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
        "collateral_required": collateral_required,
        "collateral_value": collateral_value
        }
     


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
        self.loan_amount = self.loan_amount_entry.get()
        self.employer_name = self.employer_name_entry.get()
        self.years_employed = self.years_employed_entry.get()
        self.annual_income = self.annual_income_entry.get()
        self.credit_score = self.credit_score_entry.get()
        # Get collateral details only if collateral is required
        if self.collateral_required == "yes":
            self.collateral_type = self.collateral_type_entry.get()
            self.collateral_value = self.collateral_value_entry.get()
        else:
            self.collateral_type = None
            self.collateral_value = None

        #check if every field is filled or not if not then show error message
        if self.first_name == "" or self.last_name == "" or self.email == "" or self.phone_number == "" or self.street_address == "" or self.city == "" or self.state == "" or self.zip_code == "" or self.dob == "" or self.loan_amount == "" or self.employer_name == "" or self.years_employed == "" or self.annual_income == "" or self.credit_score == "":
            messagebox.showerror("Loan Application Error", "All fields are required.")
            return
        
        #convert the loan amount, annual income, credit score and collateral value to float and integer respectively
        try:
            self.loan_amount = float(self.loan_amount)
            self.annual_income = float(self.annual_income)
            self.credit_score = int(self.credit_score)
            if self.collateral_required == "yes":
                self.collateral_value = float(self.collateral_value)
        except ValueError:
            messagebox.showerror("Loan Application Error", "Loan amount, annual income, credit score, and collateral value must be numbers.")
            return

        # # Assuming the following details were already fetched during loan display
        loan_id = self.loan_id  # Ensure `loan_id` is stored when the user selects a loan
        loan_details = self.get_loan_details(loan_id)

        # # Extract loan requirements
        self.min_age = loan_details["min_age"]
        self.max_age = loan_details["max_age"]
        self.min_income = loan_details["min_income"]
        self.required_credit_score = loan_details["credit_score"]
        self.required_collateral_value = loan_details["collateral_value"]
        

        # Validation Logic
        import datetime
        today = datetime.date.today()
        dob_date = datetime.datetime.strptime(self.dob, "%Y-%m-%d").date()
        self.dob = dob_date
        age = (today - dob_date).days // 365

        # Validate age
        if not (self.min_age <= age <= self.max_age):
            messagebox.showerror("Loan Application Error", f"Applicant's age must be between {self.min_age} and {self.max_age} years.")
            #return

        # Validate annual income
        if self.annual_income < self.min_income:
            messagebox.showerror("Loan Application Error", f"Applicant's annual income must be at least {self.min_income}.")
            #return

        # Validate credit score
        if self.credit_score < self.required_credit_score:
            messagebox.showerror("Loan Application Error", f"Applicant's credit score must be at least {self.required_credit_score}.")
           #return

        # Validate collateral value
        if self.collateral_required == "yes":
            if self.collateral_value < self.required_collateral_value:
                messagebox.showerror("Loan Application Error", f"Collateral value must be at least ${self.required_collateral_value}.")
                #return

        # If all validations pass, proceed
        interest_rate, repayment_schedule = self.calculate_loan_quote(self.loan_amount, self.credit_score, self.annual_income)

        self.interest_rate = interest_rate
        self.repayment_schedule = repayment_schedule

        # Show the loan quote with repayment plan
        self.show_quote_screen(self.loan_amount, interest_rate, repayment_schedule, self.loan_term)


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
        
        #add image to the quote screen
        self.quote_image = Image.open("Loan_app/images/user_agree_screen.jpg")
        self.quote_image = self.quote_image.resize((1200, 750), Image.LANCZOS)
        self.quote_image = ImageTk.PhotoImage(self.quote_image)
        self.quote_image_label = Label(self.quote_frame, image=self.quote_image).place(x=0, y=0, relwidth=1, relheight=1)
        

        # Display the loan quote details
        quote_text = f"""
        Your Loan Quote:
        -----------------
        Loan Amount: ${loan_amount}
        Loan Term: {loan_term} months
        Interest Rate: {interest_rate}%
        Repayment Schedule: {repayment_schedule}
        """

        self.quote_label = Label(self.quote_frame, text=quote_text, font=("calibri", 20), bg="#85C1F5", fg="black")
        self.quote_label.place(x=400, y=200)

        
        quote_color = "#86C2F6"
        self.quote_frame.configure(bg=quote_color)
        # Add Agree button using customtkinter
        self.agree_button = ctk.CTkButton(
            self.quote_frame,
            text="Agree",
            font=("calibri", 15, "bold"),
            fg_color="green",
            text_color="white",
            width=150,
            height=50,
            corner_radius=20,
            border_width=0,
            bg_color=quote_color,
            command=self.agree_to_loan
        )
        self.agree_button.place(x=500, y=500)

        # Add Cancel button using customtkinter
        self.cancel_button = ctk.CTkButton(
            self.quote_frame,
            text="Cancel",
            font=("calibri", 15, "bold"),
            fg_color="red",
            text_color="white",
            width=150,
            height=50,
            corner_radius=20,
            border_width=0,
            bg_color=quote_color,
            command=self.userpage
        )
        self.cancel_button.place(x=800, y=500)

    def agree_to_loan(self):
        # Once the user agrees, we submit the loan application to the database
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_sys")
            cursor = con.cursor()

            # Insert loan application into the loan_application table
            cursor.execute("""
                INSERT INTO loan_application (
                    first_name, last_name, email, phoneno, dob, street_address, city, state, zip_code,
                    amount, loan_term, interest_rate, repayment_schedule, collateral_type, collateral_value,
                    employer_name, years_employed, annual_income, credit_score, loan_id, user_id
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                self.first_name, self.last_name, self.email, self.phoneno,
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
        self.bg_add_loan = Image.open("Loan_app/images/add_loan_details.png")
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
        #only show if collateral is required
        self.collateral_value_label = Label(self.add_loan_frame, text="Collateral Value", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.collateral_value_label.place(x=870, y=320)
        self.collateral_value_entry = Entry(self.add_loan_frame, font=("calibri", 15), bg="white", fg="black", width=8)
        self.collateral_value_entry.place(x=1040, y=320)
        
        #add a note under the collateral value
        self.note_label = Label(self.add_loan_frame, text="Note: Enter 0 if collateral is not required", font=("calibri", 12), bg="white", fg="black")
        self.note_label.place(x=870, y=350)
        
        
        # add image as button for submit loan details
        self.submit_loan_details_image = Image.open("Loan_app/images/submit.png")
        self.submit_loan_details_image = self.submit_loan_details_image.resize((70, 70), Image.LANCZOS)
        self.submit_loan_details_image = ImageTk.PhotoImage(self.submit_loan_details_image)
        self.submit_loan_details_button = Button(self.add_loan_frame, image=self.submit_loan_details_image, bg="white", bd=0, cursor="hand2", command=self.publish_loan)
        self.submit_loan_details_button.place(x=690, y=440)
        
        # add image as button for back to admin page
        self.back_to_admin_image = Image.open("Loan_app/images/back.png")
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
        
        # Add background image to the report page
        self.bg = Image.open("Loan_app/images/reports_page.jpg")
        self.bg = self.bg.resize((1200, 750), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg)
        self.bg_image = Label(self.report_frame, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
            
        # Add report title and timestamp
        self.report_label = Label(self.report_frame, text="Loan Applications Report", font=("calibri", 30, "bold"), bg="#F6F6F6", fg="black")
        self.report_label.place(x=400, y=80)
        
        current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        timestamp_label = Label(self.report_frame, text=f"Generated on: {current_timestamp}", font=("calibri", 15), bg="#F6F6F6", fg="black")
        timestamp_label.place(x=450, y=150)
        
        # Configure Treeview Style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#EAEAEA", foreground="black", fieldbackground="#EAEAEA")
        style.map("Treeview", background=[('selected', 'green')])
        
        # Create a treeview with custom style
        self.report_tree = ttk.Treeview(
            self.report_frame,
            columns=("Application ID", "Loan ID", "User ID", "First name", "Last name", "Amount", "Interest Rate", "Repayment Schedule"),
            show="headings",
            height=15
        )
        self.report_tree.heading("Application ID", text="Application ID")
        self.report_tree.heading("Loan ID", text="Loan ID")
        self.report_tree.heading("User ID", text="User ID")
        self.report_tree.heading("First name", text="First name")
        self.report_tree.heading("Last name", text="Last name")
        self.report_tree.heading("Amount", text="Amount")
        self.report_tree.heading("Interest Rate", text="Interest Rate")
        self.report_tree.heading("Repayment Schedule", text="Repayment Schedule")

        self.report_tree.column("Application ID", width=100)
        self.report_tree.column("Loan ID", width=100)
        self.report_tree.column("User ID", width=100)
        self.report_tree.column("First name", width=150)
        self.report_tree.column("Last name", width=150)
        self.report_tree.column("Amount", width=100)
        self.report_tree.column("Interest Rate", width=150)
        self.report_tree.column("Repayment Schedule", width=200)

        self.report_tree.place(x=100, y=240)
        
        # Fetch and display loan application data
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_sys")
        cursor = con.cursor()
        cursor.execute("SELECT application_id, loan_id, user_id, first_name, last_name, amount, interest_rate, repayment_schedule FROM loan_application")
        loan_applications = cursor.fetchall()
        con.close()

        for loan_application in loan_applications:
            self.report_tree.insert("", "end", values=loan_application, tags=('row_background',))
        
        # Add download report button with an image
        self.download_image = Image.open("Loan_app/images/downloads.png")
        self.download_image = self.download_image.resize((40, 40), Image.LANCZOS)
        self.download_image = ImageTk.PhotoImage(self.download_image)
        self.download_button = Button(self.report_frame, image=self.download_image, bg="#F6F6F6", bd=0, cursor="hand2", command=self.download_report)
        self.download_button.place(x=550, y=600)
        
        #add lable below the download button
        self.download_label = Label(self.report_frame, text="Click to Download Report", font=("calibri", 13), bg="#F6F6F6", fg="black")
        self.download_label.place(x=480, y=650)
        
        # Add back to admin page button with an image
        self.back_image = Image.open("Loan_app/images/back.png")
        self.back_image = self.back_image.resize((60, 60), Image.LANCZOS)
        self.back_image = ImageTk.PhotoImage(self.back_image)
        self.back_button = Button(self.report_frame, image=self.back_image, bg="#F6F6F6", bd=0, cursor="hand2", command=self.adminpage)
        self.back_button.place(x=90, y=650)

        
        
    
    def download_report(self):
    # Connect to the database and fetch loan applications
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_sys")
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

  
    # def repayment_page(self):
    #     for i in self.root.winfo_children():
    #         i.destroy()
        
    #     self.repayment_frame = Frame(self.root, bg="white")
    #     self.repayment_frame.place(x=0, y=0, width=1200, height=750)
        
    #     # Adding Repayment Background Image
    #     self.bg_repayment = Image.open("Loan_app/images/repayment_screen.jpg")
    #     self.bg_repayment = self.bg_repayment.resize((1200, 750), Image.LANCZOS)
    #     self.bg_repayment = ImageTk.PhotoImage(self.bg_repayment)
    #     self.bg_repayment_image = Label(self.repayment_frame, image=self.bg_repayment).place(x=0, y=0, relwidth=1, relheight=1)

    #     self.repayment_label = Label(self.repayment_frame, text="Loan Repayment", font=("calibri", 30, "bold"), bg="#BBA0E3", fg="black")
    #     self.repayment_label.place(x=40, y=50)

    #     #show user loan details in a drop down box
    #     con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_sys")
    #     cursor = con.cursor()
    #     cursor.execute("SELECT la.application_id, l.loan_name FROM loan_application la JOIN loan l ON la.loan_id = l.loan_id")
    #     loan_applications = cursor.fetchall()
    #     con.close()

    #     self.loan_id_label = Label(self.repayment_frame, text="Select Application ID", font=("calibri", 15, "bold"), bg="#BBA0E3", fg="black")
    #     self.loan_id_label.place(x=500, y=120)
    #     self.loan_id_entry = ttk.Combobox(self.repayment_frame, font=("calibri", 15), state="readonly", width=17)
    #     # Display the loan IDs and names in the drop-down box
    #     self.loan_id_entry["values"] = [f"{loan[1]} (Application ID: {loan[0]})" for loan in loan_applications]
    #     self.loan_id_entry.place(x=650, y=120)

    #     # add image as button for show repayment schedule
    #     self.show_repayment_schedule_image = Image.open("Loan_app/images/user_repay.png")
    #     self.show_repayment_schedule_image = self.show_repayment_schedule_image.resize((70, 70), Image.LANCZOS)
    #     self.show_repayment_schedule_image = ImageTk.PhotoImage(self.show_repayment_schedule_image)
    #     self.show_repayment_schedule_button = Button(self.repayment_frame, image=self.show_repayment_schedule_image, bg="#BBA0E3", bd=0, cursor="hand2", command=self.show_repayment_schedule)
    #     self.show_repayment_schedule_button.place(x=660, y=200)
        
    #     #add image as button for back to user page
    #     self.back_to_user_image = Image.open("Loan_app/images/back.png")
    #     self.back_to_user_image = self.back_to_user_image.resize((70, 70), Image.LANCZOS)
    #     self.back_to_user_image = ImageTk.PhotoImage(self.back_to_user_image)
    #     self.back_to_user_button = Button(self.repayment_frame, image=self.back_to_user_image, bg="#BBA0E3", bd=0, cursor="hand2", command=self.view_loan_applications)
    #     self.back_to_user_button.place(x=1050, y=650)
    
    
    def repayment_page(self):
        for i in self.root.winfo_children():
            i.destroy()
        
        self.repayment_frame = Frame(self.root, bg="white")
        self.repayment_frame.place(x=0, y=0, width=1200, height=750)
        
        # Adding Repayment Background Image
        self.bg_repayment = Image.open("Loan_app/images/repayment_screen.jpg")
        self.bg_repayment = self.bg_repayment.resize((1200, 750), Image.LANCZOS)
        self.bg_repayment = ImageTk.PhotoImage(self.bg_repayment)
        self.bg_repayment_image = Label(self.repayment_frame, image=self.bg_repayment).place(x=0, y=0, relwidth=1, relheight=1)

        self.repayment_label = Label(self.repayment_frame, text="Loan Repayment", font=("calibri", 30, "bold"), bg="#BBA0E3", fg="black")
        self.repayment_label.place(x=40, y=50)

        # Show user-approved loan details in a drop-down box
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_sys")
        cursor = con.cursor()
        # Fetch only approved loans for the logged-in user
        cursor.execute("""
            SELECT la.application_id, l.loan_name 
            FROM loan_application la 
            JOIN loan l ON la.loan_id = l.loan_id 
            WHERE la.user_id = %s AND la.loan_decision = 'Approved'
        """, (self.user_id,))
        loan_applications = cursor.fetchall()
        con.close()

        # Add a drop-down for selecting a loan application
        self.loan_id_label = Label(self.repayment_frame, text="Select Application ID", font=("calibri", 15, "bold"), bg="#BBA0E3", fg="black")
        self.loan_id_label.place(x=500, y=120)
        self.loan_id_entry = ttk.Combobox(self.repayment_frame, font=("calibri", 15), state="readonly", width=17)
        # Display only approved loans in the drop-down box
        self.loan_id_entry["values"] = [f"{loan[1]} (Application ID: {loan[0]})" for loan in loan_applications]
        self.loan_id_entry.place(x=650, y=120)

        # Add image as button for showing repayment schedule
        self.show_repayment_schedule_image = Image.open("Loan_app/images/user_repay.png")
        self.show_repayment_schedule_image = self.show_repayment_schedule_image.resize((70, 70), Image.LANCZOS)
        self.show_repayment_schedule_image = ImageTk.PhotoImage(self.show_repayment_schedule_image)
        self.show_repayment_schedule_button = Button(self.repayment_frame, image=self.show_repayment_schedule_image, bg="#BBA0E3", bd=0, cursor="hand2", command=self.show_repayment_schedule)
        self.show_repayment_schedule_button.place(x=660, y=200)
        
        # Add image as button for back to user page
        self.back_to_user_image = Image.open("Loan_app/images/back.png")
        self.back_to_user_image = self.back_to_user_image.resize((70, 70), Image.LANCZOS)
        self.back_to_user_image = ImageTk.PhotoImage(self.back_to_user_image)
        self.back_to_user_button = Button(self.repayment_frame, image=self.back_to_user_image, bg="#BBA0E3", bd=0, cursor="hand2", command=self.view_loan_applications)
        self.back_to_user_button.place(x=1050, y=650)

        
    def show_repayment_schedule(self):
        # Validate if a loan is selected
        selected_loan = self.loan_id_entry.get()
        if not selected_loan:
            messagebox.showerror("Error", "Please select a loan before proceeding.")
            return

        # Extract loan ID from the selected loan
        try:
            loan_id = int(selected_loan.split("(Application ID: ")[1].strip(")"))
        except (IndexError, ValueError):
            messagebox.showerror("Error", "Invalid loan selection. Please try again.")
            return

        # Fetch the repayment schedule and other details from the database
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_sys")
        cursor = con.cursor()
        cursor.execute("""
            SELECT repayment_schedule, amount, amount * 0.1 AS minimum_due 
            FROM loan_application 
            WHERE application_id = %s
        """, (loan_id,))
        loan_details = cursor.fetchone()
        con.close()

        if not loan_details:
            messagebox.showerror("Repayment Schedule", "Repayment details not found for the selected loan.")
            return

        repayment_schedule, remaining_balance, minimum_due = loan_details

        # Display repayment schedule
        if hasattr(self, 'repayment_schedule_label') and self.repayment_schedule_label.winfo_exists():
            self.repayment_schedule_label.config(text=f"Repayment Schedule: {repayment_schedule}")
        else:
            self.repayment_schedule_label = Label(
                self.repayment_frame,
                text=f"Repayment Schedule: {repayment_schedule}",
                font=("calibri", 15),
                bg="#BBA0E3",
                fg="black"
            )
            self.repayment_schedule_label.place(x=500, y=250)

        # Display remaining balance
        if hasattr(self, 'remaining_balance_label') and self.remaining_balance_label.winfo_exists():
            self.remaining_balance_label.config(text=f"Remaining Balance: ${remaining_balance:.2f}")
        else:
            self.remaining_balance_label = Label(
                self.repayment_frame,
                text=f"Remaining Balance: ${remaining_balance:.2f}",
                font=("calibri", 15),
                bg="#BBA0E3",
                fg="black"
            )
            self.remaining_balance_label.place(x=500, y=300)

        # Display minimum due
        if hasattr(self, 'minimum_due_label') and self.minimum_due_label.winfo_exists():
            self.minimum_due_label.config(text=f"Minimum Due: ${minimum_due:.2f}")
        else:
            self.minimum_due_label = Label(
                self.repayment_frame,
                text=f"Minimum Due: ${minimum_due:.2f}",
                font=("calibri", 15),
                bg="#BBA0E3",
                fg="black"
            )
            self.minimum_due_label.place(x=500, y=350)

        # Add input for custom amount
        if not hasattr(self, 'custom_amount_entry') or not self.custom_amount_entry.winfo_exists():
            self.custom_amount_label = Label(
                self.repayment_frame,
                text="Enter Custom Amount:",
                font=("calibri", 15),
                bg="#BBA0E3",
                fg="black"
            )
            self.custom_amount_label.place(x=500, y=400)

            self.custom_amount_entry = Entry(self.repayment_frame, font=("calibri", 15), width=10)
            self.custom_amount_entry.place(x=700, y=400)
        else:
            self.custom_amount_entry.delete(0, 'end')  # Clear previous input

        # Add or update Pay button
        if not hasattr(self, 'process_payment_button') or not self.process_payment_button.winfo_exists():
            self.process_payment_button = Button(
                self.repayment_frame,
                text="Submit Payment",
                font=("calibri", 15),
                bg="green",
                fg="white",
                command=lambda: self.process_payment(loan_id, remaining_balance, minimum_due)
            )
            self.process_payment_button.place(x=800, y=450)
        else:
            # Update command for existing button
            self.process_payment_button.config(command=lambda: self.process_payment(loan_id, remaining_balance, minimum_due))



    # def process_payment(self, loan_id, remaining_balance, minimum_due):
    #     # Validate the custom amount input
    #     try:
    #         custom_amount = float(self.custom_amount_entry.get())
    #     except ValueError:
    #         messagebox.showerror("Invalid Input", "Please enter a valid numeric amount.")
    #         return

    #     # Check for minimum due
    #     if custom_amount < minimum_due:
    #         messagebox.showerror("Payment Error", f"Custom amount must be at least ${minimum_due:.2f}.")
    #         return

    #     # Check for exceeding the remaining balance
    #     if custom_amount > remaining_balance:
    #         messagebox.showerror("Payment Error", "Custom amount exceeds the remaining balance.")
    #         return

    #     # Update the remaining balance in the database
    #     new_balance = remaining_balance - custom_amount
    #     con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_sys")
    #     cursor = con.cursor()
    #     cursor.execute("UPDATE loan_application SET amount = %s WHERE application_id = %s", (new_balance, loan_id))
    #     con.commit()
    #     con.close()

    #     # Update UI after payment
    #     messagebox.showinfo("Payment Successful", f"Payment of ${custom_amount:.2f} for Loan ID: {loan_id} has been processed successfully.")
    #     self.remaining_balance_label.config(text=f"Remaining Balance: ${new_balance:.2f}")
    #     self.custom_amount_entry.delete(0, 'end')






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
            con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_sys")
            cursor = con.cursor()
            cursor.execute("INSERT INTO loan (loan_name, loan_type, loan_amount, interest_rate, loan_term, collateral_required, min_age, max_age, min_income, credit_score, collateral_value) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (loan_name, loan_type, loan_amount, loan_interest_rate, loan_term, collateral_required, min_age, max_age, min_income, credit_score, collateral_value))
            con.commit()
            messagebox.showinfo(title="Loan Added", message="Loan details added successfully")
            con.close()
    
    
    
    def pay_loan(self):

        # Get the selected loan ID from the drop-down box
        selected_loan = self.loan_id_entry.get()
        
        if not selected_loan:
            messagebox.showerror("Error", "Please select a loan before proceeding.")
            return

    # Safely extract the loan ID
        try:
            loan_id = int(selected_loan.split(" - ")[1])
        except (IndexError, ValueError):
            messagebox.showerror("Error", "Invalid loan selection. Please try again.")
            return

        # Fetch the loan application details, including amount and repayment details
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_sys")
        cursor = con.cursor()
        cursor.execute("SELECT amount, repayment_schedule FROM loan_application WHERE loan_id = %s", (loan_id,))
        loan_application = cursor.fetchone()
        con.close()

        if not loan_application:
            messagebox.showerror("Error", "Loan details not found.")
            return
        
        

        remaining_balance = loan_application[0]  # Get the remaining balance from the loan application
        repayment_schedule = loan_application[1]  # Get the repayment schedule

        # Ask the user to pay the minimum due or enter a custom amount
        self.payment_frame = Frame(self.repayment_frame, bg="#BBA0E3")
        self.payment_frame.place(x=500, y=450)

        self.min_due_label = Label(self.payment_frame, text=f"Minimum Due: ${round(remaining_balance * 0.05, 2)}", font=("calibri", 15), bg="#BBA0E3", fg="black")
        self.min_due_label.grid(row=0, column=0, padx=5, pady=5)

        self.custom_amount_label = Label(self.payment_frame, text="Custom Amount: ", font=("calibri", 15), bg="#BBA0E3", fg="black")
        self.custom_amount_label.grid(row=1, column=0, padx=5, pady=5)

        self.custom_amount_entry = Entry(self.payment_frame, font=("calibri", 15), bg="white", fg="black")
        self.custom_amount_entry.grid(row=1, column=1, padx=5, pady=5)

        # Add button to process payment
        self.process_payment_button = Button(self.payment_frame, text="Submit Payment", font=("calibri", 15), bg="green", fg="white", command=lambda: self.process_payment(loan_id, remaining_balance))
        self.process_payment_button.grid(row=2, column=0, columnspan=2, pady=10)

    def process_payment(self, loan_id, remaining_balance, minimum_due):
        # Get the custom amount entered by the user
        try:
            custom_amount = self.custom_amount_entry.get().strip()
            custom_amount = float(custom_amount) if custom_amount else 0.0
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric amount.")
            return

        # Determine the payment amount
        if custom_amount == 0.0:  # If no custom amount is entered, use the minimum due
            payment_amount = minimum_due
        elif custom_amount < minimum_due:  # If custom amount is less than minimum due
            messagebox.showerror("Error", f"Custom payment amount cannot be less than the minimum due of ${minimum_due:.2f}.")
            return
        elif custom_amount > remaining_balance:  # If custom amount exceeds remaining balance
            messagebox.showerror("Error", "Payment exceeds the remaining loan balance.")
            return
        else:  # Valid custom amount entered
            payment_amount = custom_amount

        # Calculate the updated remaining balance after payment
        new_balance = remaining_balance - payment_amount

        # Update the loan amount in the database
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_sys")
        cursor = con.cursor()
        cursor.execute("UPDATE loan_application SET amount = %s WHERE application_id = %s", (new_balance, loan_id))
        con.commit()
        con.close()

        # Show success message
        messagebox.showinfo("Payment Successful", f"Payment of ${payment_amount:.2f} completed. New remaining balance: ${round(new_balance, 2)}.")

        # Refresh the repayment schedule and balance
        self.show_repayment_schedule()
        self.repayment_page()





        
        
        # creating delete loan page
    def delete_loan(self):
        for i in self.root.winfo_children():
            i.destroy()
        
        self.delete_loan_frame = Frame(self.root, bg="white")
        self.delete_loan_frame.place(x=0, y=0, width=1200, height=750)
        
        # Adding Delete Loan Background Image
        self.bg_delete_loan = Image.open("Loan_app/images/delete_loan_deatils.jpg")
        self.bg_delete_loan = self.bg_delete_loan.resize((1200, 750), Image.LANCZOS)
        self.bg_delete_loan = ImageTk.PhotoImage(self.bg_delete_loan)
        self.bg_delete_loan_image = Label(self.delete_loan_frame, image=self.bg_delete_loan).place(x=0, y=0, relwidth=1, relheight=1)
        
        self.delete_loan_label = Label(self.delete_loan_frame, text="Delete Loan Details", font=("calibri", 30, "bold"), bg="white", fg="black")
        self.delete_loan_label.place(x=40, y=50)

       #show all loans in a drop down box
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_sys")
        cursor = con.cursor()
        cursor.execute("SELECT loan_id, loan_name FROM loan")
        loans = cursor.fetchall()
        con.close()

        self.loan_id_label = Label(self.delete_loan_frame, text="Select Loan ID", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.loan_id_label.place(x=500, y=120)
        self.loan_id_entry = ttk.Combobox(self.delete_loan_frame, font=("calibri", 15), state="readonly", width=8)
        # Display the loan IDs and names in the drop-down box
        self.loan_id_entry["values"] = [f"{loan[0]} - {loan[1]}" for loan in loans]
        self.loan_id_entry.place(x=650, y=120)

        # add image as button for delete loan details
        self.delete_loan_details_image = Image.open("Loan_app/images/delete.png")
        self.delete_loan_details_image = self.delete_loan_details_image.resize((40, 40), Image.LANCZOS)
        self.delete_loan_details_image = ImageTk.PhotoImage(self.delete_loan_details_image)
        self.delete_loan_details_button = Button(self.delete_loan_frame, image=self.delete_loan_details_image, bg="white", bd=0, cursor="hand2", command=self.delete_loan_details)
        self.delete_loan_details_button.place(x=675, y=250)
        
        #add lable for delete image
        self.delete_label = Label(self.delete_loan_frame, text="Click to Delete Loan", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.delete_label.place(x=610, y=300)
        
        
        # add image as button for back to admin page
        self.back_to_admin_image = Image.open("Loan_app/images/back.png")
        self.back_to_admin_image = self.back_to_admin_image.resize((70, 70), Image.LANCZOS)
        self.back_to_admin_image = ImageTk.PhotoImage(self.back_to_admin_image)
        self.back_to_admin_button = Button(self.delete_loan_frame, image=self.back_to_admin_image, bg="white", bd=0, cursor="hand2", command=self.adminpage)
        self.back_to_admin_button.place(x=1050, y=650)

    def delete_loan_details(self):
        loan_id = self.loan_id_entry.get()
        if loan_id == "":
            messagebox.showerror(title="Empty Field", message="Please select a loan ID")
            return

        try:
            # Extract the loan ID
            loan_id = loan_id.split(" - ")[0]

            # Confirm deletion
            confirm = messagebox.askyesno("Delete Loan", "Are you sure you want to delete this loan? This will also delete associated applications.")
            if not confirm:
                return

            # Connect to the database
            con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_sys")
            cursor = con.cursor()

            # Delete associated applications first
            cursor.execute("DELETE FROM loan_application WHERE loan_id = %s", (loan_id,))
            con.commit()

            # Then delete the loan
            cursor.execute("DELETE FROM loan WHERE loan_id = %s", (loan_id,))
            con.commit()

            # Close the connection
            con.close()

            # Success message
            messagebox.showinfo(title="Loan Deleted", message="Loan details deleted successfully")

            # Refresh the delete loan page to update the dropdown
            self.delete_loan()

        except mysql.connector.IntegrityError as e:
            messagebox.showerror("Error", f"Cannot delete loan: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")




        
        #creating update loan page

        #creating user page
    def userpage(self):
        for i in self.root.winfo_children():
            i.destroy()
        
        self.user_frame = Frame(self.root, bg="white")
        self.user_frame.place(x=0, y=0, width=1200, height=750)
        
        # Adding User Page Background Image
        self.bg_user = Image.open("Loan_app/images/available_loans.jpg")
        self.bg_user = self.bg_user.resize((1200, 750), Image.LANCZOS)
        self.bg_user = ImageTk.PhotoImage(self.bg_user)
        self.bg_user_image = Label(self.user_frame, image=self.bg_user).place(x=0, y=0, relwidth=1, relheight=1)
        
        self.user_label = Label(self.user_frame, text="Choose Your suitable Loan", font=("calibri", 30, "bold"), bg="#BEDDFC", fg="black")
        self.user_label.place(x=650, y=80)
        
        # Fetch published loans from the database
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_sys")
        cursor = con.cursor()
        cursor.execute("SELECT loan_id, loan_name, loan_type FROM loan")
        loans = cursor.fetchall()
        con.close()
        print(loans)
        # Display the loans as clickable buttons
        y_offset = 185
        for loan in loans:
            loan_id = loan[0]
            loan_name = loan[1]
            loan_type = loan[2]
            
            loan_button = Button(self.user_frame, text=f"{loan_name} ({loan_type})", font=("calibri", 15,"bold"), bg="white", fg="black", cursor="hand2",bd=0, command=lambda loan_id=loan_id: self.show_loan_details(loan_id))
            loan_button.place(x=750, y=y_offset)
            y_offset += 30
            
        
        
        # Add image as button for back to login
        self.back_to_login_image = Image.open("Loan_app/images/back.png")
        self.back_to_login_image = self.back_to_login_image.resize((80, 80), Image.LANCZOS)
        self.back_to_login_image = ImageTk.PhotoImage(self.back_to_login_image)
        self.back_to_login_button = Button(self.user_frame, image=self.back_to_login_image, bg="#BEDDFC", bd=0, cursor="hand2", command=self.user_dashboard)
        self.back_to_login_button.place(x=1050, y=650)
        
        
        
        
    def show_loan_details(self, loan_id):
         # Implementation of the show_loan_details method as described earlier
        for i in self.root.winfo_children():
            i.destroy()
        
        self.loan_details_frame = Frame(self.root, bg="white")
        self.loan_details_frame.place(x=0, y=0, width=1200, height=750)
        
        #add image to the loan details page
        self.bg_loan_details = Image.open("Loan_app/images/loan_deatils.jpg")
        self.bg_loan_details = self.bg_loan_details.resize((1200, 750), Image.LANCZOS)
        self.bg_loan_details = ImageTk.PhotoImage(self.bg_loan_details)
        self.bg_loan_details_image = Label(self.loan_details_frame, image=self.bg_loan_details).place(x=0, y=0, relwidth=1, relheight=1)
            
        # Fetch loan details from the database using the loan_id
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_sys")
        cursor = con.cursor()
        cursor.execute("SELECT loan_name, loan_type, loan_amount, interest_rate, loan_term, min_age, max_age, min_income, credit_score,collateral_required, collateral_value FROM loan WHERE loan_id = %s", (loan_id,))
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
        collateral_required=loan[9]
        collateral_value = loan[10]
        
        self.loan_details_label = Label(self.loan_details_frame, text=f"Loan Details for {loan_name}", font=("calibri", 20, "bold"), bg="#85C1F5", fg="black")
        self.loan_details_label.place(x=600, y=50)
        
        details_text = f"""
        Loan Type: {loan_type}
        Loan Amount: {loan_amount}
        Interest Rate: {interest_rate}%
        Loan Term: {loan_term} months
        Minimum Age: {min_age}
        Maximum Age: {max_age}
        Minimum Income: {min_income}
        Required Credit Score: {credit_score}
        Collateral Required: {collateral_required}
        Collateral Value: {collateral_value}
        """

        self.loan_details = Label(self.loan_details_frame, text=details_text, font=("calibri", 15), bg="#85C1F5", fg="black", justify=LEFT)
        self.loan_details.place(x=620, y=120)
        
        #add a note to the user saying details may vary based on user profile and details
        self.note_label = Label(self.loan_details_frame, text="Note: Loan details may vary based on user profile and details", font=("calibri", 15,"bold"), bg="#85C1F5", fg="black")
        self.note_label.place(x=500, y=500)
        
        
      
       # Add apply loan image as a button (positioned after loan details)
        self.apply_loan_image = Image.open("Loan_app/images/apply.png")
        self.apply_loan_image = self.apply_loan_image.resize((70, 70), Image.LANCZOS)
        self.apply_loan_image = ImageTk.PhotoImage(self.apply_loan_image)
        self.apply_loan_button = Button(self.loan_details_frame, image=self.apply_loan_image, bg="#85C1F5", bd=0, cursor="hand2", command=lambda: self.loan_application(loan_id,collateral_required))
        self.apply_loan_button.place(x=705, y=415)  # Adjust the position as needed# Add apply loan image as a button (positioned after loan details)
        
        # Add back to user page button
        self.back_to_user_image = Image.open("Loan_app/images/back.png")
        self.back_to_user_image = self.back_to_user_image.resize((70, 70), Image.LANCZOS)
        self.back_to_user_image = ImageTk.PhotoImage(self.back_to_user_image)
        self.back_to_user_button = Button(self.loan_details_frame, image=self.back_to_user_image, bg="#85C1F5", bd=0, cursor="hand2", command=self.userpage)
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
        "collateral_required": collateral_required,
        "collateral_value": collateral_value
    }
        
    #creating a user dashboard
    def user_dashboard(self):
        for i in self.root.winfo_children():
            i.destroy()
        
        self.user_dashboard_frame = Frame(self.root, bg="white")
        self.user_dashboard_frame.place(x=0, y=0, width=1200, height=750)
        
        # Adding User Dashboard Background Image
        self.bg_user_dashboard = Image.open("Loan_app/images/dashboard.jpg")
        self.bg_user_dashboard = self.bg_user_dashboard.resize((1200, 750), Image.LANCZOS)
        self.bg_user_dashboard = ImageTk.PhotoImage(self.bg_user_dashboard)
        self.bg_user_dashboard_image = Label(self.user_dashboard_frame, image=self.bg_user_dashboard).place(x=0, y=0, relwidth=1, relheight=1)
        
        # self.user_dashboard_label = Label(self.user_dashboard_frame, text="User Dashboard", font=("calibri", 20, "bold"), bg="white", fg="black")
        # self.user_dashboard_label.place(x=500, y=50)
        
        cursor = loan_management_systemdb.cursor()
        select_data = "SELECT first_name FROM user WHERE email = %s"
        cursor.execute(select_data, (self.email,))
        result = cursor.fetchone()

        if result:
            first_name = result[0]
            welcome_message = f"Welcome {first_name}"
        else:
            welcome_message = "Welcome User"

        # Add user text with dynamic first name to the user page center
        self.user_label = Label(self.user_dashboard_frame, text=welcome_message, font=("calibri", 35, "bold"), bg="#7C96C7", fg="black")
        self.user_label.place(x=400, y=90)
        
        
        import customtkinter as ctk
        from tkcalendar import DateEntry


        # Initialize CustomTkinter appearance and theme if not already done
        ctk.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
        ctk.set_default_color_theme("dark-blue")  # Themes: "blue", "green", "dark-blue"

        # Add CustomTkinter button for 'Available Loans'
        self.user_dashboard_frame.config(bg="#72A5D0")
        self.view_loans_button = ctk.CTkButton(
            self.user_dashboard_frame,
            text="Available Loans",
            font=("calibri", 25, "bold"),
            fg_color="#72A5D0",       # Background color of the button
            text_color="black",
            hover_color="#A0C4E4",    # Color when hovered over
            width=200,                # Adjust width as needed
            height=70,                # Adjust height as needed
            border_width=1,
            corner_radius=10,         # Rounded corners
            command=self.userpage
        )
        self.view_loans_button.place(x=550, y=300)

        # Add CustomTkinter button for 'My Loan Applications'
        self.view_loan_applications_button = ctk.CTkButton(
            self.user_dashboard_frame,
            text="My Loan Applications",
            font=("calibri", 25, "bold"),
            fg_color="#72A5D0",
            text_color="black",
            hover_color="#A0C4E4",
            width=200,
            height=70,
            border_width=1,
            corner_radius=10, 
            command=self.view_loan_applications
        )
        self.view_loan_applications_button.place(x=533, y=400)

        
        
        
        
        

        
        
        # Add image as button for logout
        self.logout_image = Image.open("Loan_app/images/logout.png")
        self.logout_image = self.logout_image.resize((70, 70), Image.LANCZOS)
        self.logout_image = ImageTk.PhotoImage(self.logout_image)
        self.logout_button = Button(self.user_dashboard_frame, image=self.logout_image, bg="#7C96C7", bd=0, cursor="hand2", command=self.loginscreen)
        self.logout_button.place(x=1050, y=650)
        
    def view_loan_applications(self):
        for i in self.root.winfo_children():
            i.destroy()
            
        self.user_dashboard_frame = Frame(self.root, bg="white")
        self.user_dashboard_frame.place(x=0, y=0, width=1200, height=750)
        
        
        #add image to the loan details page
        self.bg_loan_details = Image.open("Loan_app/images/my_loan_applications.jpg")
        self.bg_loan_details = self.bg_loan_details.resize((1200, 750), Image.LANCZOS)
        self.bg_loan_details = ImageTk.PhotoImage(self.bg_loan_details)
        self.bg_loan_details_image = Label(self.user_dashboard_frame, image=self.bg_loan_details).place(x=0, y=0, relwidth=1, relheight=1)
        
        
        # add label for view loan applications
        self.view_loan_applications_label = Label(self.user_dashboard_frame, text="My Loans", font=("calibri", 30,"bold"), bg="white", fg="black")
        self.view_loan_applications_label.place(x=550, y=60)

        # add image as button for back to user dashboard
        self.back_to_user_dashboard_image = Image.open("Loan_app/images/back.png")
        self.back_to_user_dashboard_image = self.back_to_user_dashboard_image.resize((80, 80), Image.LANCZOS)
        self.back_to_user_dashboard_image = ImageTk.PhotoImage(self.back_to_user_dashboard_image)
        self.back_to_user_dashboard_button = Button(self.user_dashboard_frame, image=self.back_to_user_dashboard_image, bg="white", bd=0, cursor="hand2", command=self.user_dashboard)
        self.back_to_user_dashboard_button.place(x=1030, y=640)
        
        # fetch loan details from loan_application table for the user with status of the loan
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_sys")
        cursor = con.cursor()
        cursor.execute("SELECT la.application_id, l.loan_name, la.loan_decision FROM loan_application la JOIN loan l ON la.loan_id = l.loan_id WHERE la.user_id = %s", (self.user_id,))
        loan_applications = cursor.fetchall()
        con.close()
        print(loan_applications)
        # Display the loan applications as clickable buttons
        y_offset = 273
        for loan_application in loan_applications:
            loan_id = loan_application[0]  # application_id
            loan_name = loan_application[1]
            loan_decision = loan_application[2]

            if loan_decision is None:
                loan_decision = "Decision Pending"
                
            #if loan is decision is pending show decision pending
            loan_application_button = Button(self.user_dashboard_frame, text=f" ({loan_name}) - {loan_decision}", font=("calibri", 14,"bold"), bg="black", fg="white", cursor="hand2",bd=0, command=lambda application_id=loan_id, loan_name=loan_name: self.show_loan_application(application_id, loan_name))
            loan_application_button.place(x=523, y=y_offset)
            y_offset += 50
            
    def show_loan_application(self, application_id, loan_name):
        
        
        # Fetch loan application details from the database using the loan_id
        con = mysql.connector.connect(host="localhost", user="root", password="Croatia@24", database="loan_management_sys")
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
        
        if loan_decision is None:
            loan_decision = "Decision Pending"
        
        self.loan_application_frame = Frame(self.root, bg="white")
        self.loan_application_frame.place(x=0, y=0, width=1200, height=750)
        
        # Adding Loan Application Background Image
        self.bg_loan_application = Image.open("Loan_app/images/loan_deatils.jpg")
        self.bg_loan_application = self.bg_loan_application.resize((1200, 750), Image.LANCZOS)
        self.bg_loan_application = ImageTk.PhotoImage(self.bg_loan_application)
        self.bg_loan_application_image = Label(self.loan_application_frame, image=self.bg_loan_application).place(x=0, y=0, relwidth=1, relheight=1)
        
        self.loan_application_label = Label(self.loan_application_frame, text=f"Loan Application for {loan_name}", font=("calibri", 20, "bold"), bg="#85C1F5", fg="black")
        self.loan_application_label.place(x=700, y=50)
        
        
        
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
        Loan Decision: {loan_decision}
        """
        
        self.loan_application_details = Label(self.loan_application_frame, text=application_text, font=("calibri", 15), bg="#85C1F5", fg="black", justify=LEFT)
        self.loan_application_details.place(x=600, y=120)
        
        #add button for repaymeny page
        #only show repay button if loan decision is approved
        if loan_decision == "approved":
            self.repayment_image = Image.open("Loan_app/images/user_repay.png")
            self.repayment_image = self.repayment_image.resize((70, 70), Image.LANCZOS)
            self.repayment_image = ImageTk.PhotoImage(self.repayment_image)
            self.repayment_button = Button(self.loan_application_frame, image=self.repayment_image, bg="#85C1F5", bd=0, cursor="hand2", command=self.repayment_page)
            self.repayment_button.place(x=750, y=450)
        # # add lable for repayment page
        # self.repayment_label = Label(self.loan_application_frame, text="Repay my loan", font=("calibri", 15, "bold"), bg="white", fg="black")
        # self.repayment_label.place(x=600, y=500)
        
        
        
        
        # Add back to user dashboard button
        self.back_to_user_dashboard_image = Image.open("Loan_app/images/back.png")
        self.back_to_user_dashboard_image = self.back_to_user_dashboard_image.resize((70, 70), Image.LANCZOS)
        self.back_to_user_dashboard_image = ImageTk.PhotoImage(self.back_to_user_dashboard_image)
        self.back_to_user_dashboard_button = Button(self.loan_application_frame, image=self.back_to_user_dashboard_image, bg="#85C1F5", bd=0, cursor="hand2", command=self.view_loan_applications)
        self.back_to_user_dashboard_button.place(x=1050, y=650)
        
        
        

        
if __name__ == "__main__":
    root = Tk()
    app = loan_managnment_system(root)
    root.mainloop()
