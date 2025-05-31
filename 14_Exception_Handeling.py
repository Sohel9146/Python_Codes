# 1 - With Normal Example

# print(10*2)
# print(10/2)


# try:
#     print(10/0)
    
# except Exception as e:
#     print(f"Kindely Do not Division by zero")

# print(10-2)

# 2 - With Files Exception Handeling

# try:
#     with open ("Family_name.txt", "r") as f:
#         content = f.readlines()
# except Exception as e:
#     print(f"The File You Looking For is not Available..",type(e))
# else:
#     for lines in content:
#         print(f"Well-Come - {lines.rstrip()}")