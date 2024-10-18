import pickle

# x = 10
# y = [1, 2, 3, 4]

# with open("pickle_file", mode="wb") as p_file:
#     pickle.dump(x, p_file)
#     pickle.dump(y, p_file)

with open("pickle_file", mode="rb") as p_file:
    print(pickle.load(p_file))
    print(pickle.load(p_file))
