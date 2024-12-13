import streamlit as st

def student_grade_calculator(project, internal, external):
    if project < 0 or internal < 0 or external < 0:
        st.error("Marks can't be negative!")
    else:
        if project >= 50 and internal >= 50 and external >= 50:
            project_score = (70 / 100) * project
            internal_score = (10 / 100) * internal
            external_score = (20 / 100) * external
            total_marks = project_score + internal_score + external_score
            if total_marks >= 90:
                st.success(f"A Grade with total marks: {total_marks:.2f}")
            elif total_marks >= 80:
                st.success(f"B Grade with total marks: {total_marks:.2f}")
            elif total_marks >= 50:
                st.success(f"C Grade with total marks: {total_marks:.2f}")
        else:
            if project < 50:
                st.warning(f"Failed in project with marks: {project}")
            if internal < 50:
                st.warning(f"Failed in internal with marks: {internal}")
            if external < 50:
                st.warning(f"Failed in external with marks: {external}")

# Streamlit app layout
st.title('Student Grade Calculator')

# Input fields for project, internal, and external marks, disabling the + and - buttons
project = st.number_input("Enter the project marks:", min_value=0, max_value=100, value=0, step=1)
internal = st.number_input("Enter the internal marks:", min_value=0, max_value=100, value=0, step=1)
external = st.number_input("Enter the external marks:", min_value=0, max_value=100, value=0, step=1)

# Calculate and display result on button click
if st.button("Calculate Grade"):
    student_grade_calculator(project, internal, external)
