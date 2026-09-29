try :
    num1=int(input(" Enter number : "))
    num2=int(input(" Enter number : "))
    sum = num1+num2

except:
    print("Invalid Number")

else:
    print("Sum : ",sum)

finally:
    print("Done")