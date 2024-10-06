def findSmallerTotal(inList, n):
    sum = 0
    for item in inList:
        if item < n:
            sum += item

    return sum


print(findSmallerTotal([1, 2, 3], 3))  # returns 3
print(findSmallerTotal([1, 2, 3], 1))  # returns 0
print(findSmallerTotal([3, 2, 5, 8, 7], 999))  # returns 25
print(findSmallerTotal([3, 2, 5, 8, 7], 0))  # returns 0
