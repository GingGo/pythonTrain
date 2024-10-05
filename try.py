for counter, c in enumerate("How are you today?"):
    if counter < 10:
        print(c)


x = [1, 2, 3]
y = ["A", "B", "C"]
z = ["A", "B", "C", "D"]

for t in zip(x, y, z):
    print(t)
