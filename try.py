a = 5


def f1():
    x = 2
    y = 3
    print(x, y, a)


f1()


def change(num):
    global a
    a = num


change(25)
print(a)
