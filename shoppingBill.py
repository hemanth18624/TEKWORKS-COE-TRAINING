salary = int(input("Enter the employee salary: "))
sb1 = int(input("Enter the shopping bill1 amount: "))
sb2 = int(input("Enter the shopping bill2 amount: "))
sb3 = int(input("Enter the shopping bill3 amount: "))

total_bill = sb1 + sb2 + sb3
print("Total bill amount spent is: " + str(total_bill))
if total_bill > salary:
    print("Salary is not sufficient")
else:
    percentage_of_salary_spent = (total_bill / salary) * 100
    print("Percentage of salary spent is: " + str(percentage_of_salary_spent))