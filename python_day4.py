# Given two integers n and m, return their product if their product 
# is less than or equal to 1000; otherwise return their sum.
def sum_prod(n, m):
    if n * m <= 1000:
        return n * m
    else:
        return n + m

def test_sum_prod():
    print(f"Expect sum_prod(5, 7) to be 35: {sum_prod(5, 7)}")
    print(f"Expect sum_prod(69, 2) to be 138: {sum_prod(69, 2)}")
    print(f"Expect sum_prod(9, 2000) to be 2009: {sum_prod(9, 2000)}")
    print(f"Expect sum_prod(11, 100) to be 111: {sum_prod(11, 100)}")

#test_sum_prod()

# Given three integers, return 3 if all are equal, 
# return 2 if any two of them are equal, 
# and return 0 if they are all different.

def check_equals(a, b, c):
    if a == b and b == c:
        return 3
    elif a == b or b == c or a == c:
        return 2
    else:
        return 0

def test_check_equals():
    print(f"Expect check_equals(8, 7, 6) to be 0: {check_equals(8, 7, 6)}")
    print(f"Expect check_equals(8, 7, 8) to be 2: {check_equals(8, 7, 8)}")
    print(f"Expect check_equals(6, 7, 6) to be 2: {check_equals(6, 7, 6)}")
    print(f"Expect check_equals(7, 7, 7) to be 3: {check_equals(7, 7, 7)}")
    print(f"Expect check_equals(3, 3, 1) to be 2: {check_equals(3, 3, 1)}")
    print(f"Expect check_equals(2.1, 2.2, 2.5) to be 0: {check_equals(2.1, 2.2, 2.5)}")

#test_check_equals()

# Write a function that prints the first 3 items in a list. 
# Assume that the input list has at least three items.
def print_first_3(lst):
    print(lst[0])
    print(lst[1])
    print(lst[2])

lst = ["red","green","blue","purple"]
print_first_3(lst)

# Write a function that takes a list of numbers and 
# returns the sum of the first three numbers. 

def add_first_3(nums):
    return nums[0] + nums[1] + nums[2]

numbers = [6, 5, 4, 3, 2, 1]
print(add_first_3(numbers))

teachers = ["Ms. Ellyn", "Mr. Smith", "Ms. K"]
print(teachers)
# Modify the element at index 1
teachers[1] = "Mr. Emilio"
print(teachers)

# Assign the element at index 1 to another variable
name = teachers[1]
print(name)
print(teachers)

# Check if an element is in the list
if "Mr. Emilio" in teachers:
    print("Found Mr. Emilio!")
if "Mr. Smith" in teachers:
    print("Found Mr. Smith!")

print("Mr. Emilio" in teachers)
print("Mr. Smith" in teachers)

# Problems in Part 3 on the course website
# https://scuba.cs.uchicago.edu/problems.html
my_animals = ["lion", "panther", "jellyfish", "otter", "bulldog"]
my_animals.append("sponge")
my_animals.append("monkey")

print(my_animals)
sorted_animals = sorted(my_animals)
print(sorted_animals)

sorted_animals.pop(0)
sorted_animals.pop(0)
sorted_animals.pop(0)

print(sorted_animals)

print(len(sorted_animals))

sorted_animals[1] = "axolotl"

print(sorted_animals)
