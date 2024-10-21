def divide(a, b):
    if type(a) != int or type(b) != int:
        raise ValueError("Not vaild type given!")

    if b == 0:
        raise ZeroDivisionError("Second argument can't be 0")

    return a / b


try:
    print(divide(10, "hello"))

except Exception as e:
    print(e)
