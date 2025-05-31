# Same as List, However You Can't Modify the items of Tuple.
# Tuple is Immutable
# it is ordered

print("\n")

Name = ("Sohel","Irfan","Arshad","Wasim","Shuaib","Sohel")
print(Name)
print("\n")


# For Counting How Many Time Given Item is Present in the Tuple
print("--"*25)
print("Count Function : ")
print(Name.count("Sohel"))
print("--"*25)

# For Checking Index Number of Given Item in Tuple
print("--"*25)
print("Index Function : ")
print(Name.index("Irfan"))
print("--"*25)

#if u try to Modify The Tuple Items
# Name[0] = "Shuaib"
# TypeError: 'tuple' object does not support item assignment

