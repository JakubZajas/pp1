with open("lista.txt","r") as f:
    for line in f:
        print(line, end="")
f.close()