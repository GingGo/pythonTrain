def intersection(List_a, List_b):
    ret = []
    for item in List_a:
        if List_b.count(item) > 0:
            ret.append(item)
    return ret


# returns [3, 4]
print(intersection([1, 3, 4, 6, 10], [5, 11, 4, 3, 100, 144, 0]))
