import json

def writeJsonFile(file: str, data: dict) -> None:
    with open(file, "w", encoding="utf8") as f:
        json.dump(data, f, indent=2)