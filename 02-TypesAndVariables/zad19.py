xx=input('Enter your height in cm:')
yy=input('Enter your weight in kg:')
x=int(xx)
y=int(yy)
wzrost=x/100
BMI=y/(wzrost*wzrost)
print('BMI index:', round(BMI,2))
