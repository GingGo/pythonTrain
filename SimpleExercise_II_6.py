def findMin(inList):
    min = 0
    if inList == []:
        return None
    else:
        min = inList[0]
        for item in inList:
            if item < min:
                min = item
        return min


print(findMin([1, 2, 5, 6, 99, 4, 5]))  # returns 1
print(findMin([]))  # returns undefined
print(findMin([1, 6, 0, 33, 44, 88, -10]))  # returns -10
