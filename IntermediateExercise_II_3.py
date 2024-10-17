
resutl = []


def flatten(lst):
    for i in lst:
        if type(i) == type([]):
            flatten(i)
        else:
            resutl.append(i)
    return resutl


print(flatten([1, [[], 2, [0, [1]], [3]], [1, 3, [3], [4, [1]], [2]]]))
