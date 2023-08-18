# For Loop in a sequence(Collection)
# collection: string, lists, tuples, dictionaries

language = "python"
for letters in language:
    print(letters)

print("============")
# List Sequence
# Loops with Conditions

proLanguages = ["Python", "C", "Java", "JavaScript"]
for language in proLanguages:
    if language == "Java":
        print("Java Exists")

    print(language)

    # Assumption
    # Create a list of 8 counties in kenya
    # Create 2 empty lists namely single and double

    # Task: 
    # Iterate through the list of 8 counties checking whether it has single name or double name
    # if it has single name append to single empty list, otherwise append to double

    counties = ["Nairobi", "Taita Taveta", "Garissa", "Nakuru", "Uasin Gishu", "Homa Bay", "Murang'a", "Kakamega"]

    double = []
    single = []

    for county in counties:
        if " " in county:
            double.append(county)
        else: 
            single.append(county)

    print(single)
    print(double)
    



