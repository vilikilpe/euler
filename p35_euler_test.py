import pytest

from p35_euler import circular_primes, permutations, prime_number, primes_v1, primes_v2


@pytest.mark.parametrize("test_input, expected", [(197, [719, 971, 197])])
def test_permutations(test_input, expected):
    assert permutations(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [(100, 13), (1000, 25), (10000, 33)])
def test_circular_primes(test_input, expected):
    assert circular_primes(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [(10, [2, 3, 5, 7]), (4, [2, 3])])
def test_primes(test_input, expected):
    assert primes_v1(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [(10, [2, 3, 5, 7]), (4, [2, 3])])
def test_primes(test_input, expected):
    assert primes_v2(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [(3, True), (100, False), (29, True)])
def test_prime_number(test_input, expected):
    assert prime_number(test_input) == expected
