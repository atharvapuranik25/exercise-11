class Teacher:

    def __init__(self, subject):
        self._subject = subject

    def name(self):
        """return name of subject"""
        print("Subject: ", self._subject)

    def year(self):
        """return year"""
        year = int(input("Year of starting: "))
        print ("Year: ", year)

class Student:

    def __init__(self, batch):
        self._batch = batch

    def admit(self, program):
        """return name of program"""
        if program == 1:
            program = "\nProgram: Computer Science and Engineering"
            print(program)
        elif program == 2:
            program = "\nProgram: Communication Design"
            print(program)
        else:
            print("\nInvalid Program")

    def subjects(self):
        """returns list of subjects"""
        if self._batch == 1: # B.Tech
            print("\nSubjects:\nNature and Design\nDesign Methodology\nIntroduction to Computing\nPrinciples of Engineering\n")
        elif self._batch == 2: # B.Des
            print("\nSubjects:\nCreative Visualization\nSemiotics\nPhotography\nCritical and Creative Thinking\n")
        else:
            print("\nInvalid Batch")

class StudentOffice(Student):
    """Extending class Student"""

    def __init__(self, batch):
        super().__init__(batch) # calling super constructor

    def enrollment_status(self):
        """returns enrollment status of batch"""
        if self._batch == 1:
            year = int(input("Enter enrolment year for B.Tech (2020 or 2021): "))
            if year == 2020:
                print("Enrolment Status: Active")
            elif year == 2021:
                print("Enrolment Status: Inactive")
            else:
                print("Enter a valid year")
        elif self._batch == 2:
            year = int(input("Enter enrolment year for B.Des (2020 or 2021): "))
            if year == 2020:
                print("Enrolment Status: Active")
            elif year == 2021:
                print("Enrolment Status: Inactive")
            else:
                print("Enter a valid year")
        else:
            print("Invalid Batch")

    def attendance(self):
        """attendance status"""
        attend = int(input("Enter attendance (in %): "))
        return attend

class ExamOffice(StudentOffice):

    """Extending class StudentOffice"""

    def __init__(self, batch, CGPA):

        super().__init__(batch)
        self._CGPA = CGPA

    def pass_exam(self):
        """returns pass if cgpa > 5"""
        if self._CGPA > 5:
            print("Pass\n")
        else:
            return False

    def fail(self):
        """returns fail if cgpa < 5"""
        if self._CGPA < 5:
            print("Fail\n")
        else:
            return False

    def fr(self):
        """returns fail due to reason if attendance < 50%"""
        attend = super().attendance()
        if attend < 50 and self._CGPA < 5:
            print("Fail due to reason\n")
        else:
            pass
