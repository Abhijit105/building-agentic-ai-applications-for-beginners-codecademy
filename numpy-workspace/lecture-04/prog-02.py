# Given a positive odd number n(> 2), create a numpy array of size nxn with all zeros and ones such that the ones make a shape of a plus(+). If n is even, then the function should return "Please enter an odd number greater than 2"

import numpy as np

def make_plus(n):
    if n <= 2 or n % 2 == 0:
        print("Please enter an odd number greater than 2")
        return

    # make a grid of all zeros
    a = np.zeros((n, n), dtype="int")
    print(a)
    print(type(a))

    # make the middle row as all 1s
    middle_row = len(a) // 2
    a[middle_row, :] = 1
    # for i in range(n):
        # a[middle_row, i] = 1

    print(a)

    # make the middle column as all 1s
    middle_col = n // 2
    a[:, middle_col] = 1
    # for i in range(n):
        # a[i, middle_col] = 1

    print(a)

size = int(input("Enter the size of the grid:\t"))
make_plus(size)
