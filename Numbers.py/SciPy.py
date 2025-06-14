# =====================================
# 🔬 SciPy – Advanced Math in Python
# =====================================

# 📌 What is SciPy?
# SciPy is a library for advanced math, science, and engineering.
# It is built on NumPy and provides tools for:
# ✅ Optimization
# ✅ Integration
# ✅ Statistics
# ✅ Linear Algebra
# ✅ Signal Processing

# =====================================
# 📌 INSTALLING SCIPY
# =====================================
# If SciPy is not installed, run:
# pip install scipy

# =====================================
# 📌 IMPORTING SCIPY MODULES
# =====================================
import numpy as np  # SciPy is built on NumPy
from scipy import optimize, integrate, stats, linalg  # Import useful SciPy modules

# =====================================
# 📌 OPTIMIZATION (Finding Min/Max)
# =====================================
# Find the minimum of f(x) = x² + 2x + 1
def f(x):
    return x**2 + 2*x + 1

result = optimize.minimize(f, x0=0)  # Start from x = 0
print("Minimum at x =", result.x)

# =====================================
# 📌 INTEGRATION (Solving Integrals)
# =====================================
# Compute the integral of f(x) = x² from 0 to 3
def f(x):
    return x**2

integral, error = integrate.quad(f, 0, 3)
print("Integral result:", integral)

# =====================================
# 📌 STATISTICS (Mean, Median, Mode)
# =====================================
data = [1, 2, 2, 3, 4, 4, 4, 5]

mean = np.mean(data)  # Mean (average)
median = np.median(data)  # Median (middle value)
mode = stats.mode(data)  # Mode (most frequent)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode.mode[0])

# =====================================
# 📌 LINEAR ALGEBRA (Solving Equations)
# =====================================
# Solve: 2x + 3y = 5 and 4x + 6y = 10
A = np.array([[2, 3], [4, 6]])  # Coefficients
B = np.array([5, 10])  # Constants

solution = linalg.solve(A, B)
print("Solution:", solution)

# =====================================
# 📌 SUMMARY
# =====================================
# ✅ SciPy is used for advanced math calculations
# ✅ It extends NumPy with optimization, integration, stats, etc.
# ✅ Fast and efficient 🚀

