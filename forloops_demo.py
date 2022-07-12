# List of breakfast food items
breakfast = ["muffin", "bagel", "muffin", "muffin", "bagel", "danish", "croissant", "bagel"]

# Count the number of times a food shows up in the list items
# food: string representing a food
# items: list of food items
def count_num(items, food):
    total = 0
    for x in items:
        if x == food:
            total = total + 1

    return total

#print(count_num(breakfast, "muffin"))
#print(count_num(breakfast, "pancake"))

# Calculate the average of a list of values
# ratings: list of numbers
def average_rating(ratings):
    if ratings == []:
        return None
    else:
        total = 0
        for r in ratings:
            total = total + r
        return total/len(ratings)

bagel_ratings = [1,1,2,2,3,1.5,1,1,3,3.5,3,3,3.5,3,3,3.5,3.5,3.14]
chocolate_muffin_ratings = [4,3,4,4,3.5,5,5,4,4,5,3,4]
croissant_ratings = [3,4,1,4,3,1.5,5,5,2.5,2,2.5,2.71,3]

# print(average_rating(bagel_ratings))
# print(average_rating(chocolate_muffin_ratings))
# print(average_rating(croissant_ratings))

# What do you want for lunch on Thursday? Non-meat toppings?
# Dietary restrictions?
# Comment out the meat ones
dominos_top_10_toppings = [
    # "Pepperoni",
    "Mushrooms",
    "Onions",
    # "Sausage",
    # "Bacon",
    "Extra cheese",
    "Black olives",
    "Green peppers",
    "Pineapple",
    "Spinach",
]

toppings_counts = ['m', 'c', 'b', 'm', 'p', 'm', 'c', 's','c','m','c','c','o','s','c','c','c','c','c','s','m','m','s','g','c','p']

# Count the number of votes for each type of topping
# print(f"cheese: {count_num(toppings_counts, 'c')}")
# print(f"pineapple: {count_num(toppings_counts, 'p')}")
# print(f"mushroom: {count_num(toppings_counts, 'm')}")
# print(f"spinach: {count_num(toppings_counts, 's')}")
# print(f"onion: {count_num(toppings_counts, 'o')}")
# print(f"green peppers: {count_num(toppings_counts, 'g')}")
# print(f"black olive: {count_num(toppings_counts, 'b')}")

# List of teachers and their computers
scuba_teachers = ["Ellyn", "Zoa", "Emilio"]
scuba_teachers_computers = ["Benin", "Cameroon", "Macbook Pro"]
print(scuba_teachers[0])
print(scuba_teachers_computers[0])

# List of students and their computers
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

# Given the name of a person and the lists of people and computers,
# return the name of the computer belonging to the person
def find_computer(name, people, computers):
    for i in range(len(people)):
        if people[i] == name:
            return computers[i]
    return None

# Given the name of a computer, return the name of the individual
# the computer belongs to
def find_person(name, people, computers):
    for i in range(len(computers)):
        if computers[i] == name:
            return people[i]
    return None

'''
print("Borja's computer is", find_computer("Borja", scuba_teachers, scuba_teachers_computers))
print("Zoa's computer is", find_computer("Zoa", scuba_teachers, scuba_teachers_computers))
print("Cameroon belongs to", find_person("Cameroon", scuba_teachers, scuba_teachers_computers))
print("Benin belongs to", find_person("Benin", scuba_teachers, scuba_teachers_computers))

print("Monee's computer is ", find_computer("Monee", scuba_students, scuba_students_computers))
print("Ruby's computer is", find_computer("Ruby", scuba_students, scuba_students_computers))
print("Guatemala belongs to", find_person("Guatemala", scuba_students, scuba_students_computers))
print("Japan belongs to", find_person("Japan", scuba_students, scuba_students_computers))
print("Slovenia belongs to", find_person("Slovenia", scuba_students, scuba_students_computers))
'''

# Reverse a string by index
def reverse_string(str):
    for x in range(len(str)-1,-1,-1):
        print(str[x], end="")

#reverse_string("Mr. Emilio")

# Create a list of all the unique elements in a list (remove duplicates)
def unique_elements(lst):
    # lst = [5, 6, 7, 5]
    unique = [] # [5, 6, 7]
    for x in lst:
        if x not in unique:
            unique.append(x)
    return unique
'''
print(unique_elements(toppings_counts))
print(unique_elements(list("mississippi")))
print(unique_elements([5, 6, 7, 5]))
'''
