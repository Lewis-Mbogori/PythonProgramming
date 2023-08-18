# create a program to perform simple interest taking inputs from the user
# Algorithm/pseudocode: Step by Step procedure to perform a task
# Get the formula: (PxRxT)/100
# Get Principal: Amount Deposited
# Get Rate
# Get the Time
# Apply the Formula
# Output Your Result

principal = int(input("Enter the amount deposited?: "))
rate = int(input("Enter the Rate?: "))
time = int(input("Enter the Time: "))

interest = (principal * rate * time)/100
print(f"Your Interest is {interest}")