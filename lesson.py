customer = {
    "pin": 2024,
    "name":"Shelby",
    "balance":"15000",
    "status": "active",
    "phone": "+254792022047"
}

def withdraw(pin, amount, agent_no):
    print("====WELCOME SHELBY========")
    if pin == customer["pin"]:
            print("====ACCESS GRANTED====")
            if amount <= customer["balance"]:
                print(f"Confirmed. Successfully Withdrawn Kshs. {amount} from agent no. {agent_no}")
                balance = customer["balance"] - amount
                print(f"Your Balance is {balance}")
                print("Thank You!!!")
            else:
                print("Insufficient Account Balance!")
    else:
            print("======ACCESS DENIED======")
            print("Wrong Pin!!!")


