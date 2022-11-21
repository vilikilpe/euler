"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
by only moving to the right and down, is indicated in bold red and is equal to 2427.

Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt
(right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""

import csv
import time


def minimal_path(matrix: list) -> int:
    """Find the minimal path from top left to the bottom right of the matrix.
    This is done by creating a sum matrix and returning the bottom right value

    Args:
        matrix (list): matrix (list of lists)

    Returns:
        int: minimal sum
    """
    # Size of the matrix
    y = len(matrix)
    x = len(matrix[0])

    # Loop every item in the matrix
    for y_idx in range(0, y):
        for x_idx in range(0, x):
            # Convert value to integer
            matrix[y_idx][x_idx] = int(matrix[y_idx][x_idx])

            if y_idx == 0 and x_idx == 0:
                continue  # no need for actions, we are in the upper left corner
            # When we are in the 1. row or 1. column the logic is same: sum current value and value before current one
            elif x_idx == 0:
                matrix[y_idx][x_idx] = matrix[y_idx - 1][x_idx] + matrix[y_idx][x_idx]
            elif y_idx == 0:
                matrix[y_idx][x_idx] = matrix[y_idx][x_idx - 1] + matrix[y_idx][x_idx]
            # Because we can only move right or down the sum value in the middle of the matrix is minimum of these
            # two values: value on top of the current one or value on the left of the current one
            else:
                matrix[y_idx][x_idx] = min(matrix[y_idx][x_idx - 1], matrix[y_idx - 1][x_idx]) + matrix[y_idx][x_idx]
    return matrix[y_idx][x_idx]


if __name__ == "__main__":

    start_time = time.perf_counter()

    B = []
    with open("matrix.txt", "r") as file:
        csvreader = csv.reader(file, delimiter=",")
        for row in csvreader:
            B.append(row)

    print("Solving projecteuler problem #081, Python solution")
    print(f"Minimal path sum of the given matrix: {minimal_path(B)}")
    print(f"Execution time: {time.perf_counter()-start_time}")
