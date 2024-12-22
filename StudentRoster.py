class Student:
    def __init__(self,student_id,student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None

    def display_attributes(self):
        print("The attributes and values of students are : ")
        print(f"Student ID : {self.student_id}")
        print(f"Student Name : {self.student_name}")
        if self.student_class:
            print(f"Student Class : {self.student_class}")

student_id = input("Enter the student id : ")
student_name = input("Enter the student name : ")
student1 = Student(student_id,student_name)
student1.display_attributes()