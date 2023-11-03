import math


def func_get_prime(n):
    return filter(lambda x: not[x % i for i in range(2, int(math.sqrt(x)) + 1)if x % i == 0], range(2, n+1))


def is_odd(n):
    return n % 2 == 1


print(list(func_get_prime(100)))
newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(newlist))
