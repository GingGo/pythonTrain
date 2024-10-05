for i in "How are you":
    pass

print("after pass")


for i in "12345678":
    if int(i) > 5:
        break
    else:
        print(i)

print("-------------------------------")
for i in "ABCDEFG":
    if i == "D":
        continue
    print(i)
