def findSmallCount(intList, n):
    count = 0
    for item in intList:
        if item < n:
            count += 1

    return count


print(findSmallCount([1, 2, 3], 2))  # returns 1
print(findSmallCount([1, 2, 3, 4, 5], 0))  # returns 0
