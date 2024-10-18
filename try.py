# user_input = input("How old are you?")
# print("---------------------------------")
# print(user_input)
# print(type(user_input))

import random

sercret_num = random.randint(1, 100)
v_min = 1
v_max = 100
while True:
    user_input = input(f"key a num between {v_min} and {v_max}:")
    if int(user_input) < v_min or int(user_input) > v_max:
        print("input fail!")
        continue

    if int(user_input) == sercret_num:
        print(f"right {sercret_num}")
        break

    if int(user_input) < sercret_num:
        v_min = int(user_input)

    if int(user_input) > sercret_num:
        v_max = int(user_input)
