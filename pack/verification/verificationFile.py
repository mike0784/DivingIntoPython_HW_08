import os

def verificationFile(file: str) -> bool:
    if os.path.exists(file):
        return True
    else:
        return False