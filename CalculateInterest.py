initial_balance = float(input("Enter the initial balance : "))
interest_rate = float(input("Enter the interest rate : "))
total_capital = initial_balance
n = int(input("Enter the number of years you want to calculate the interest along with the initial investment : "))
t = n
while n > 0:
    total_capital += (total_capital/interest_rate)
    print("For year ",t - (n-1),"the increased capital is : ",total_capital)
    n -=1