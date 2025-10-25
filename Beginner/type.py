import random

class Hat:
    
    houses = ['Kumasi' , "Accra" , "Bono"]

    @classmethod
    def sort(cls , name):
        
        print(name , "is in ",random.choice(cls.houses))



Hat.sort("Harry")