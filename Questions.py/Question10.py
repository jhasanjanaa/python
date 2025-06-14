'''
You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
"python", "java", "C++", "python", "javascript",
"java", "python", "java", "C++", "C"
'''

list = ("python", "java", "C++", "python", "javascript",
"java", "python", "java", "C++", "C")


'''
x = list.count("python")
y = list.count("java")
z = list.count("C++")
q = list.count("C")

print(x)
print(y)
print(z)
print(q)

Total_Student = print(x+y+z+q)
'''


subjects = ("python", "java", "C++", "python", "javascript",
            "java", "python", "java", "C++", "C")

unique_subjects = set(subjects)  # Convert to set to get unique subjects
classrooms_needed = len(unique_subjects)

print("Classrooms needed:", classrooms_needed)
