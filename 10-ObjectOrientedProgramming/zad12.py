class TV:
    def __init__(self):    
        self.is_on=False
        self.channel_no=0
        self.channels=[]

    def turn_on(self):  
        self.is_on=True
    def turn_off(self):
        self.is_on =False
    def show_status(self,channel):
        if self.is_on:
            self.channel_no=channel
            print("tv is on, channel",self.channel_no,self.channels[channel])
        else:
            print("tv is off")

    def set_channel(self,number):
        self.channel_no=number

    def set_channels(self,channels_list):
        self.channels.append(channels_list)


    def show_channels(self):
        print(self.channels)
            

telewizor=TV()
telewizor.show_status(0)
telewizor.turn_on()
telewizor.set_channels("channel 0")
telewizor.set_channels("TVP1")
telewizor.set_channels("TVP2")
telewizor.set_channels("Polsta")
telewizor.set_channels("TVN")
telewizor.set_channels("filmbox")
telewizor.set_channels("Discovery")
telewizor.set_channels("BBC")
telewizor.show_channels()
telewizor.show_status(1)
telewizor.show_status(2)
telewizor.show_status(3)
telewizor.show_status(4)
telewizor.show_status(5)
telewizor.show_status(6)
telewizor.show_status(7)
telewizor.turn_off()
telewizor.show_status(0)
