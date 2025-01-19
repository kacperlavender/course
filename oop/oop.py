from car import Car

"""
object = a 'boundle' of related attribues (variables) and methods (functions)
        for example. phone, cup or book
        you need a 'class' to create many objects

class = (blueprint) used to design the structure and layout

methods are actions that our objects can perform 

"""



# Other file
"""

class Car:
    def __init__(self, model, year, color, for_sale): # Constructor, which we need to create objects
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f'you drive the {self.color} {self.model}')

    def stop(self):
        print(f'you stop the {self.color} {self.model}')

    def describe(self):
        print(f'{self.year} {self.color} {self.model}')
        
"""


car1 = Car("BMW", 2022, "black", False) # Creating new cars
car2 = Car("Porsche", 2021, "black", True)


print(car1.model, car1.year, car1.color, car1.for_sale) 
print(car2.model, car2.year, car2.color, car2.for_sale)

car1.drive()
car1.stop()
car1.describe()