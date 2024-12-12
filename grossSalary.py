"""
accept basic salary as input and find gross salary
gs = HRA + DA + Basic
basic < 1000 ---
--->HRA = 67 % on basic salar
--->DA = 73 % on basic salary
basic between 10k and 20k---
--->hra = 69 % on basic salary
--->da = 76% on basic salary
basic above 20k:
---> hra = 73 %on basic salary
---> da = 89 % of basic salary

"""
def calculate_gross_salary(basic_salary):
    if(basic_salary < 0):
        print("Salary cannot be negitive")
    else:
        if (basic_salary < 10000):
            hra = (67 / 100) * basic_salary
            da = (73 / 100) * basic_salary
        elif (basic_salary < 20000):
            hra = (69 / 100) * basic_salary
            da = (76 / 100) * basic_salary
        else:
            hra = (73 / 100) * basic_salary
            da = (89 / 100) * basic_salary
        gross_salary = basic_salary + hra + da
        print("The gross salary is : " + str(gross_salary))


basic_salary = int(input("Enter the employee salary : "))
calculate_gross_salary(basic_salary)