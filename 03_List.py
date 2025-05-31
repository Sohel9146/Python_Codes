#ORDERED SEQUENCE OF DIFFERENT TYPE OF VALUES

Users = ["Sohel","Irfan","Arshad","Wasim"]

#Getting Values From List

# print(Users[0])
# print(Users[1])
# print(Users[2])
# print(Users[3])

print("\n")
print("~~~~~~~~~~~~~~~~~ LIST OPERATIONS ~~~~~~~~~~~~~~~~")
print("\n")

print(f"Orignal List : {Users}")

#Adding Item To List
print("--"*25)
print("Adding Item to List : ")
Users.append("Shuaib")
print(Users)
print("--"*25)

#Deleting Values From List
print("--"*25)
print("Deleting Values From List : ")
Users.remove("Shuaib")
print(Users)
print("--"*25)

#Modifying List
print("--"*25)
print("Modifying List : ")
Users[1] = "Shoeb"
print(Users)
print("--"*25)

#Adding Item To a List At Given Position
print("--"*25)
print("Adding Item in List at Given Position : ")
Users.insert(1,"Irfan")
print(Users)
print("--"*25)

#Getting Length of List
print("--"*25)
print("Length of The List : ")
print(len(Users))
print("--"*25)

print("\n")
print("~~~~~~~~~~~~~~~~~~ LIST SORTING ~~~~~~~~~~~~~~~~~~")
print("\n")

Number = [3,2,1,4,5]
print(f"Orignal Number's : {Number}")

#Sorting The Number
print("--"*25)
print("Sorting The Number : ")
Number.sort()
print(Number)
print("--"*25)

#Sorting Number In Reverse Order
print("--"*25)
print("Sorting Number In Reverse Order : ")
# Number.sort(reverse=True)
Number.reverse()
print(Number)
print("--"*25)

#Popping Items From List
print("--"*25)
print("Popping Item's from List : ")
Number.pop()
# Removed_Number = Number.pop()
print(Number)
print("--"*25)

#Popping Items From list With Index Number
print("--"*25)
print("Popping items from list with Index Number : ")
Number.pop(1)
print(Number)
print("--"*25)

print("\n")
print("~~~~~~~~~~~~~~~~~~ SLICING LIST ~~~~~~~~~~~~~~~~~~")
print("\n")

Alphabets = ["A","B","C","D"]
print(f"Orignal List : {Alphabets}")

#Getting First 2 Items From List
print("--"*25)
print("Getting First 2 Items : ")
print(Alphabets[:2])
print("--"*25)

#Getting MIddle of 2 Items from List
print("--"*25)
print("Getting Middle of 2 Items : ")
print(Alphabets[1:3])
print("--"*25)

#Getting Last 2 Items from List
print("--"*25)
print("Getting Last 2 Items : ")
print(Alphabets[-2:])
print("--"*25)

print("\n")
print("~~~~~~~~~~~~~~~~~~ NUMERIC LIST ~~~~~~~~~~~~~~~~~~")
print("\n")

Marks = [20,10,40,50]
print(f"Orignal List : {Marks}")

#Getting Min Marks from list 
print("--"*25)
print("Getting Min Marks : ")
print(min(Marks))
print("--"*25)

#Getting Max Marks From list
print("--"*25)
print("Getting Max Marks : ")
print(max(Marks))
print("--"*25)

#Getting Sum of Marks from list
print("--"*25)
print("Getting Sum of Marks : ")
print(sum(Marks))
print("--"*25)










