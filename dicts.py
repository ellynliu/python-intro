# Create a dictionary with teachers and their ages
teachers_ages = {
"Ms. Ellyn": 22,
"Ms. K": 20,
"Mr. Emilio": 20,
"Mr. Ben": 97
}

# Access a value with the key
print(teachers_ages["Mr. Emilio"])

# The keys method returns the dictionary keys
print(teachers_ages.keys())

# The values method returns the dictionary values
print(teachers_ages.values())

# Remove an element by the key and return the value
print(teachers_ages.pop("Ms. K"))
print(teachers_ages)

# Create a dictionary with students and their computers
students_laptop = {
    "Malik": "Finland",
    "Ajibola": "Romania",
    "Asia": "Honduras",
    "Ruby": "Oman",
    "Joshua Clark": "Qatar",
    "Alila": "Uruguay",
    "Dajah": "Estonia",
    "Milana": "Nambia",
    "Jahatrell": "India",
    "David": "Slovenia",
    "Armando": "Denmark",
    "Joshua Passmore": "Zimbabwe",
    "Monee": "Kenya",
    "Khalid": "Japan"
}

print(students_laptop)
print(students_laptop["Ajibola"])
print(students_laptop["Armando"])

# In a previous class, we created separate lists of students and their computers
# In this exercise, we combine the information into a dictionary
scuba_students = ["Jamellia",
"Monee",
"Khalid",
"Joshua",
"Armando",
"David",
"Jahatrell",
"Alila",
"Ruby",
"Yaneli",
"Milana",
"Dajah",
"Ajibola",
"Asia",
"Malik"
]
scuba_students_computers = ["Moldova",
"Kenya",
"Japan",
"Zimbabwe",
"Denmark",
"Slovenia",
"India",
"Uruguay",
"Oman",
"Guatemala",
"Nambia",
"Estonia",
"Romania",
"Honduras",
"Finland"
]

# Create a dictionary of the students and their computers given two lists
def zip(students, computers):
    dict = {}
    for i in range(len(students)):
        student = students[i]
        computer = computers[i]
        dict[student] = computer
    return dict

computers_dict = zip(scuba_students, scuba_students_computers)
for (name, comp) in computers_dict.items():
    print(name, ": ", comp)

# Print out each value in the dictionary
def print_dict(dict):
    for key in dict:
        print(dict[key])

print_dict(computers_dict)