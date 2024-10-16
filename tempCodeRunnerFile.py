        # add loan name label and entry box
        self.loan_name_label = Label(self.add_loan_frame, text="Loan Name", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.loan_name_label.place(x=450, y=120)
        self.loan_name_entry = Entry(self.add_loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.loan_name_entry.place(x=600, y=120)

        # add loan type label and drop down box
        self.loan_type_label = Label(self.add_loan_frame, text="Loan Type", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.loan_type_label.place(x=450, y=170)
        self.loan_type_entry = ttk.Combobox(self.add_loan_frame, font=("calibri", 15), state="readonly")
        self.loan_type_entry["values"] = ["Personal Loan", "Home Loan", "Car Loan", "Business Loan"]
        self.loan_type_entry.place(x=600, y=170)

        # add loan amount label and entry box
        self.loan_amount_label = Label(self.add_loan_frame, text="Loan Amount", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.loan_amount_label.place(x=450, y=220)
        self.loan_amount_entry = Entry(self.add_loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.loan_amount_entry.place(x=600, y=220)

        # add loan interest rate label and entry box
        self.loan_interest_rate_label = Label(self.add_loan_frame, text="Interest Rate", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.loan_interest_rate_label.place(x=450, y=270)
        self.loan_interest_rate_entry = Entry(self.add_loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.loan_interest_rate_entry.place(x=600, y=270)

        # add loan term label and entry box
        self.loan_term_label = Label(self.add_loan_frame, text="Loan Term", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.loan_term_label.place(x=450, y=320)
        self.loan_term_entry = Entry(self.add_loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.loan_term_entry.place(x=600, y=320)

        # collateral required label and drop down box
        self.collateral_required_label = Label(self.add_loan_frame, text="Collateral Required", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.collateral_required_label.place(x=450, y=370)
        self.collateral_required_entry = ttk.Combobox(self.add_loan_frame, font=("calibri", 15), state="readonly")
        self.collateral_required_entry["values"] = ["Yes", "No"]
        self.collateral_required_entry.place(x=600, y=370)