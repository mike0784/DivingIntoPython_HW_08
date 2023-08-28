__all__ = ["writePickleFile"]

def writePickleFile(file: str, data: dict) -> None:
    with open(file, 'wb') as f:
        pickle.dump(data, f)