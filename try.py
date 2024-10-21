def safe_dvide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Divide by 0.")
        return None


a = int(input("Enter a:"))
b = int(input("Enter b:"))
print(f"a / b = {safe_dvide(a, b)}")
