def f(human_age):
    human_age=int(human_age)
    if human_age>2:
        dog_age=20
        age=human_age-2
        new_age=age*4
        age=dog_age+new_age

        print(age)
        return age
    elif human_age==1:
        age=10
        print(age)
        return age
    elif human_age==2:
        age=20
        print(age)
        return age

    
f(15) 
f(2)