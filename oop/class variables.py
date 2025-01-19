'''
class variables = Shared among all instances of a class
                Defined outside the constructor
                Allow you to share data among all objects created from that class
'''

class Student:
     
     class_year = 2024 # Variables inside of whole class avaiblable for every object
     num_students = 0
     
     def __init__(self, name, age):
          self.name = name
          self.age = age
          Student.num_students += 1

student1 = Student('spongebob', 30)
student2 = Student('freakbob', 35)
student3 = Student('squidward', 55)
student4 = Student('sandy', 27)


# While refering to class variables its important to use Student.{something} instead of certain object
print(student1.name, student1.age, Student.class_year, Student.num_students)
print(f'my graduating class of {Student.class_year} has {Student.num_students}')