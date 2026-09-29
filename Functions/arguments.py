# sum of different paramenters using *args

def sum(*args):
    sum1=0
    for i in args:
        sum1 += i
    print(sum1)

sum(4,5,6)