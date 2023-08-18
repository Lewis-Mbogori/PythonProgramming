# Tuples: ()
# Properties: Ordered, duplicates allowed, immutable(unchangeable)
# Data from database to/from an application are enclosed on a tuple

counties = ("Nairobi", "Baringo", "Siaya")
print(type(counties))

# Create a tuple of one item
# Print the type

county = ("Nairobi")
print(county)

newCounty = tuple("Nakuru")
print(type(newCounty))

print(counties[0])

# Methods
counties.index("Nairobi")

newCounties = list(counties)
newCounties.append("Murang'a")

counties = tuple(newCounties)
print(counties)