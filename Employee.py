class Employee:
    
    #CONSTRUCTOR
    def __init__(self,name,age,Depatment,gmail):
        self.Emp_Name = name
        self.Emp_Age = age
        self.Emp_Department = Depatment
        self.Emp_Gmail = gmail
    
    #FUNCTION  
    def Emp_Details(self):
        print("\n")
        print("*"*40)
        print(f"Employee Name is {self.Emp_Name}")
        print(f"{self.Emp_Name}'s Age is {self.Emp_Age}")
        print(f"{self.Emp_Name}'s Department is {self.Emp_Department}")
        print(f"{self.Emp_Name}'s Gmail is {self.Emp_Gmail}")
        print("*"*40)
        print("\n")
    
    #FUNCTION
    def Change_Department(self,NewDepartment):
        self.Emp_Department = NewDepartment
        print(f"{self.Emp_Name}'s Department is changed to {NewDepartment}")

#CREATING OBJECT OF EMPLOYEE CLASS
emp_1 = Employee("Sohel Shaikh",28,"CSE","Suhailshaikh7866@gmail.com")
emp_2 = Employee("Irfan Shaikh",29,"Technician","irfan78292@gmail.com")
emp_3 = Employee("Arshad Shaikh",29,"Commondo","arshad@gmail.com")

#CALLING Emp_Details() FUNCTION THROUGH OBJECT
emp_1.Emp_Details()
emp_2.Emp_Details()
emp_3.Emp_Details()

#CALLING Change_Department() FUNCTION THROUGH OBJECT
emp_1.Change_Department('Devops')
emp_1.Emp_Details()

