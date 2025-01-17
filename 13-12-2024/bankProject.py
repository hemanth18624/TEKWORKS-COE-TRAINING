import streamlit as st


class Bank:
    account_balance = 10000
    withDrawCount = 1

    def pin_validation(self):
        pin = st.text_input("Enter your PIN number:", type="password")
        if pin == "1234":
            self.showOptions()
        else:
            st.error("Invalid PIN. Please try again.")

    def showOptions(self):
        st.title("Welcome to ABC Bank")

        option = st.radio(
            "Choose an option",
            ("Deposit", "Withdraw", "Balance Enquiry", "Exit")
        )

        if option == "Deposit":
            self.deposit()
        elif option == "Withdraw":
            self.withdraw()
        elif option == "Balance Enquiry":
            self.balance_enquiry()
        elif option == "Exit":
            st.write("Thank you for using ABC Bank. Have a nice day.")
            st.stop()

    def deposit(self):
        deposit_amount = st.number_input("Enter the deposit amount:", min_value=100, max_value=50000, step=100)

        if deposit_amount:
            if deposit_amount < 100:
                st.warning("Min Deposit is Rs. 100")
            elif deposit_amount % 100 != 0:
                st.warning("Deposit amount should be in multiples of 100")
            elif deposit_amount > 50000:
                st.warning("Max Deposit Amount is Rs. 50,000")
            else:
                self.account_balance += deposit_amount
                st.success(f"Amount Deposited Successfully. Current balance: Rs. {self.account_balance}")

    def withdraw(self):
        if self.withDrawCount > 3:
            st.warning("Max Limit for withdrawals reached!")
            return

        withdraw_amount = st.number_input("Enter the amount you wish to withdraw:", min_value=100, max_value=50000,
                                          step=100)

        if withdraw_amount:
            if withdraw_amount < 100:
                st.warning("Min Withdraw amount is Rs. 100")
            elif withdraw_amount % 100 != 0:
                st.warning("Withdraw amount should be in multiples of 100 only")
            elif self.account_balance < withdraw_amount:
                st.warning("Insufficient Account Balance")
            elif (self.account_balance - withdraw_amount) < 500:
                st.warning("Minimum 500 account balance needed")
            else:
                self.account_balance -= withdraw_amount
                self.withDrawCount += 1
                st.success(f"Money Debited Successfully. Current balance: Rs. {self.account_balance}")

    def balance_enquiry(self):
        st.write(f"Your current balance is: Rs. {self.account_balance}")


# Streamlit app layout

obj = Bank()
st.title("Bank Login")
st.write("Please enter your PIN to proceed.")
obj.pin_validation()


