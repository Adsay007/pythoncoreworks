#ask total bill price and total member count and provide how much each should pay 

bill = int(input("Enter Bill Amount : "))
members = int(input("Enter Total Members Count : "))
pay = bill/members
print(f"Bill Total is {bill} and each should pay {pay} each")
