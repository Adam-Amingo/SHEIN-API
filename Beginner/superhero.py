class Superhero:
    def __init__(self , name , power):
        self.name = name 
        self.power = power
    
    def use_power(self):
        print(f"{self.name} is using {self.power} power!")
    
    def intro(self):
        print(f"I am {self.name} and I have {self.power} power!")
    
    def save_day(self):
        print(f"{self.name} has saved the day")
    
    def power_level(self):
        lenght = len(self.power)
        level = lenght*10 
        return level
    
class Flying(Superhero):
    def __init__(self , name , power , speed):
        super().__init__(name , power)
        self.speed = speed

    def use_power(self):
        print(f"{self.name} is flying at the speed of {self.speed} miles per hour")
    
    def calc_distance (self, flight_time):
        distance = self.speed * flight_time
        return distance






    #
batman = Superhero("Batman" , "Flight")
batman.intro()
batman.save_day()
print(batman.power_level())

superman = Flying("Superman" , "flight" , 258)
superman.intro()
superman.use_power()

print()
flight_dist = 30
attack = superman.calc_distance(flight_dist)
print(f"{superman.name} can fly at a distance of {attack} miles in {flight_dist} hours")