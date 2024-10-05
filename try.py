def sum(*args):
    ret = 0
    print(args)
    print(type(args))
    for i in range(len(args)):
        ret += args[i]
    return ret


print(sum(1, 2, 3, 4, 5, 6, 7, 8))


def myFunc(**kwargs):
    print(kwargs)
    print(type(kwargs))


myFunc(name="Terry", age=25, addr="Taipei")


def myFunc2(*args, **kwargs):
    print("I would like to eat {} {}".format(args[1], kwargs["food"]))


myFunc2(1, 5, 10, "Hello", name="Terry", food="eggs")
