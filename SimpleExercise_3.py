def position(string):
    for i in range(len(string)):
        if string[i] == str.upper(string)[i]:
            return string[i], i

    return -1


print(position("abcd"))  # returns -1
print(position("AbcD"))  # returns ('A', 0)
print(position("abCD"))  # returns ('C', 2)
