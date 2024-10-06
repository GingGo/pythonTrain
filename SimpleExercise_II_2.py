def stars2(n):
    star = "*"
    for i in range(1, n+1):
        print(star*i)
    for j in range(n-1, 0, -1):
        print(star*j)


stars2(1)
print("---------------------")
stars2(2)
print("---------------------")
stars2(3)
print("---------------------")
stars2(4)
