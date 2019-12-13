import csv
from ast import literal_eval
import json

def helper(children):
    child_array = []
    for each in children:
        obj = {}
        obj["name"] = rows[each][1]
        obj["id"] = rows[each][0]
        obj["pathName"] = "&nbsp;<i class='right'></i>&nbsp;".join(literal_eval(rows[each][6]))
        obj["numChildren"] = rows[each][5]
        obj["productCount"] = rows[each][2]
        obj["subtreeProductCount"] = rows[each][3]
        arr = literal_eval(rows[each][7])
        if(len(arr)>0):
            obj["children"] = helper(arr)

        child_array.append(obj)

    return child_array




rows = []

maxChildVal = 0

with open('all-nodes.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    
    for row in readCSV:
        if(maxChildVal<int(row[5])):
            maxChildVal = int(row[5])
        
        rows.append(row)

main_children = literal_eval(rows[0][7])

result = {
    "name": "all-nodes",
    "id":0,
    "pathName":"all-nodes",
    "numChildren":len(main_children),
    "productCount":rows[0][2],
    "subtreeProductCount":rows[0][3],
    "children": [],
    "childrenNormalizationValue":maxChildVal
    }

for child in main_children:
    obj = {}
    obj["name"] = rows[child][1]
    obj["id"] = rows[child][0]
    obj["pathName"] = "&nbsp;<i class='right'></i>&nbsp;".join(literal_eval(rows[child][6]))
    obj["numChildren"] = rows[child][5]
    obj["productCount"] = rows[child][2]
    obj["subtreeProductCount"] = rows[child][3]
    arr = literal_eval(rows[child][7])
    if(len(arr)>0):
        obj["children"] = helper(arr)

    result["children"].append(obj)

with open('all-nodes.json', 'w') as f:
    json.dump(result, f)



