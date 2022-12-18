class TV:
    def __init__(self):    
        self.is_on=False
        self.channel_no=0
        self.channels=[]
        self.volume=0

    def turn_on(self):  
        self.is_on=True
    def turn_off(self):
        self.is_on =False
    def show_status(self):
        if self.is_on:
            print("tv is on, volume: ",self.volume)
        else:
            print("tv is off")

    def set_channel(self,number):
        self.channel_no=number

    def set_channels(self,channels_list):
        self.channels.append(channels_list)


    def show_channels(self):
        print(self.channels)

    def turn_down(self):
        if self.volume>0 and self.volume<=10:
            self.volume=self.volume-1         
    def turn_up(self):
        if self.volume>=0 and self.volume<10:
            self.volume=self.volume+1
telewizor=TV()
telewizor.show_status()
telewizor.turn_on()
telewizor.show_status()
telewizor.turn_up()
telewizor.turn_up()
telewizor.turn_up()
telewizor.turn_up()
telewizor.show_status()
telewizor.turn_down()
telewizor.turn_down()
telewizor.show_status()
telewizor.turn_off()