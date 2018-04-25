class Quote:
    """ Programs to incooperate long carry and stairs factors
        so as to calculate a very accurate quote."""

    
    def __init__(self,name,address,bedrooms,factor):
        self.name = name
        self.address = address
        self.bedroom = bedroom
        self.factor = factor
        name_list = []

    Customer1 = Quote('Tahir', "50 S Essex Ave, Orange NJ 07050",2)
    

    def convert_bedroom_to_cuft(self):
        assert self.bedroom == int(self.bedroom)
        return self.bedroom * 576

    #def crew_factor(self, long_carry, stairs):
        #if long_carry:
           # return self.90 * .75
        #else: return self.90 * .80

    def num_crew(self, crew):
        if crew == 2:
            return 2 * crew_factor()
        elif crew == 3:
            return 3 * crew_factor()
        elif crew == 4:
            return 4 * crew_factor()
        elif crew == 5:
            return 5 * crew_factor()
        else:
            print('Consult E-Movers')   

    def quote(self):
        pass


        
    def add_customer(self):
        for self.name in name_list:
            name_list.append(self.name)
            name_list = name_list + 1
        print('There are {} names in name_list'.format(self.name))
        

    print(Tahir.convert_bedroom_to_cuft(2))
              
