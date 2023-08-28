__all__ = ["verificationId"]

def verificationId(id: str, a: dict) -> bool:
    for item in a:
        print(f'item={a[item]}')
        if id in a[item].keys():
            return False
    return True