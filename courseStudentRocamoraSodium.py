class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def displayInfo(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Course:
    def __init__(self, name):
        self.name = name
        self.student= []

    def addStudent(self, student):
        self.student.append(student)

    def displayInfos(self):
        print(f"Course: {self.name}")
        for student in self.student:
            print(f"Student('{student.name}', {student.age})")  
        
    

student0 = Student("Placeholder", 0)
student1 = Student("Tinoy", 15)
student2 = Student("Yan", 18)

course1 = Course("Math")
course1.addStudent(student0)
course1.addStudent(student1)
course1.addStudent(student2)

course1.displayInfos()

