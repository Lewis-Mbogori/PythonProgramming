# DICTIONARIES: collection {}
# Properties of a dictionary: unordered, no duplicates, mutable(changeable)-> keys
# Key - Value pair

student = ["Joseph", 34, "Male", False, ["Programming", "SQL"]]
# With lists data is accessed using indexing

student = {
    "name": "Joseph",
    "age": 34,
    "gender": "Male",
    "isPresent": "False",
    "subjects": ["Programming", "SQL"],
    "scores": {
        "programming": 100,
        "sql": 87

    }

}

print(type(student))

# Operations
# 1.printing dictionary
print(student)
# 2. Accessing items from a dictionary 
# we use key to access items from dictionary
print(student["gender"])
# Access subjects from the dictionary
print(student["subjects"])
# Updating values -> we use the key
student["age"] = 35
print(student)

student["subjects"] = ["Programming in python", "SQL"]
print(student)

# 4. Adding items to a dictionary
student["email"] = "joe@gmail.com"
print(student)

# Nested Dictionary
# Access the students SQL score
print(student["scores"]["sql"])


# Methods - functions
print(student.keys())
print(student.values())

student.clear()
print(student)