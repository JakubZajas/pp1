li=["Genowefa","Onufry","Celestyna", "Alojzy", "Pankracy"]
max=len(li[0])
najw=0
for i in range(0,len(li)-1):
    if len(li[i])>max:
        if len(li[i])>najw:
            najw=li[i]
if najw==0:
    najw=li[0]
print(najw)
