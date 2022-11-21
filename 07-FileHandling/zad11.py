film_titles=["John Wick",'John Wick 2','John Wick 3','Dr. Strange','Iron-Man']

plik=open('tytuły.txt',"w",encoding="utf-8")

for i in range(0,len(film_titles)):
    plik.write(film_titles[i])
    plik.write("\n")

plik.close()