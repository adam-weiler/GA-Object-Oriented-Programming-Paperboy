class PaperBoy():
	#name, experience, earnings

    def __init__(self, name):
        self.name = name
        self.experience = 0
        self.earnings = 0

    def __str__(self):
        return f'PaperBoy instance:name={self.name} experience={self.experience} earnings={self.earnings}'

    def quota(self):
        # self.quota = quota
        quota = 50 + (self.experience / 2)
        return quota
         #Minimum: At least 50 papers
        #Quota = Experience / 2 + Minimum

    def deliver(self, start_address, end_address):
        quota = self.quota()

        self.experience += (end_address - start_address)

        # self.earnings += self.experience


        if (self.experience < quota):
            print('not enoguh!')
            print(self.experience)
            print(quota)
            pass
        else:
            self.earnings += ((self.experience - quota) * .5) + (quota * .25)


            
            
            
            
            print('Thats good!')
            print(self.experience)
            print(quota)
            # self.earnings += self.experience * .25


            



        
        return self.earnings



    def report(self):
        pass

        #.25 for each paper
        #.50 for each paper over quota
        #-2.0 if they didn't meet quota.
       

        #Run 1, quota = 50
        #Run 2, quota = 50 + (.5 * papers delivered before)


# johnny = PaperBoy('Johnny', 0, 0)
# print(johnny.quota())
# print(johnny.quota())
# print(johnny.deliver(42, 45))

# print(johnny)



tommy = PaperBoy('Tommy')
print(tommy.quota()) #50
print(tommy.deliver(100, 160)) #17.5

print(tommy)