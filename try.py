getStr = input("Enter input:")

match getStr:
    case "a" | "t":
        print("Input a or t")
    case "b":
        print("Input b")
    case _:
        print("Other Input")
