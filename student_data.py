# Below we are initialising a class for a student with variables name, age and course.

class Student():
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

# Below we are creating two functions, one to state the student is on lunch and one to state that they are at home.

    def lunch(self):
        print(self.name + " " + "is on lunch")

    def test_date(self):
        pass

# The above function is a template for a students test date. However, only DevOps students have an upcoming
# so we need to write 'pass' here.

m = Student("Mehdi", "21", "DevOps")






