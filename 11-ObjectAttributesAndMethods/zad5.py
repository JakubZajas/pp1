class Music():
    def __init__(self,Artist,Track_Title, Album, Year):
        self.artist=Artist
        self.name=Track_Title
        self.album=Album
        self.year=str(Year)

    def __str__(self):
        return f"Performer: {self.artist} \nSong:      {self.name} \nAlbum:     {self.album}\nYear:      {self.year} \n"

m1=Music("Ed Sheeran","Hearts Don't Break Around Here","Divide","2017")
print(m1)
m2=Music("Twenty One Pilots","Stressed Out","IDK MAN",2015)
print(m2)