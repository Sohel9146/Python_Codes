#Block of code which perform particular task and run when it is called
#can be use many times in our program which lessen our line of code
#we can pass argument to the functions

# 1 - Normal Example 

# def my_fun():
#     print("--"*25)
#     print("Function is Called..")
#     print("--"*25)


# my_fun()

# 2 - Sending Arguments to the Function

# def my_fun(name,city):
#     print("--"*25)
#     print(f"Name is : {name}")
#     print(f"City is : {city}")
#     print("--"*25)

   
# my_fun("Sohel Shaikh","Solapur")
# my_fun("Arshad Shaikh","Solapur")

# 3 - Adding two numbers 


# def addtion(Num_1,Num_2):
#      return Num_1 + Num_2

# Num_1 = int(input("Enter Num 1 : "))
# Num_2 = int(input("Enter Num 2 : "))

# Result = addtion(Num_1,Num_2)
# print(f"Addition is {Result}")

# 4 - Even or Odd Program

# def EvenOrOdd(Num):
#     if Num % 2 == 0:
#         print(f"{Num} is Even..")
#     else:
#         print(f"{Num} is Odd..")

# Num = int(input("Enter The Number : "))

# EvenOrOdd(Num)

# 5 - Finding MAX of 3 Numbers

# def Max_Of_Three(a,b,c):
#     return max(a,b,c)

# print("--"*25)
# Num_1 = int(input("Enter Number 1 : "))
# Num_2 = int(input("Enter Number 2 : "))
# Num_3 = int(input("Enter Number 3 : "))

# Result = Max_Of_Three(Num_1,Num_2,Num_3)
# print("--"*25)
# print(f"Max Number is : {Result}")
# print("--"*25)


# 6 - Count Vowels

# def Count_Vowels(Name):
#     Vowels = "aeiouAEIOU"
#     count = 0
#     for char in Name:
#         if char in Vowels:
#             count += 1
        
#     return count

# print("--"*25)
# Name = input("Enter String : ")

# total  = Count_Vowels(Name)
# print(f"Toatl Vowels in '{Name}' is : {total}")
# print("--"*25)


# 7 - Reverse String Function 

# def Reverse_String(String):
#     return String[::-1]

 
# print("--"*25)
# String = input("Enter A String to Reverse : ")

# Result = Reverse_String(String)

# print(f"Your Reversed String is : {Result}")
# print("--"*25)


# 8 - Sum of List Elements 

# def Sum_Of_List(Number_List):
#     # return sum(Number_List)
#     total = 0

#     for num in Number_List:
#         total += num

#     return total


# User_Input = input("Enter The Number Seprated by Space : ")

# Number_List = list(map(int, User_Input.split()))


# Result = Sum_Of_List(Number_List)
# print(f"Addition of provided list is : {Result}")

# 9 - Find the Largest Number in List 

# def Largest_Number(Number_list):
#     return max(Number_list)


# print("--"*25)
# User_Input = input("Enter The Number's Seprated by Space : ")

# Number_list = list(map(int,User_Input.split()))

# Result = Largest_Number(Number_list)

# print("\n")
# print(f"Largest Number from {Number_list} is : {Result}")
# print("--"*25)