# def swap(string):
#     swapString = ""
#     for chIndex in range(len(string)):
#         if string[chIndex] == str.upper(string[chIndex]):
#             swapString += str.lower(string[chIndex])
#         else:
#             swapString += str.upper(string[chIndex])

#     return swapString

def swap(string):
    swapString = ""
    for ch in string:
        if ch == ch.upper():
            swapString += str.lower(ch)
        else:
            swapString += str.upper(ch)

    return swapString


print(swap("Aloha"))  # returns "aLOHA"
print(swap("Love you."))  # returns "lOVE YOU."
