__all__ = ["readPickleFile"]

def readPickleFile(file: str) -> dict:
    with open(file, "rb") as f:
        result = pickle.load(f)
    return result