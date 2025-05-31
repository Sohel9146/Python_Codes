class Parents:

    def __init__(self,name,middlename,surname):
        self.name = name
        self.middlename = middlename
        self.surname = surname

    def show_details(self):
        print(f"{self.name} and {self.surname}")

        
class child(Parents):
    
    def show_middlename(self):
        print(f"{self.name} {self.middlename} {self.surname}")




p = Parents("Altaf","Allahbaksh","Khan")
s = child("Sohel","Altaf","Shaikh")

s.show_details()
s.show_middlename()