#Pass or fail grading application for CSIS110
#Programmer: Kevin Nolan
#Date: 2/23/2026

print("Please Enter the grades for the following Exams")
print("Exam 1: ") ;grade1 = input("") ;grade1 = int(grade1)
print("Exam 2: ") ;grade2 = input("") ;grade2 = int(grade2)


average = (grade1 + grade2) / 2

if average  >60:
    print("Congratulations! You passed the class with an average of: " + str(average))
else:    print("Sorry, you failed the class with an average of: " + str(average))
