import math


def sieve_of_eratosthenes(limit):
    arr = [True] * (limit + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if arr[i]:
            for j in range(i * i, limit + 1, i):
                arr[j] = False

    return arr


limit = 123456 * 2
prime_flags = sieve_of_eratosthenes(limit)

while True:
    x = int(input())
    if x == 0:
        break

    count = sum(1 for i in range(x + 1, 2 * x + 1) if prime_flags[i])
    print(count)