# import csv
# with open("student.csv") as file:
#     for line in file:
#        name , house  = line.rstrip().split(",")
#        print(f"{name} is in {house}")


# students = []

# with open ("student.csv") as file:
#     for line in file :
#         name , house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)

######################
###################
# students = []

# with open ("student.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name" : row['name'] , "house" : row['house']})
    

# for student in sorted(students , key= lambda student: student['name']) :
#     print(f"{student['name']} is in {student['house']}")
    ###############
    ###############


# students = []

# with open ("student.csv") as file:
#     for line in file :
#         name , house = line.rstrip().split(",")
#         student = {"name" : name, "house" :house}
#         students.append(student)
    

# for student in sorted(students , key= lambda student: student['name']) :
#     print(f"{student['name']} is in {student['house']}")


# import csv 


# name = input("Whats your name? ")
# house = input("Wheres your house? ")

# with open("student.csv" , "a") as file:
#     writer = csv.DictWriter(file , fieldnames= ["name" , "house"])
#     writer.writerow({"name" : name , "house" : house})

class Student:
    def __init__(self, name , house):
        self.name = name 
        self.house = house
        
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("house: ")
        return cls(name , house)
    
    
    



def main():
    student = Student.get()
    print(student)
   



if __name__ ==  "__main__":
    main()
    




