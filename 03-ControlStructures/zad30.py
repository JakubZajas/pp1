enterNumber = int(input("List of nth prime numbers: "))
startNumber = 1
primeList = []
while True:
    if enterNumber <= 0:
        print("The entry MUST be greater than zero.")
        break
    if startNumber > 1:
        for i in range(2,startNumber):
            if (startNumber % i) == 0:
                break
        else:
            primeList.append(startNumber)
    if (len(primeList) == enterNumber):
        print(primeList)
        break
    else:
        startNumber = startNumber + 1
        continue


