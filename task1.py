# ELECTRICITY BILL CALCULATOR

print("=====WELCOME=====")
units = int(input("Enter Units Spent: "))
if units >=0 and units <=100:
    print("NO CHARGE")

if units >=100 and units <=200:
    price = (units) * 5
    print(price)

if units >=200:
    price2 = (units) * 10
    print(price2)