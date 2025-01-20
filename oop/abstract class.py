from abc import ABC, abstractmethod

'''

abstract class: a class that cannot be instantianted by its own;
                            meant to be subclassed;
                they can contain abstract methods, which are declared 
                            but have no implementation
                1. prevents instantiation of the class itself
                2. requires children to use inherited abstract methods


The module ABC is specifically desigdned to ensure that no subclass forgets
to implement the required methods!

'''

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    
    def go(self):
        print('you drive the car')

    def stop(self):
        print('you stop the car')


class Motorcycle(Vehicle):
    def go(self):
        print('you ride the motorcycle')

    def stop(self):
        print('you stop the motorcycle')
