
try:
    num = int(input("Enter a number :"))
    if (num<=0):
        raise ValueError("Number Must be Positive")
    else:
        print(num)
except ValueError as e:
    print (e)


#To define an exception (to create our own exception)
class invalidnumbererror(Exception):
    pass

try:
    num = int(input("Enter another number :"))
    if (num<=0):
        raise invalidnumbererror("Number Must be Positive")
    else:
        print(num)
except invalidnumbererror as e:
    print (e)