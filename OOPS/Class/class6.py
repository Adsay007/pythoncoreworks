class Circle:
    def __init__(self):
        self.radius=int(input("Enter Radius : "))
        self.pi=3.14
    def getarea(self):
        print(f"Area : {self.pi*(self.radius ** 2)}")

    def getperimeter(self):
            print(f"Perimeter : {2 * self.pi * self.radius}")

c=Circle()
c.getarea()
c.getperimeter()