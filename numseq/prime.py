def primes(n):
    """Return a list of prime numbers less than n"""
    res = []
    for num in range(2, n):
        if is_prime(num):
            res.append(num)
    return res


def is_prime(m):
    """Determine if m is prime"""
    if m <= 1:
        return False
    if m == 2:
        return True
    for num in range(2, m):
        if m % num == 0:
            return False
    return True