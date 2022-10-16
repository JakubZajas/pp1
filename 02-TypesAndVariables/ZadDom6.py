x = 'X-DSPAM-Confidence: 0.8475'
y=x.find(":")
print(y)
z=x.find("5")
print(z)
xx=x[y+1:z]
koniec=float(xx)
print(koniec)
