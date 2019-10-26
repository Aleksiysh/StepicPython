import itertools


def primes():
    i = 1
    while True:
        i += 1
        count = 0
        for j in range(1, i):
            if i % j == 0:
                count += 1
        if count <= 1:
            yield i


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
