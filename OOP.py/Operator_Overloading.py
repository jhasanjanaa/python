# Operator Overloading (Using operators in a custom way)
# Example: + is used for numbers (5+3=8) and for strings ("hi" + "bye" = "hibye").
# We can also define how operators work for our own objects.

# Example in Python

class Box:
    def __init__(self, weight):
        self.weight = weight

    def __add__(self, other):  # Overloading +
        return Box(self.weight + other.weight)

box1 = Box(10)
box2 = Box(20)
box3 = box1 + box2  # Calls __add__()

print(box3.weight)  # Output: 30
# ✅ We customized the + operator for our class!

