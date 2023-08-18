# Nested if Conditions
# Money withdrawal Application

account = {
    "PIN": "1234",
    "name": "SHELBY",
    "balance": 10000
}
print("======WELCOME TO ABC BANK======")

while True:
    pin = input("Enter Your PIN: ")
    if pin == account["PIN"]:
        print(f"=====KARIBU {account['name']}=====")
        amount = int(input("Enter The Amount To Withdraw:  "))
        if amount <= account["balance"]:
            print(f"Confirmed. Withdrawn Kshs {amount}")
            newBalance = account["balance"] - amount
            print(f"Your Balance is{newBalance}")

        else:
         print("INSUFFICIENT ACCOUNT BALANCE!!")
        print(f"Your Balance Is {account['balance']}")

    else: 
        print("Wrong PIN, Try Again!!!")