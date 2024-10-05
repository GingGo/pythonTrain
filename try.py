def higherOrder(fn):
    fn()


def smallFunc():
    print("Hello from small function.")


higherOrder(smallFunc)


def square(num):
    return num ** 2


myList = [-10, 3, 9, 8, 10]


print(map(square, myList))

for item in map(square, myList):
    print(item)

print("-----------------------------------")


def even(num):
    if num % 2 == 0:
        return True


evencheckList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in filter(even, evencheckList):
    print(i)
