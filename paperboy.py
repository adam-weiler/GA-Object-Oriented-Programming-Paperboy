class PaperBoy(): #A PaperBoy class.
    def __init__(self, name): #Every PaperBoy has attributes name, experience, and earnings.
        self.name = name
        self.experience = 0
        self.earnings = 0

    def __str__(self): #Returns a meaninful string that describes the instance.
        return f'PaperBoy instance:name={self.name} experience={self.experience} earnings={self.earnings}'

    def quota(self): #An instance method that calculates the PaperBoy's quota.
        return 50 + (self.experience / 2) #Minimum quota is 50 plus half of experience (number of papers already delivered).

    def deliver(self, start_address, end_address): #An instance method that calculates current_earnings based on quota, start_address, and end_address.
        quota = self.quota() #Gets quota for this route.
        current_route = abs(end_address - start_address) #Number of houses delivered on this route.
        self.experience += (current_route) #Adds current_route's houses to experience.

        if (current_route > quota): #If current_route is greater than the quota, PaperBoy is rewarded for going over.
            current_earnings = ((current_route - quota) * .5) + (quota * .25) #The current_earnings is $.50 for each house over quota, plus $.25 for each house in quota.
        else: #Else the current_route is less than the quota, PaperBoy is punished for going under. 
            current_earnings = (current_route * .25) - 2 #The current_earnings is $.25 for each house in quota, minus the $2 penalty.
    
        self.earnings += current_earnings #The self.earnings is added to the current_earnings.
        return current_earnings #The current_earnings is returned. (Not the self.earnings.)

    def report(self): #Returns an plain-English string that describes the instance.
        return f"I'm {self.name}, I've delivered {self.experience} papers and I've earned ${self.earnings} so far!"


tommy = PaperBoy('Tommy')

print(f'The current quota: {tommy.quota()}') #50
tommy.deliver(100, 160) #17.5
# print(tommy.earnings) #17.5
print(tommy.report())
print()

print(f'The current quota: {tommy.quota()}') #80
tommy.deliver(1, 76) #16.75
# print(tommy.earnings) #34.25
print(tommy.report()) #"I'm Tommy, I've been delivered 135 papers and I've earned $34.25 so far!"
print()

print(tommy)
print('\n')



johnny = PaperBoy('Johnny')

print(f'The current quota: {johnny.quota()}') #50
johnny.deliver(160, 100) #17.5
# print(johnny.earnings) #17.5
print(johnny.report())
print()

print(f'The current quota: {johnny.quota()}') #80
johnny.deliver(76, 1) #16.75
# print(johnny.earnings) #34.25
print(johnny.report()) #"I'm Johnny, I've been delivered 135 papers and I've earned $34.25 so far!"
print()

print(johnny)
print('\n')



bender = PaperBoy('Bender')

print(f'The current quota: {bender.quota()}') #50
bender.deliver(1, 9) #17.5
# print(bender.earnings) #17.5
print(bender.report())
print()

print(f'The current quota: {bender.quota()}') #80
bender.deliver(1, 8) #16.75
# print(bender.earnings) #34.25
print(bender.report()) #"I'm bender, I've been delivered 135 papers and I've earned $34.25 so far!"
print()

print(bender)
print('\n')