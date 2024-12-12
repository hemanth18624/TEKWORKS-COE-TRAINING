"""
College -- Certificate
take inputs project, internal, and external score out of 100
total marks :
--->From project take 70%
--->From internal take 10%
--->From external take 20%

calculate total marks if and only if he got 50 and above in each
if in any one less than 50 print(Failed in so and so)

90+ ---> A Grade
80 to 90 ---> B Grade
50 to 80 ---> C Grade

"""

project = int(input("Enter the project marks : "))
internal = int(input("Enter the internal marks : "))
external = int(input("Enter the external marks : "))
def student_grade_calculator(project,internal,external):
    if project < 0 or internal < 0 or external < 0:
        print("Makrs cant be negitive")
    else:
        if project >= 50 and internal >= 50 and external >= 50:
            project_score = (70 / 100) * project
            internal_score = (10 / 100) * internal
            external_score = (20 / 100) * external
            total_marks = project_score + internal_score + external_score
            if (total_marks >= 90):
                print("A Grade")
            elif (total_marks >= 80):
                print("B Grade")
            else:
                print("C Grade")
        else:
            if (project < 50):
                print("Failed in project and the marks are : " + str(project))
            if (internal < 50):
                print("Failed in internal and the marks are : " + str(internal))
            if (external < 50):
                print("Failed in external and the marks are : " + str(external))



student_grade_calculator(project,internal,external)
