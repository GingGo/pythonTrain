def swap(string):
    swapString = ""
    for chIndex in range(len(string)):
        if string[chIndex] == str.upper(string[chIndex]):
            swapString += str.lower(string[chIndex])
        else:
            swapString += str.upper(string[chIndex])

    return swapString


print(swap("Aloha"))  # returns "aLOHA"
print(swap("Love you."))  # returns "lOVE YOU."