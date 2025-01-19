'''

inheritance = allows a class to inherit attributes and methods from another class
            helps with code reusability and extensibility
            class Child(Parent)

'''

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is asleep')

class Dog(Animal):
    def speak(self):
        print('woof') # we add special behaviors to certain Child class

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog = Dog('marco')
cat = Cat('garfield')
mouse = Mouse('mickey')

print(cat.name) # even tho Child classes are empty - they still have atrbiutes of Parent class
print(cat.is_alive)

dog.eat()
dog.speak()
mouse.sleep()