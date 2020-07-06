class Student():
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def lunch(self):
        print(self.name + " " + "is on lunch")

    def __home(self):
        print(self.name + "is at home")


m = Student("Mehdi", "21", "DevOps")




