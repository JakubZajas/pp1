kraje=[
    {"Country":"Polska","Populacja":30000000},
    {"Country":"Islandia","Populacja":3000},
    {"Country":"Niemcy","Populacja":500000},
    {"Country":"Hiszpania","Populacja":60000000},
    {"Country":"Grenlandia","Populacja":100}
    ]

for kraj in kraje:
    for key, value in kraj.items():
        print(key,":",value)
    