import json
film={
    "title":"John Wick",
    "genre":"Action",
    "Year_of_Production":2016,
    "Actors":{
        "Keanu Reeves":"good",
        "the rock":"bad"
        },
    "Rating":"10/10",
    
}

with open("favourite.json","w") as file:
    json.dump(film,file,indent=2)

file.close()