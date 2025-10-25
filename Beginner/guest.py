class Guest:
    def __init__(self , first , last , rank , age):
        self.last_name = last
        self.first_name = first
        self.rank = int(rank)
        self.age = int(age)
    
    def guest_info(self , all_guests):
        for guest in all_guests:
            print(guest.first_name , guest.last_name , "Age: ",guest.age )
        
    def loyalty_program(self, all_guests):
        #gold member >= 10 loyalty point

        #1. Create a list for any guest who meets certain conditions
        #2. For every guest in my list , add thier last name to the list
        #3. This condition MUST be met in order to be added to the list

        gold_members = [guest.last_name for guest in all_guests if guest.rank >= 10]
        if gold_members:
            print("Gold Members: ")
            for member in gold_members:
                print("\tGuest:", member)
        
    def guest_avg(self, all_guests):
        total_age = 0
        for guest in all_guests:
            total_age += guest.age
        avg_age = total_age / len(all_guests)
        print("Average customer age:", avg_age)



    

all_guest = list()
num_guest = int(input("Enter a number of guest: "))
for i in range(num_guest):
    data = input("First Name / Last Name / Rank / Age: ").split('/')
    guest = Guest(data[0] , data[1] , data[2] ,data[3])
    all_guest.append(guest)

guest = all_guest[0]
guest.loyalty_program(all_guest)
guest.guest_info(all_guest)