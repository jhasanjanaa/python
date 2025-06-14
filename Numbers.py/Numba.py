# Numba is a Python tool that makes code run much faster 🚀  
# It converts slow Python code into fast machine code using JIT (Just-In-Time) compilation.  

# 🔹 Why use Numba?  
# - Python runs line by line (slow).  
# - Numba compiles the code once and reuses the fast version (fast).  

# 🔹 What is JIT (Just-In-Time) Compilation?  
# - First time: Converts Python code to machine code.  
# - Next times: Uses the fast version (no need to compile again).  
# - Final result: The code runs much faster! 

# 🔹 How to use Numba?  
# - Use @jit before defining a function.  
# - Add `nopython=True` to force full speed optimization.  

# 🔹 Where is Numba useful?  
# - Loops (like for loops).  
# - Mathematical operations (adding, multiplying numbers).  
# - Big data calculations.  

# 🔹 Summary  
# ✅ Numba makes Python code faster   
# ✅ It compiles Python into machine code for better performance.  
# ✅ Just add @jit to speed up functions.  

# Example: Squaring an array (Normal vs. Numba)

import numpy as np  # Import NumPy  
from numba import jit  # Import Numba  

# Normal Python function (slow)
def square_numbers(arr):
    return arr ** 2  

# Numba-optimized function (fast)
@jit(nopython=True)  # Use JIT to speed it up 
def square_numbers_fast(arr):
    return arr ** 2  

# Create an array
arr = np.array([1, 2, 3, 4, 5])  

# Run both functions
print("Without Numba:", square_numbers(arr))  
print("With Numba:", square_numbers_fast(arr))  # Much faster! 