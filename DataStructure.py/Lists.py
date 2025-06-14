# LISTS : A built in data type that stores set of values. It can store elements of different types (int, float, str etc.).
# Either we write all the values differently or else all at the same time, saving a lot of time.

A = [ 97.5, 99.0, 98.7, 94.3]
print(A)
print(type(A))

# Now we can even access the list elements. But remember the fwd counting always starts with 0.

print(A[0])
print(A[3])

# We can store values here.

B = ["Jake", 100, "Excellent"]
B[2] = "Best"
print(B)

# For finding length:

print(len(B))

# List slicing is also possible. But ENDING INDEX IS NOT INCLUDED.

print(B[2:4])