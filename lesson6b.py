# Triangle

side1 = int(input("Enter First Side In cm: "))
side2 = int(input("Enter Second Side In cm: "))
side3 = int(input("Enter Third Side In cm: "))

# Equilateral
if side1 == side2 and side2 == side3:
    print("EQUILATERAL!!")

# Isosceles
elif (side1 == side2 and side2 != side3) or (side2 == side3 and side3 != side1) or (side3 == side1 and side1 != side2):
    print("ISOSCELES")

elif (side1 != side2) and (side2 != side3) and (side3 != side1):
    print("SCALENE")