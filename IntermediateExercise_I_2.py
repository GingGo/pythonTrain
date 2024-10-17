def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2)):
        if n % i == 0:
            return False
    return True


print(isPrime(1))  # returns false
print(isPrime(5))  # returns true
print(isPrime(91))  # returns false
print(isPrime(1000000))  # returns false
print(isPrime(10001))  # returns false
print(isPrime(67))  # returns true
