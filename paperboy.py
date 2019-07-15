class PaperBoy():
	#name, experience, earnings

    def __init__(self, name, experience, earnings):
        self.name = name
        self.experience = experience
        self.earnings = earnings

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



        self.earnings += (end_address - start_address) 
        
        return earnings

    def report(self):
        pass

        #.25 for each paper
        #.50 for each paper over quota
        #-2.0 if they didn't meet quota.
       

        #Run 1, quota = 50
        #Run 2, quota = 50 + (.5 * papers delivered before)


johnny = PaperBoy('Johnny', 0, 0)
print(johnny)