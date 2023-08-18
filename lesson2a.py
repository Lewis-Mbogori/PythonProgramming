# Data types
# Specify the format(type) of data stored on a variable e,g number, letter, collection....
# Specify the operation done on that variable
# In pythone :
# Integers (int): Numbers without decimal, e,g age, month...
# Floating Points (floats): Numbers with decimal places e,g distance, height, speed...
# Strings (str): sequence of characters enclosed insideneither double or single quotes e,g name, course
# Booleans (bool): a value having only 2 instances, e.g True , False

# Collections(Arrays): list, tuple, dictionary, sets

# Strings
# type()
# Escape sequence: used to introduce special characters inside a string\', \n

message = "I love programming"
print(type(message))

weather = 'It\'s a Chilly Morning'
print(weather)

paragraph = 'This is the first line,\n This is the second line'
print(paragraph)

firstmessage = "I love "
secondmessage = "python"

# Concatenation - merge strings (+)

wholemessage = firstmessage + secondmessage
print(wholemessage)

# len(): Return the number of characters in a string
password = input("Enter Your Password: ")
print(len(password))