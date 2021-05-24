from exercise_x import Teacher, Student, StudentOffice, ExamOffice

teacher1 = Teacher("Engineering")
teacher1.name()
teacher1.year()

student1 = Student(1)
student1.admit(1)
student1.subjects()

SubClass=StudentOffice(1)
SubClass.enrollment_status()

cgpa=float(input("Enter CGPA: "))
SubClass2=ExamOffice(1, cgpa)
SubClass2.pass_exam()
SubClass2.fail()
SubClass2.fr()

teacher2 = Teacher("Design")
teacher2.name()
teacher2.year()

student2 = Student(2)
student2.admit(2)
student2.subjects()

SubClass3=StudentOffice(2)
SubClass3.enrollment_status()

cgpa2=float(input("Enter CGPA: "))
SubClass4=ExamOffice(2, cgpa2)
SubClass4.pass_exam()
SubClass4.fail()
SubClass4.fr()
