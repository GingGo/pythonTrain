friends = ["Terry", "Mike", "Nelson", "Greg"]
friends.insert(2, "Eric")
print(friends)


friends.remove("Nelson")
print(friends)

friendsTest = friends
print(friendsTest)
# friendsTest.clear()
# print(friendsTest)
friendsTest.sort()
print(friendsTest)

nums = [6, 4, -1, 0, -5]
nums.sort()
print(nums)

nums.reverse()
print(nums)

nums.append(10)
print(nums)
nums.pop()
print(nums)
