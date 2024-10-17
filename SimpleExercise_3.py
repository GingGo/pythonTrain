# def position(string):
#     for i in range(len(string)):
#         if string[i] == str.upper(string)[i]:
#             return string[i], i

#     return -1

def position(string):
    for num, s in enumerate(string):
        if s == s.upper():
            return (s, num)
    return -1


print(position("abcd"))  # returns -1
print(position("AbcD"))  # returns ('A', 0)
print(position("abCD"))  # returns ('C', 2)
