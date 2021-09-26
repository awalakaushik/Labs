#Dictionary Exercise 3 (Lists as Values)
#(1 point possible)
#Write a function that accepts a dictionary as input which contains the names and grades of students (The keys are student names and the values are lists of grades for 3 exams (1 Dimensional list)) and returns the list of names for those students whose grade on all three exams is greater than or equal to 78.

def overall_grade(dic):
    student_list=[]
    keys=dic.keys()
    for key in keys:
        student_data=dic[key]
        grade1,grade2,grade3=student_data[0],student_data[1],student_data[2]
        if grade1>=78 and grade2>=78 and grade3>=78:
            student_list.append(key)
    return student_list