import pprint
import json


with open("load.json", "r") as f:
    data = json.load(f)


pprint.pprint(data)
