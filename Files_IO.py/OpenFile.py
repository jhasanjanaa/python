# We have to open a file before reading and writing.
# f= open("File Name","Mode")   # Agar ham kuch bhi nahi batate toh by default it is set to read.

f = open("C:\\Users\\SANJANA JHA\\Python Programming\\Files_IO.py\\Example.txt","r")          # Double the backslashes because we are working on windows, or else use forward slash.

stored_data = f.readline()
print(stored_data)
print(type(stored_data))
f.close()                    # Khuli rahengi ko koi bhi aake access kar skta hai isliye as a responsible programmer, always close the file.


'''
'r'
open for reading (default)
'w'
open for writing, truncating the file first
'x'
create a new file and open it for writing
'a'
open for writing, appending to the end of the file if it exists
'b'
binary mode
't'
text mode (default)
'+'
open a disk file for updating (reading and writing)
'''


'''
data f.read()
#reads entire file

data f.readline()                        #Iske baad space aa skta hai kyuki hamne line switch ki jiski wajah se by default /n ki jagah hai vo.
#reads one line at a time
# print(line1) ya print(line2) karke ham line ko print kara skte hai apne man pasand wali.
'''

'''
Writing ke liye bas f.write("whatever i wanna write)
'''
# Truncate : Data delete.
# No Truncate : No data delete.

# Refer Q30.