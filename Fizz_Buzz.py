print("Fizz Buzz Program...")

till_number = int(input("Enter The Number - "))

my_list = []

for i in range(1,till_number+1):
    Result = ""
    if i % 3 == 0:
        Result = Result + "Fizz"
        # Result += "Fizz"
        if i % 5 == 0:
            Result = Result + "Buzz"
            # Result += "Buzz"
    elif i % 5 == 0:
        Result = Result + "Buzz"
        # Result += "Buzz"
    else:
        Result = i
    my_list.append(Result)

print(my_list)