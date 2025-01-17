"""
Rules for deposit :
--->Min deposit amount should be 100
--->Amount should be multiples of 100
--->Max Deposit amount 50k
Rules for Withdraw :
--->Min WithDraw Amount should be 100
--->Amount should be multiples of 100
--->Withdraw amount should be less than account balance
--->Need to maintain min 500 balance
--->Max Transaction amount should be 50k
--->Max Number of Transactions 3 only
"""


class Bank:
    account_balance = 10000
    withDrawCount = 1
    def pin_validation(self,count):
        pin = int(input("Enter your PIN number : "))
        count = count + 1
        if(pin == 1234):
            count = 0
            obj.showOptions()
        else:
            if(count < 4):
                print("Invalid PIN. Please Try Again")
                obj.pin_validation(count)
            else:
                print("Card Blocked")

    def showOptions(self):
        while True:
            print("\n 1. Deposit \n 2. WithDraw \n 3. Balance Enquiry \n 0. EXIT")
            choice = int(input("Enter your choice : "))

            if (choice == 1):
                obj.deposit()

            elif choice == 2:
                obj.withdraw()
            elif choice == 3:
                obj.balance_enquiry()
            elif choice == 0:
                print("Thank You for using ABC Bank. Please visit Again. Have a nice day")
                exit()
            else:
                print("Invalid Choice")



    def deposit(self):
        deposit_amount = int(input("Enter the deposit amount : "))
        if(deposit_amount < 100):
            print("Min Deposit is Rs. 100")
            obj.deposit()
        elif(deposit_amount % 100 != 0):
            print("Deposit amount should be multiples of 100")
            obj.deposit()
        elif(deposit_amount > 50000):
            print("Max Deposit Amount is Rs.50000")
            obj.deposit()
        else:
            self.account_balance = self.account_balance + deposit_amount
            print("Amount Deposited Successfully")

    def withdraw(self):
        if(self.withDrawCount > 3):
            print("Max Limit for withdraw reached !")
        else:
            withdraw_amount = int(input("Enter the amount you wish to withdraw : "))
            if (withdraw_amount < 100):
                print("Min WithDraw amount should be 100")
                obj.withdraw()
            elif withdraw_amount % 100 != 0:
                print("Withdraw Amount should be multiples of 100 only")
                obj.withdraw()
            elif self.account_balance < withdraw_amount:
                print("Insufficient Account Balance")
                obj.withdraw()
            elif (self.account_balance - withdraw_amount < 500):
                print("Minimum 500 account balance needed")
                obj.withdraw()
            else:
                self.account_balance = self.account_balance - withdraw_amount
                print("Money Debited successfully")
                self.withDrawCount = self.withDrawCount + 1


    def balance_enquiry(self):
        print("Your Balance is : " + str(self.account_balance))


obj = Bank()
obj.pin_validation(1)