# Dictionary are used to store data in Key:Value Pairs

Employee_1 = {
                'Name' : "Sohel Shaikh",
                'Age'  : 28,
                'Department' : "Devops",
                'City' : "Solapur" 
             }

print("\n")
print(Employee_1)
print("\n")

#Getting Particular Value From Dictionary
print("--"*25)
print("Getting Particular Value From Dictionary")
print(Employee_1['City'])
print("--"*25)

# if we search a particular key from Dictionary when there is no key present in Dictionary.
# print(Employee_1['Salary'])
#it will show u this error > KeyError: 'Salary' <
#for avoiding this error use .get() Function like below
print("--"*25)
print("if we search a particular key from Dictionary when there is no key present in Dictionary, but we don’t want a Key error so, at that time we can use “get” method")
print(Employee_1.get("Bonus"))
print("--"*25)

#Adding New Key and It's Value
print("--"*25)
print("Adding New Key To Dictionary : ")
print(f"Befor Adding : {Employee_1}")
Employee_1['Salary'] = 45000
print(f"After Adding : {Employee_1}")
print("--"*25)

#If we want to delete Particular Key:Value From Dictionary
print("--"*25)
print("Deleting Particular Key:Value From Dictionary : ")
del Employee_1['Salary']
print(Employee_1)
print("--"*25)

#To Check The Total Length of Dictionary
print("--"*25)
print("Checking Length of Dictionary : ")
print(len(Employee_1))
print("--"*25)









