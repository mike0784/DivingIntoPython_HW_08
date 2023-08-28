import csv

__all__ = ["readCSVFile"]

def readCSVFile(file: str) -> dict:
    result = {}
    if verificationFile(file):
        with open(file, "r", encoding="utf8") as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                status = row['status']
                id = row['id']
                name = row['name']
                if status in result.keys():
                    result[status][id] = name
                else:
                    result[status] = {id: name}
        return result
    else:
        return None