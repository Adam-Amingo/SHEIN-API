from abc import ABC , abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("You drive the car")
    
    def stop(self):
        print("You stop the car")
    

class Motorcycle:
    def go(self):
        print("You ride the motocycle")
    
    def stop(self):
        print("You stop the motorcycle")

car = Car()
car.go()