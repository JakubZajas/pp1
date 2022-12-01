icao={
    "a":"Alfa",
    "b":"Bravo",
    "c":"Charlie",
    "d":"Delta",
    "e":"Echo",
    "f":"Foxtrot",
    "g":"Golf",
    "h":"Hotel",
    "i":"India",
    "j":"Juliett",
    "k":"Kilo",
    "l":"Lima",
    "m":"Mike",
    "n":"November",
    "o":"Oscar",
    "p":"Papa",
    "q":"Quebec",
    "r":"Romeo",
    "s":"Sierra",
    "t":"Tango",
    "u":"Uniform",
    "w":"Victor",
    "x":"Whiskey",
    "y":"Yankee",
    "z":"Zulu", 
}
with open("ICAO.txt","w") as file:
    for key,value in icao.items():
        file.write(key)
        file.write(" ")
        file.write(value)
        file.write("\n")