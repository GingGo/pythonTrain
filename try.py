a = ([1, 2, 3], "Terry")
a[0][1] = 100
print(a)

# if an element in a tuple is mutable, then we can just
# select the element, and then change it.

# If we want to use a tuple as a dictionary key, then
# all elements in the tuple has to be immutable.
