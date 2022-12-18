class TV:
    def __init__(self):    
        self.is_on=False

    def turn_on(self):  
        self.is_on=True
    def turn_off(self):
        self.is_on =False
    def show_status(self):
        if self.is_on:
            print("tv is on")
        else:
            print("tv is off")
            

telewizor=TV()
telewizor.show_status()
telewizor.turn_on()
telewizor.show_status()
telewizor.turn_off()
telewizor.show_status()

