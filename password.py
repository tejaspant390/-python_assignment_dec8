#A program to check the password.

password= "tejas"

def word(value):
    if(value == password):
        print("Password match")
    else:
        print("Password is wrong")

value=input("Enter the password: ")
word(value)