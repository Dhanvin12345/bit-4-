def  setOrNot(number, n):
    # Make a mask variable by left shift 1 (n - 1)times
    # Then check if (number AND mask) equals to 1 or not
    if number & (1 << (n - 1)):
        print("\nSET")
    else:
        print("\nNOT SET")


# Take inputs from the user
number = int(input("Enter number: "))
n = int(input("Enter bit number"))

setOrNot(number, n)