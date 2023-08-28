__all__ = ["verificationStatus"]

def verificationStatus(status: str) -> bool:
    if status.isdigit():
        temp = int(status)
        if temp < 1 or temp > 7:
            print("Введенное значение должно быть в пределах от 1 до 7")
            return False
        else:
            return True
    else:
        print("Введенное значение должно быть числом от 1 до 7")
        return False