class Statistics:
    def __init__(self):
        self.numbers=[]
        while True:
            try:
                self.input=int(input("Enter number: "))
                self.numbers.append(self.input)
            except:
                break
        print(" ")        

        self.x=self.numbers[0]
        for i in self.numbers:
            if i>self.x:
                self.x=i
      
        self.y=self.numbers[0]
        for i in self.numbers:
            if i<self.y:
                self.y=i

        suma=0
        for i in self.numbers:
            suma=suma+i
        self.wynik=suma/len(self.numbers)


        if len(self.numbers)%2==0:
            zm=int(len(self.numbers)/2)
            x1=self.numbers[zm]
            x2=self.numbers[zm-1]
            self.mediana=(x1+x2)/2
        else:
            self.mediana=self.numbers[len(self.numbers)//2]

    def display(self):
        leng=len(self.numbers)
        for i in range(0,leng-1):
            print(self.numbers[i],end=" ")
        print(self.numbers[-1])

        print("Greatest number: ",self.x)  
        print("Smallest number: ",self.y)
        print("Arithmetic mean: ",self.wynik)
        print("Median: ",self.mediana)



n1=Statistics()
n1.display()


