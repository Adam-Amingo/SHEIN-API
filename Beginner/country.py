class Country:
    def __init__(self , name , capital , population):
        self.name = name 
        self.capital = capital
        self.population = population

    def get_info(self):
        return {
            "Name": {self.name},
            "Capital": {self.capital},
            "Population": {self.population}
        }
    
class DevelopedCountry(Country):
    def __init__(self, name, capital, population , gdp):
        super().__init__(name, capital, population)
        self.gdp = gdp

    def get_info(self):
        info = super().get_info()
        info["GDP"] = self.gdp
        return info
    
class DevelopingCountry(Country):
    def __init__(self, name, capital, population , hdi):
        super().__init__(name, capital, population)
        self.hdi = hdi
    
    def get_info(self):
        info =  super().get_info()
        info["HDI"] = self.hdi
        return info

class World:
    def __init__(self):
        self.countries = []

    def add_country(self, country):
        self.countries.append(country) 

    def get_country_info(self , name):
        for country in self.countries:
            if name == country.name:
                return country.get_info()
        return None


world = World()
#
usa = DevelopingCountry("United States" , "Wahsington" , 634646464 , 83746893746)
russia = DevelopedCountry("Russia" , "Moscow" , 874687464, 437487628728)
ghana = DevelopingCountry("Ghana" , "Accra" , 8476483,9479475)

world.add_country(usa)
world.add_country(russia)
world.add_country(ghana)

country_info = world.get_country_info("Unuted States")

if country_info:
    print("Country Info")
    for key , value in country_info.items():
        print(f'{key}:{value}')
else:
        print("Country not found")


