from student_data import Student

# Here we have the Student class from the student_data.py file
# Next we initialise a new class for DevOps students

class Devops(Student):

    def __init__(self, name, age, course, grade):
        self.name = name
        self.age = age
        self.course = course
        self.grade = grade

    def lunch(self):
        print(self.name + " " + "is on lunch")

    def __home(self):
        print(self.name + "is at home")

# Below we have added a new function to this class. The study function increases the students ability.

    def study(self):
        self.ability = self.ability + 5
        print("Student has finished studying, ability is now:", self.ability)

    def test_date(self):
        print("Your test date is next Friday!")


m = Devops("Mehdi","21", "DevOps", 5)

print(m.test_date())

