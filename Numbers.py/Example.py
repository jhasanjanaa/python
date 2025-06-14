# Write a Python function that calculates the sum of squares of the first n natural numbers. Optimize it using Numba.
import numba
from numba import jit

@jit(nopython=True)
def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

print(sum_of_squares(10))  # Output: 385

import time

n = 10**6  # Large input

# Without Numba
start = time.time()
sum_of_squares(n)  # Normal Python version
print("Without Numba:", time.time() - start)

# With Numba
start = time.time()
sum_of_squares(n)  # JIT compiled version
print("With Numba:", time.time() - start)
