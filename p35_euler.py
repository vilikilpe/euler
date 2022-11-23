"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million? Correct answer: 55
"""

import math as m
import time


def prime_number(num: int) -> bool:
    """Check if number is prime number

    Args:
        num (int): any possible integer

    Returns:
        bool: return True if number is prime number
    """
    for i in range(2, m.ceil(m.sqrt(num)) + 1):  # reduce redundant checks with sqrt
        if num % i == 0 and num != 2:
            return False
    return True


def primes_v1(n: int) -> list:
    """Finds all primes under n, version 1

    Args:
        n (int): range upper limit

    Returns:
        list: list of primes
    """
    primes = []
    for num in range(2, n + 1):
        if prime_number(num):
            primes.append(num)
    return [2] + primes


def primes_v2(n: int) -> list:
    """Finds all primes under n, version 2. Reduce even more redundant checks.

    Args:
        n (int): range upper limit

    Returns:
        list: list of primes
    """
    sieve = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i :: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def permutations(num: int) -> list:
    """Find cyclic permutations of given integer and return those in a list

    Args:
        num (int): any possible number

    Returns:
        list: list of integers
    """

    # number of digis in a given number
    nbr = m.floor(m.log10(num) + 1)

    perm = []
    while True:
        rem = num % 10
        div = m.floor(num / 10)
        num = (m.pow(10, nbr - 1)) * rem + div
        perm.append(int(num))
        if len(perm) == nbr:
            return perm


def circular_primes(n: int) -> int:
    """How many circular primes are there below n

    Args:
        n (int): limitting number

    Returns:
        int: number of circlar primes
    """
    # Find all primes below number n
    primes = primes_v2(n)
    i = 0
    # Loop all primes and check if all circular permutations are prime numbers
    for prime in primes:
        all_primes = True
        for number in permutations(prime):
            if prime_number(number) == False:
                all_primes = False
                break
        # If all circular permutations are prime numbers update i
        if all_primes:
            i += 1
    return i


if __name__ == "__main__":

    start_time = time.perf_counter()
    n = 1000000
    print("Solving projecteuler problem #035, Python solution")
    print(f"There are {circular_primes(n)} circular primes below {n}")
    print(f"Execution time: {time.perf_counter()-start_time}")
