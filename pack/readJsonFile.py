import json
import pack.verification.verificationFile as ver

__all__ = ["readJsonFile"]

def readJsonFile(file: str) -> dict:
    if ver.verificationFile(file):
        with open(file, "r", encoding="utf8") as f:
            result = json.load(f)
        return result
    else:
        return None