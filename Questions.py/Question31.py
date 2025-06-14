'''
WAF that replace occurances of 'Java' with 'Python'. First make te file.
Hi everyone
we are learning File I/O
using Java.
I like programming in Java.
'''
with open("file1.txt", "w") as f:
    f.write("Hi everyone\n")
    f.write("we are learning File I/O\n")
    f.write("using Java\n")
    f.write("I like programming in Java.")
    
with open("file1.txt","r+") as f:
    content = f.read()
    print(content)
    new = content.replace("Java","Python")       # Replace karn eke baad content ko likhwana bji toh padega.
    f.write(new)

with open("file1.txt","r") as f:
    print(f.read())

# Very Very Good


