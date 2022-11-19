import pytest

from p81_euler import minimal_path


def test_minimal_path():
    A = [
        [131, 673, 234, 103, 18],
        [201, 96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524, 37, 331],
    ]
    B = [[131, 673, 21, 103, 18]]

    assert minimal_path(A) == 2427
    assert minimal_path(B) == 946
