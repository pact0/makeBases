import json
from json.decoder import JSONDecoder

data ={}

a = open('./test.json')
test = json.load(a)

tiers = {
    '68': {'tier':1},
    '69': {'tier':2},
    '70': {'tier':3},
    '71': {'tier':4},
    '72': {'tier':5},
    '73': {'tier':6},
    '74': {'tier':7},
    '75': {'tier':8},
    '76': {'tier':9},
    '77': {'tier':10},
    '78': {'tier':11},
    '79': {'tier':12},
    '80': {'tier':13},
    '81': {'tier':14},
    '82': {'tier':15},
    '83': {'tier':16},
}

def getBases():
    for key,value in test.items():
        if value["item_class"] == "Map":
            newObject = {}
            newObject["base"] = value["item_class"]
            newObject["name"] = value["name"]
            newObject["w"] = value["inventory_width"]
            newObject["h"] = value["inventory_height"]
            newObject["img"] = value["visual_identity"]["dds_file"].replace(".dds",".png")
            print(newObject)



getBases()
with open("map_bases.json", "w") as write_file:
    json.dump(data, write_file)
