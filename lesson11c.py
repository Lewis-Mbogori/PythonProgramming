# Banking System
# Account

# Parent Class
class Bank:
    def __init__(self, usd_exchange_rate):
        self.usd_exchange_rate = usd_exchange_rate

    def usd_exchange_rate(self, currency):
        self.usd_exchange_rate * currency
        print(f"Your New Rate Is : {self}")

        
        


class Account(Bank):
    def __init__(self, name, pin, balance, accno, branch, status):
        super(). __init__(140)
        if balance <= 0:
            print("Account Balance Cannot be zero!")
        elif len(name) == ():
            print("Please Enter Account Name!")
        elif len(accno) != 6:
            print("Invalid Account Number")
        else:
            self.name = name
            self.pin = pin
            self.balance = balance
            self.accno = accno
            self.status = status
            self.branch = branch

    def withdraw(self):
        
        print("======WITHDRAW======")
        pin = int(input("Please Enter PIN: "))
        if pin == self.pin:
            print("=====ACCESS GRANTED=====")
            amount = int(input("Enter Amount To Withdraw: "))
            if amount <= self.balance:
                print("Success! You have withdrawn Kshs. {amount}")
                newBalance = self.balance - amount
                print(f"Your New Balance Is {newBalance}")

            else:
                print("Insufficient Account Balance!")

        else: 
            print("Wrong Pin!!!!")

    # Check Balance()
    def check_balance(self):
        print("====WELCOME TO CHECK BALANCE====== \n")
        pin = int(input("Enter Your PIN: "))
        if pin == self.pin:
            print("======ACCESS GRANTED======")
            print(f"Your Current Balance Is : {self.balance}")


    



account1 = Account("Modcom Institute", 1234, 10000, "123456", "Westlands", "Active")
account1.withdraw()
account1.check_balance()
account1.usd_exchange_rate()

# In Object Oriented Programming we follow some of its concepts:
# We have four concepts:
# 1. Inheritance: Childclass can inherit states and behaviours of a parent Class

# 2. Abstraction: It hides complexities of a program by implementing interfaces
# 3. Encapsulation: Classes can hide their information from other classes
# 4. Polymorphism: A Class can generate different instances
# Method Overloading
# Method Overriding


        