'''
Create a new file "practice.txt" using python. Add the following data in it:
Hi everyone
we are learning File I/O
using Java.
I like programming in Java.
'''

# Write data to the file
with open("practice.txt", "w") as f:
    f.write("Hi everyone\n")
    f.write("We are learning File I/O\n")
    f.write("Using Java\n")
    f.write("I like programming in Java\n")

# Read data from the file
with open("practice.txt", "r") as f:
    content = f.read()
    print(content)
