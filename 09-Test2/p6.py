def f(age, course, average):
    import json
    with open("test.json","r") as file_json:
        file=json.load(file_json)
        result=0
        for i in file:
            for key,value in i.items():
                if key=="age":
                    if value>=age:
                        for x in i["studies"]["courses"]:
                            if x["name"] == course:
                                suma=0
                                for value in x["grades"]:
                                    suma=suma+value
                                avg=suma/len(x["grades"])
                                if avg>=average:
                                    result=result+1


                        
        print(result)

    file_json.close()

f(21, "statistics", 4) 