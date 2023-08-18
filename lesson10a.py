# Error Handling/Exception Handling.......
# Handling Errors created by the users to avoid system from crashing
# we use try, except block
# try: houses a code that generate an error from the user
# except/catch: where the error is handled before the system crashing

# while True:
#     try: 
#         number = int(input("Enter a Digit: "))
#         print(f"You have entered {number}")

#     except: ("please enter a valid input...")

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

division = num1/num2
print(division)


# Handle the error above....