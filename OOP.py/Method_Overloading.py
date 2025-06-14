# Method Overloading (Same function, different number of arguments)
# Python doesn't support method overloading directly, but we can do it using default arguments!

# Example in Python

class Math:
    def add(self, a, b, c=0):  # c is optional
        return a + b + c

obj = Math()
print(obj.add(2, 3))     # Calls add(a, b)
print(obj.add(2, 3, 4))  # Calls add(a, b, c)
# ✅ Same function works differently based on input!

