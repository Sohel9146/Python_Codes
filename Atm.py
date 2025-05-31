from playsound3 import playsound 
# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty('voices') 
# engine.setProperty('voice', voices[1].id)

class Atm:

    #Constructor
    def __init__(self,Name,User_data):
        self.User_Name = Name
        self.User_Data = User_data

    #Check Balance Function
    def check_balance(self):
        # engine.say("You Selected Check Balance Option")
        # engine.runAndWait()
        Balance = self.User_Data[self.User_Name]["Balance"]
        print(f"\n{self.User_Name}'s Account Balance is Rs - {Balance}")

    #Deposit Function
    def deposit(self,amount):
        # engine.say("You Selected Deposit Option")
        # engine.runAndWait()
        if amount > 0 :
            self.User_Data[self.User_Name]["Balance"] += amount
            playsound("deposit.wav")
            print(f"\n Rs - {amount} Deposited Successfully..")
        else:
            print("\n Invalid Deposit Amount..")    

    #Withdraw Function
    def withdraw(self,amount):
        # engine.say("You Selected Withdraw Option")
        # engine.runAndWait()
        if amount > 0 and amount <= self.User_Data[self.User_Name]["Balance"] : 
            self.User_Data[self.User_Name]["Balance"] -= amount
            playsound("withdraw.mp3")
            print(f"\n Rs - {amount} Withdrawn Successfully")
        else:
            print("\n Insufficient Balance or Invalid Amount..")

    #Change Pin
    def changepin(self):
        # engine.say("You Selected Change Pin Option")
        # engine.runAndWait()
        old_pin = input("\n Enter Your Old Pin : ")
        if old_pin == self.User_Data[self.User_Name]["pin"]:
            new_pin = input("\n Enter New Pin : ")
            confirm_pin = input("\n Confirm Your New Pin : ")
            if new_pin == confirm_pin:
                self.User_Data[self.User_Name]["pin"] = new_pin
                print("\n Pin Changed Successfully..")
            else:
                print("\n New Pin Do Not Match..")
        else:
            print("\n Incorrect Old Pin..")

    #ATM Menu
    def menu(self):
        while True:
            # engine.say("Choose Option From Below")
            # engine.runAndWait()
            print("\n ----------- ATM Menu -----------")
            print("1 - Check Balance")
            print("2 - Deposit Money")
            print("3 - Withdraw Money")
            print("4 - Change Pin")
            print("5 - Exit")

            choice = input("\nEnter your Choice from (1-4) : ")

            if choice == "1":
                self.check_balance()
            
            elif choice == "2":
                amount = float(input("Enter Amount to Deposit : "))
                self.deposit(amount)
            
            elif choice == "3":
                amount = float(input("Enter Amount To Withdraw : "))
                self.withdraw(amount)
            
            elif choice == "4":
                self.changepin()

            elif choice == "5":
                # engine.say("Thank You Using Our ATM. VISIT AGAIN")
                # engine.runAndWait()
                print(f"\n Thank You, {self.User_Name} , For Using the ATM.. ")
                break

            else:
                print("\n Invalid Choice, Please Try Again..")




# Registered_Name = "Sohel"
# Registered_Pin = "1234"

users = {
        "Sohel" : {
                    "pin" : "1234",
                    "Balance" : 10000
                  },
        "Irfan" : {
                    "pin" : "4321",
                    "Balance" : 15000
                  },
        "Arshad" : {
                    "pin" : "7866",
                    "Balance" : 25000
                   } 
                
        }

attempts = 3

while attempts > 0:
    Name_Input = input("Enter Your Registered Name : ")
    Pin_Input = input("Enter Your 4-digit Pin : ")

    if Name_Input in users and users[Name_Input]["pin"] == Pin_Input:
        print("\n Login Successfully..")
        atm = Atm(Name_Input,users)
        # Start the ATM Menu
        atm.menu()
        break
    
    else:
        attempts -= 1
        print(f"\n Incorrect Name or Pin, Attempt left - {attempts}")

    if attempts == 0:
        print("\n Too Many Failed Attempts, Access Denied.")