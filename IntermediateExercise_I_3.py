# def palindrome(string):
#     strRev = ""
#     for i in range(len(string)-1, -1, -1):
#         strRev += string[i]
#     return string == strRev


def palindrome(string):
    return string == string[::-1]


print(palindrome("bearaeb"))  # true
print(palindrome("Whatever revetahW"))  # true
print(palindrome("Aloha, how are you today?"))  # false
