class Shop:
    def __init__ (self):
        self.category_name= input("Enter Category Name. : ")
    def show_category(self):
        print(f" Category : {self.category_name} ")

class Product(Shop):
    def __init__(self):
        super().__init__()
        self.product_name = input(" Enter Product Name : ")
        self.price = int(input(" Enter Price : "))
        self.quantity = int(input(" Enter Quantity : "))

    def total_price(self):
        print(f"Total Product Price : {self.price*self.quantity}")

s = Product()
s.show_category()
s.total_price()

