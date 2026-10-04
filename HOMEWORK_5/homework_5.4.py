class InvalidTestStatusError(Exception):
    pass

def check_status(status):
    if status == "PASS":
        return True
    if status == "FAIL":
        return True
    if status == "SKIP":
        return True
    else:
        raise InvalidTestStatusError(f"Некорректный статус теста: {status}")

check_status("PASS")
check_status("FAIL")
check_status("SKIP")
try:
    check_status("ERROR")
except InvalidTestStatusError as e:
    print(e)