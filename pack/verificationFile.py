import os

__all__ = ["verificationFile"]
def verificationFile(file: str) -> bool:
    if os.path.exists(file):
        return True
    else:
        return False