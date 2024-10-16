 self.dob_label = Label(self.loan_frame, text="Date of Birth", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.dob_label.place(x=400, y=335)
        self.dob_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.dob_entry.place(x=600, y=335)

        self.loan_details_label = Label(self.loan_frame, text="Loan Details", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.loan_details_label.place(x=400, y=380)

        self.loan_amount_label = Label(self.loan_frame, text="Loan Amount", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.loan_amount_label.place(x=400, y=425)
        self.loan_amount_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.loan_amount_entry.place(x=600, y=425)

        self.loan_term_label = Label(self.loan_frame, text="Loan Term", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.loan_term_label.place(x=400, y=470)
        self.loan_term_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.loan_term_entry.place(x=600, y=470)

        self.loan_interest_rate_label = Label(self.loan_frame, text="Loan Interest Rate", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.loan_interest_rate_label.place(x=400, y=515)
        self.loan_interest_rate_entry = Entry(self.loan_frame, font=("calibri", 15), bg="white", fg="black")
        self.loan_interest_rate_entry.place(x=600, y=515)

        self.loan_repayment_schedule_label = Label(self.loan_frame, text="Loan Repayment Schedule", font=("calibri", 15, "bold"), bg="white", fg="black")
        self.loan_repayment_schedule_label.place(x=400, y=560)
        self.loan_repayment_schedule_text = Text(self.loan_frame, font=("calibri", 15), bg="white", fg="black", height=5)
        self.loan_repayment_schedule_text.place(x=600, y=560)

    # Start the application
    if __name__ == "__main__":
        root = Tk()
        app = loan_managnment_system(root)
        root.mainloop()
