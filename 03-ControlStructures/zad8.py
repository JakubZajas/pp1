Paul=21
Annie=18
if Paul>=18 and Annie>=18:
    print("Oboje są dorośli")
elif Paul<18 and Annie>=18:
    print("Paul nie jest dorosły a Annie jest")
elif Paul>=18 and Annie<0:
    print("Annie nie jest dorosła a Paul jest")
else:
    print("Oboje nie są dorośli.")
    