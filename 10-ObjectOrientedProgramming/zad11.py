class TV:
    def __init__(self):    
        self.is_on=False
        self.channel_no=1
        self.channels=[]

    def turn_on(self):  
        self.is_on=True
    def turn_off(self):
        self.is_on =False
    def show_status(self):
        if self.is_on:
            print("tv is on, channel",self.channel_no)
        else:
            print("tv is off")

    def set_channel(self,number):
        self.channel_no=number

    def set_channels(self,channels_list):
        self.channels.append(channels_list)


    def show_channels(self):
        print(self.channels)
            

telewizor=TV()
telewizor.show_status()
telewizor.turn_on()
telewizor.show_status()
telewizor.show_channels()
telewizor.set_channels("TVP1,TVP2, Polsat, TVN, Filmbox, Discovery")
telewizor.show_channels()
telewizor.show_status()
telewizor.turn_off()
telewizor.show_status()