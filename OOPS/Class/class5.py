class Book:
    def __init__(self):
        self.title = input("Enter Title : ")
        self.author = input("Enter Author Name : ")
        self.price = int(input("Enter Price : "))
        self.pages = int(input("Enter Page Count : "))
        self.language = input("Enter Language : ")

    def gettitle(self):
        print(f"Title : {self.title}")
    def getauthor(self):
            print(f"Author : {self.author}")
    def getprice(self):
            print(f"Price : {self.price}")

    def settitle(self):
          self.title=input("Enter New Title : ")
          self.gettitle()
    def setauthor(self):
              self.author=input("Enter New Author Name : ")
              self.getauthor()
    def setprice(self):
              self.price=input("Enter New Price : ")
              self.getprice()
    def updated(self):
           print("Updated Info ")
           print(f"New Title : {self.title}")
           print(f"New Price : {self.price}")
           print(f"New Author : {self.author}")


b1=Book()
b1.gettitle()
b1.getauthor()
b1.getprice()

b1.setauthor()
b1.settitle()
b1.setprice()

b1.updated()