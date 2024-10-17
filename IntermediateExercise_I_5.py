def inversePyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (1 + 2*(i - 1)))


inversePyramid(4)
# *******
#  *****
#   ***
#    *
