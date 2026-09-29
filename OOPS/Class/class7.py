class Account:
    def __init__(self):
        self.accno = int(input("Enter Account No : "))
        self.accname = input("Enter Account Name : ")
        self.accbalance = int(input("Enter Account Balance : "))

    def accountdetails(self):
         print("\n")
         print(f"Account Number : {self.accno}")
         print(f"Account Name : {self.accname}")
         print(f"Account Balance : {self.accbalance}")
         print("\n")

    def withdraw(self):
        print(f"\nCurrent Balance : {self.accbalance}")
        a = int(input("Enter Amount to withdraw : "))

        if (a > self.accbalance):
              print("Insufficient Fund")
        else : 
            self.accbalance -= a

    def deposit(self):
        print(f"\nCurrent Balance : {self.accbalance}")
        b = int(input("Enter Amount to deposit : "))
        self.accbalance += b

    def showbalance(self):
        print(f"\nAccount Name : {self.accname}")
        print(f"Balance : {self.accbalance}")


l = []

while(1):
    # Main Menu
    print("\nMenu")
    print("1.Create New Account")
    print("2.Show all accounts")
    print("3.Withdraw")
    print("4.Deposit")
    print("5.Show Balance ")
    print("6.Exit\n")

    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        acc1 = Account()
        l.append(acc1)
        print("\n--- Account Created ---")
        acc1.accountdetails()

    elif ch == 2:
        for i in l:
            i.accountdetails()
            
    elif ch == 3:
        print("\nAll Accounts\n")
        for acc in l:
            print(f"Acct No: {acc.accno} | Name: {acc.accname}")
        print("\n")
        
        number = int(input("Enter account number : "))
        for i in l:
            if (i.accno == number):
                i.withdraw()
                i.showbalance()
                break        
        else:
             print("Account Doesn't exist")

    elif ch == 4:
        number = int(input("Enter account number : "))
        for i in l:
            if (i.accno == number):
                i.deposit()
                i.showbalance()
                break        
        else:
             print("Account Doesn't exist")

    elif ch == 5:
        number = int(input("Enter account number : "))
        for i in l:
            if (i.accno == number):
                i.showbalance()
                break        
        else:
             print("Account Doesn't exist")

    else:
        exit()