class Thermometr:
    def __init__(self):
        from random import uniform
        self.temp=round(uniform(34.0,42.0),1)
        self.stan=False
    
    def turn_on(self):
        self.stan=True

    def turn_off(self):
        self.stan=False
    
    def display(self):
        if self.temp:
            if self.temp<=42.0 and self.temp>=41.0:
                print(self.temp,"CRITICAL TEMPERATURE!!!")
            elif self.temp>=37.0:
                print(self.temp,"(fever)")
            else:
                print(self.temp)