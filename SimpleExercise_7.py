def summ(inList):
    sum = 0
    for item in inList:
        sum += item

    return sum


print(summ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # returns 55
print(summ([]))  # return 0
print(summ([-10, -20, -30]))  # return -60
