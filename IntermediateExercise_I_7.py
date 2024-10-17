def spyGame(inList):
    stringRet = [0, 0, 7]
    pointfor_ret = 0
    pointforinList = 0
    while pointforinList < len(inList):
        if inList[pointforinList] == stringRet[pointfor_ret]:
            pointfor_ret += 1
            if (pointfor_ret == 2):
                return True
        pointforinList += 1
    return False


print(spyGame([1, 2, 4, 0, 3, 0, 7]))  # True
print(spyGame([1, 2, 5, 0, 3, 1, 7]))  # False

# look answer
