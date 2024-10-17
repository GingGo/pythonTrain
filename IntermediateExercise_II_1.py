
def factorPrime(n):
    answer = str(n) + " = "
    p = 2
    while p <= n:
        if n % p == 0:
            answer += str(p) + " x "
            n /= p
        else:
            p += 1

    return answer[: len(answer) - 3]


print(factorPrime(120))
