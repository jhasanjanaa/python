'''
Break : Used to terminate the loop when encountered.
# Break karke loop se bahar le aata hai and bahar wali statement ko print kara deta hai.

'''

# Write a Python program that asks the user to enter numbers continuously.
# If the user enters 0, the program should stop taking inputs and print "Loop exited!" using the break statement.

while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        print("Loop exited!")
        break
    else:
        print("You entered:", number)
