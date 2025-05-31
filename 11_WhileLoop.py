# 1 - WHILE LOOP Example

Users = []

name = ""

# Active = True

while True:
    print("\n")
    print("--"*25)
    name = input("Enter Your Name to Add in List or type 'EXIT' : ")

    if name in Users:
        print("User Already Exist..")
    
    elif name.upper() == "EXIT":
        print("Exiting From The Loop..")
        # Active = False
        break
    
    elif name.strip() == "":
        print("Enter Proper Name..")
   
    else:
        Users.append(name)
        print(f"{name} Added Sueccessfully in List..")
        print("\n")
        print(f"Updated User List : {Users}")
        print("--"*25)
        


