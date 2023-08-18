# CONTROL FLOW : A way to control program execution
# Three Categories:
# 1. Sequential control flow: Default, codes executed line by line(no indentation)
# 2. Conditional control flow: codes are executed based on some conditions

# 3. Iterative control flow: Codes are executed a number of times based on some conditions

# CONDITIONAL CONTROL FLOW
# we have 3 conditions, if, else, else if(elif), nested if

#IF: 
# condition/expression: checked return boolean (True, False)
# Statements: Code that is executed when condition is either True Or False


age = 15
if age > 18:
    print("ISSUED WITH ID")

else:
    print("PLEASE TRY NEXT TIME!")


    # IF ELSE: One Condition is checked if condition return is true if statement is executed , otherwise if the condition is false the else stateent is executed

    # Applying the idea of modulus(%) and conditions
    # Write a program to test whether a number is even (divisible by 2) or odd
    # Request the number from the user

    number = int(input("Enter Your Number"))
    if number % 2 == 0:
        print("EVEN NUMBER!!!")
    else:
        print("ODD NUMBER!!!")




