roll_no = input("Enter the student name : ")
name = input("Enter the student name : ")
cMarks = float(input("Enter the marks in C"))
cPMarks = float(input("Enter the marks in C++"))
javaMarks = float(input("Enter the marks in Java : "))
total_marks = cMarks + cPMarks + javaMarks
avg_marks = total_marks / 3
print("The total marks obtained is : ",total_marks)
if avg_marks < 70:
    print("Fail")
else:
    if avg_marks > 90:
        print("A Grade")
    elif avg_marks > 80:
        print("B Grade")
    else:
        print("C Grade")