def is_prime(x):
    """Return True if x is a prime number, otherwise False."""
    if x < 2:                 # 1
        return False
    for i in range(2, int(x ** 0.5) + 1):   # 2
        if x % i == 0:        # 3
            return False
    return True               # 4


def all_primes_upto(x):
    """Print all prime numbers less than or equal to x, one per line."""
    for n in range(2, x + 1):
        if is_prime(n):        # Reuse the is_prime function
            print(n)


def factorize(x):
    """Print the prime factorization of x, one factor per line."""
    factor = 2              # Start with the smallest prime
    while x > 1:            # Keep going until x is reduced to 1
        if x % factor == 0: # If factor divides x
            print(factor)   # Print the factor
            x = x // factor # Divide x by the factor
        else:
            factor += 1     # Try the next integer
