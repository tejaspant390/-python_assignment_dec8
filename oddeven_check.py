#A function to determine whether the user's integer input is an even number or an odd number.

def even(x):
    if (x%2==0):
       print("The number is even.")
    else:
        print("The number is odd.")

x=int(input("Enter a number: "))
even(x)