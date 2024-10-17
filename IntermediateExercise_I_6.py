def has_33(inList):
    for index in range(len(inList) - 1):
        if inList[index] == 3 and inList[index + 1] == 3:
            return True
    return False


print(has_33([1, 5, 7, 3, 3]))  # True
print(has_33([]))  # False
print(has_33([4, 3, 2, 1, 0]))  # False
