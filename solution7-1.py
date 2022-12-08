lines = list(l.strip() for l in open("./input7.txt").readlines())
fs = {}
maxSize = 100000
currMode = ""
currDirIndex = 0
#1557346
fs = [
    {
        "id": "/",
        "index": 0,
        "size": 0,
        "parent": None,
        "children": []
    }
]
currDir = fs[currDirIndex]
def getIndexFromId(indices, id):
    for i in range(len(indices)):
        if fs[indices[i]]["id"] == id:
            return indices[i]
    return False
total = 0
for l in lines:
    if l == "$ cd /":
        currDirIndex = 0
        continue
    data = l.split(" ")
    if l[0] == "$":
        instr = data[1]
        if instr == "cd":
            newDirId = data[2]
            if newDirId == "..":
                if currDir["id"] != "/":
                    parent = fs[fs[currDirIndex]["parent"]]
                    currDirIndex = parent["index"]
                    currDir = fs[currDirIndex]
            else:
                for i in fs[currDirIndex]["children"]:
                    if fs[i]["id"] == newDirId:
                        currDirIndex = i
                        currDir = fs[currDirIndex]
                        break

    else:
        if data[0] == "dir":
            newDirId = data[1]
            fs.append({
                "id": newDirId,
                "index": len(fs),
                "size": 0,
                "parent": currDirIndex,
                "children": []
            })
            fs[currDirIndex]["children"].append(len(fs) - 1)
        else:
            size = int(data[0])
            fs[currDirIndex]["size"] += size
            currIterDirIndex = fs[currDirIndex]["parent"]
            while currIterDirIndex != None:
                fs[currIterDirIndex]["size"] += size
                currIterDirIndex = fs[currIterDirIndex]["parent"]
    #print(l, currDir)
print(sum(list(i["size"] for i in fs if i["size"] <= maxSize)))
for i in fs:
    #print(i)
    pass