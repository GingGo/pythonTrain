def findAllSmall(inList, n):
    ret = []
    for item in inList:
        if item < n:
            ret.append(item)
    return ret


print(findAllSmall([1, 2, 3], 10))  # returns [1, 2, 3]
print(findAllSmall([1, 2, 3], 2))  # returns [1]
print(findAllSmall([1, 3, 5, 4, 2], 4))  # returns [1, 3, 2]
