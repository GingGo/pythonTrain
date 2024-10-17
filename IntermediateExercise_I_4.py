def pyramid(n):
    for i in range(n):
        print(" "*(n-i-1)+"*"*(1+2*i))


pyramid(1)
# *
pyramid(2)
#  *
# ***
pyramid(4)
#    *
#   ***
#  *****
# *******
