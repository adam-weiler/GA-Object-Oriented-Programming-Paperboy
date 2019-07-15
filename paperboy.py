class PaperBoy():
	#name, experience, earnings

    def __init__(self, name):
        self.name = name
        self.experience = 0
        self.earnings = 0

    def __str__(self):
        return f'PaperBoy instance:name={self.name} experience={self.experience} earnings={self.earnings}'

    def quota(self):
        quota = 50 + (self.experience / 2)
        return quota

    def deliver(self, start_address, end_address):
        quota = self.quota()

        current_route = end_address - start_address

        self.experience += (current_route)

        if (current_route < quota):
            print('Not Enough!')
            # print(self.experience)
            # print(quota)
            #-2.0 if they didn't meet quota.
            current_earnings = (current_route  * .25) - 2
            # print(self.earnings)
        else:
            print('You sold enough papers!')
            # print(self.experience)
            # print(quota)
            current_earnings = ((current_route - quota) * .5) + (quota * .25)
        
        self.earnings += current_earnings

        return current_earnings

    def report(self):
        return f"I'm {self.name}, I've delivered {self.experience} papers and I've earned ${self.earnings} so far!"


tommy = PaperBoy('Tommy')

print(tommy.quota()) #50
print(tommy.deliver(100, 160)) #17.5
print(tommy.earnings) #17.5
print(tommy.report())
print()

print(tommy.quota()) #80
print(tommy.deliver(1, 76)) #16.75
print(tommy.earnings) #34.25
print(tommy.report()) #"I'm Tommy, I've been delivered 135 papers and I've earned $34.25 so far!"
print()

print(tommy)



# johnny = PaperBoy('Johnny')
# print(johnny.quota())
# print(johnny.quota())
# print(johnny.deliver(42, 45))

# print(johnny)