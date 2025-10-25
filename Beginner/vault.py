class Vault:
    def __init__(self , gallions = 0 , sickles = 0 , knuts = 0):
        self.gallions = gallions
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.gallions} gallions ,{self.sickles} sickles, {self.knuts} knuts"
    
    def __add__(self , other):
        galleons = self.gallions + other.gallions
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        
        return Vault(galleons , sickles , knuts)



potter = Vault(100 , 50 , 25)
print(potter)

weasley = Vault(25 , 10 , 100)
print(weasley)


total = potter + weasley
print(total)