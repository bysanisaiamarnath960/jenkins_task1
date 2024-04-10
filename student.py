class Student:
    def __init__(self,x):
        self.x=x

class Course(Student):
    def cor_enroll(ce):
        print("the student enrolled for the course is :",ce)

class Grade:
    def stu_grade(g):
        print("the student grade :",g)

    def gen_trans():
        print("generate Transcripts")

obj=Course
obj.cor_enroll("computer science")

obj2=Grade
obj2.stu_grade(8.0)
obj2.gen_trans()




    

