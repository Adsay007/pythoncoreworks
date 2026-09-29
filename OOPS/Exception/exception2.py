try :
    num1=int(input(" Enter number : "))
    num2=int(input(" Enter number : "))
    d = num1/num2
    print("Result" ,d)

except ZeroDivisionError:
    print("Zero Division Error")

except ValueError:
    print("Value Error")

except:
    print("Error")

