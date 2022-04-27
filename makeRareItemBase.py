import json
from json.decoder import JSONDecoder

data ={}

a = open('./test.json')
test = json.load(a)

f = open('./test2.json')
test2 = json.load(f)

g = open('./baseTypes.json')
baseTypes = json.load(g)

h = open('./baseGroups.json')
baseGroups = json.load(h)

jewels = {
{
    "Large Cluster Jewel": {"id_bitem": "12", "id_base": "69", "name_bitem": "Large Cluster Jewel", "drop_level": "1","properties": "[]", "requirements": "[]", "implicits": "[]", "exp":"0", "imgurl": "Jewels/NewGemBase3.png?w=1&h=1", "is_legacy": "0", "exmods": null, "w": 1, "h": 1, "baseGroup": "Jewel", "base": "Large Cluster Jewel"},
    "Small Cluster Jewel": {"id_bitem": "12", "id_base": "70", "name_bitem": "Small Cluster Jewel", "drop_level": "1","properties": "[]", "requirements": "[]", "implicits": "[]", "exp":"0", "imgurl": "Jewels/NewGemBase1.png?w=1&h=1", "is_legacy": "0", "exmods": null, "w": 1, "h": 1, "baseGroup": "Jewel", "base": "Small Cluster Jewel"},
    "Medium Cluster Jewel": {"id_bitem": "12", "id_base": "71", "name_bitem": "Medium Cluster Jewel", "drop_level": "1","properties": "[]", "requirements": "[]", "implicits": "[]", "exp":"0", "imgurl": "Jewels/NewGemBase2.png?w=1&h=1", "is_legacy": "0", "exmods": null, "w": 1, "h": 1, "baseGroup": "Jewel", "base": "Medium Cluster Jewel"},
}

def getBases():
    for key,value in test.items():
        for list in test2:
            if "Cluster" in value["name"]:
                print(value["name"])
            if list["name_bitem"] == value["name"]:
                newObject = list
                newObject["w"] = value["inventory_width"]
                newObject["h"] = value["inventory_height"]
                baseId = newObject["id_base"]
                base = ""

                for base in baseTypes:
                    if base["id_base"] == baseId:
                        baseTypeId = base["id_bgroup"]

                        for baseGroup in baseGroups:
                            if base["id_bgroup"] == baseGroup["id_bgroup"]:
                                newObject["baseGroup"] = baseGroup["name_bgroup"]

                        newObject["base"] = base["name_base"]
                        break;

                data[value["name"]] = newObject
                img = value["visual_identity"]["dds_file"].split("/")[2:-1]
                # print(list["name_bitem"],img)



getBases()
with open("result.json", "w") as write_file:
    json.dump(data, write_file)
