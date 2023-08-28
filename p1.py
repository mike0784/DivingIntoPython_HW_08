import json
import os

result = list()

def listDirectories(dir: str) -> None:
    os.chdir(dir)
    content = os.listdir()
    for obj in content:
        if os.path.isfile(obj):
            size = os.path.getsize(obj)
            temp = {"file": obj, "parent": dir, "type": "file", "size": size}
            result.append(temp)
        if os.path.isdir(obj):
            size = os.path.getsize(obj)
            temp = {"file": obj, "parent": dir, "type": "directories", "size": size}
            result.append(temp)
            listDirectories(obj)
    os.chdir("..")

def writeToJSON(ls: list, file: str) -> None:
    with open(file, "w") as f:
        json.dump(ls, f)

if __name__ == "__main__":
    file = os.getcwd() + "\\Result.json"
    listDirectories("i:\\DOS")
    writeToJSON(result, file)

