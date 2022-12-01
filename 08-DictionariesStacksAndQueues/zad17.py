import json
with open("euro.json","r") as file:
    data=json.load(file)

print("Date           Buying Rates      Selling Price")
print("="*46)

for i in data:
    if i!="table":
        break
    for k in data["rates"]:
        for key,value in k.items():
            if key=="effectiveDate":
                print(value,end="     ")
            elif key=="bid":
                value=str(value)
                if len(value)<6:
                    value=value+"0"
                print(value,end="            ")
            elif key=="ask":
                print(value)