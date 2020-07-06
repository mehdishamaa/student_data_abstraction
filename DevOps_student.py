from student_data import Student

# Here we have the Student class from the student_data.py file
# Next we initialise a new class for DevOps students

class Devops(Student):

    def __init__(self, name, age, course, ability):
        self.name = name
        self.age = age
        self.course = course
        self.ability = ability

    def lunch(self):
        print(self.name + " " + "is on lunch")

    def __home(self):
        print(self.name + "is at home")

    def study(self):
        print(self.ability + 5)

me = Devops("Mehdi","21", "DevOps", 5)

print(me.study())
