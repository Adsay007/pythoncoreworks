class Hospital:
    def __init__(self):
        self.hos_name=input("Enter Hospital Name : ")
        self.location=input("Enter Location : ")
        self.phone=int(input("Enter Phone Number : "))

    def display_hospital(self):
        print(f"Hospital Name : {self.hos_name} , Location : {self.location}, Phone : {self.phone}")
    

class Department:
    def __init__(self):
        self.dept_name = input("Enter Dept Name : ")
        self.doctor_name = input("Enter Doctor Name : ")

    def display_department(self):
        print(f"Dept Name : {self.dept_name}, Doctor Name : {self.doctor_name}")

class Patient(Hospital,Department):
    def __init__(self):
        Hospital.__init__(self)
        Department.__init__(self)

        self.patient_name=input("Enter Patient Name : ")
        self.age=int(input("Enter Age : "))
        self.gender=input("Enter Gender : ")
        self.admission_date=input("Enter Admission Date : ")
        self.bedno=int(input("Enter Bed No : "))
        self.discharge_date = ""
        if (self.discharge_date == ""):
        
            print("Not Yet Discarged")
        else:
            print (self.discharge_date)

    def full_summary(self):
            Hospital.display_hospital(self)
            self.display_hospital
            Department.display_department(self)
            self.display_department
            print(self.patient_name)
            print(self.age)
            print(self.gender)
            print(self.admission_date)
            print(self.bedno)
            print(self.discharge_date)
            
    
    def set_discharge(self):
            Hospital.display_hospital(self)
            Department.display_department(self)

            self.discharge_date=input("Enter Discharge Date : ")


c=Patient()
c.set_discharge()
c.full_summary()