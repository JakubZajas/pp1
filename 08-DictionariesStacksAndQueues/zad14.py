import re
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
input=input("Enter Text: ")
input=input.lower()
list=[]
for letter in input:
    list.append(letter)

print("Spelled text: ",end="")

for i in list:
    for key,value in icao.items():
        if i==key:
            print(value, end=" ")

