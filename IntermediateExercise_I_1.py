def mySort(inList):
    ischange = False
    for i in range(len(inList) - 1):
        ischange = False
        for j in range(len(inList) - 1 - i):
            if inList[j] > inList[j+1]:
                inList[j], inList[j+1] = inList[j+1], inList[j]
                ischange = True
        if not ischange:
            break
    return inList


print(mySort([17, 0, -3, 2, 1, 0.5]))  # returns [-3, 0, 0.5, 1, 2, 17]
