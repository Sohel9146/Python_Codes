print("Even or Odd Program...")


Active = True

while Active:
    Num = input("Enter The Number or Type q to EXIT - ")
    if Num.lower() == "q":
        print("Exiting From Loop...")
        Active = False
    elif int(Num) % 2 == 0:
        print("Number is EVEN..")
    else:
        print("Number is ODD..")