x = [1, 2, 3, 4]
y = {item: item ** 2 for item in x}
print(y)

z_set = {item ** 2 for item in x}
print(z_set)

x_sqr_gener = (item ** 2 for item in x)
for item in x_sqr_gener:
    print(item)
