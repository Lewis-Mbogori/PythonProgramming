# Collections(Arrays): groups of data on the same variable
# We have:
# List: []
# Tuple: ()
# Dictionary: {}
# Sets: {}

student1 = "Sally"
student2 = "Bob"
student3 = "Jane"

student = ["Sally", "Bob", "Jane"]

# Lists: Stores data in collection using a square bracket, each comma separated
# Properties: Ordered, mutable(changeable), allow duplicate data

counties = ["Nakuru", "Kajiado", "Nyandarua", "Bomet", "Wajir", "Nairobi"]
student = ["Sally", 23, False, 3.57]
print(type(counties))

# List Operations
# 1. print elements of a list
print(counties)
# 2. Accessing Items On A List
# Ordered: Indexing -> Items on a list are given numeric values starting from zero
# []
print(counties[2])
# Print the fourth item from the list
print(counties[3])
# 3. range of values (:)
# the first index included, but the last index excluded.
print(counties[1:])
print(counties[:3])
print(counties[1:3])
# print the 2nd, 3rd, 4th, and 5th
print(counties[1:5])
# Accessing all the items
print(counties[0:6])

# 4.List methods
# a) Add a new item to the list -> append()
counties.append("Nyeri")
print(counties)
# counties.append("Mombasa")
# counties.append("Kilifi")

newCounties = ["Kilifi", "Mombasa"]
counties.extend(newCounties)
print(counties)

# append and extend, add items to the end of the list
# insert(0, "")

counties.insert(1, "Kwale")
print(counties)

#  b) Removing items from a list
counties.pop()
print(counties)
counties.remove("Nyandarua")
print(counties)

counties.clear()
print(counties)