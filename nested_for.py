# Nested loops for ice cream sizes and flavors
def ice_cream():
  sizes = ["Kid", "Small", "Medium", "Large"]
  flavors = ["Vanilla", "Chocolate", "Strawberry", "Black Raspberry", "Coconut"]
  
  print("Ice cream cones by size")
  for s in sizes:
    for f in flavors:
      print(f"{s} {f}")
  print()
  
  print("Ice cream cones by flavor")
  for f in flavors:
    for s in sizes:
      print(f"{s} {f}")
#ice_cream()

# Print out the coordinates of nested for loops
def coords():
  for i in range(5):
    print(f"row {i}:", end = " ")
    for j in range(5):
        print(f"({str(i)}, {str(j)})", end=" ")
    print()
#coords()

# Print out a multiplication table
def multiplication_table():
  for i in range(1, 21):
    for j in range(1, 21):
        print(f"{i*j:>4}", end=" ")
    print()
#multiplication_table()

# Print out an exponents table
def exponentiation_table():
  for i in range(10):
    for j in range(10):
        print(f"{i**j:>9}", end=" ")
    print()
  day_num = 1
#exponentiation_table()

# Print out a calendar 
def calendar():
  day_num = 1
  print(" Mon  Tue  Wed  Thu  Fri  Sat  Sun")
  for week in range(5):
    for day in range(7):
        print(f"{day_num:>4}", end=" ")
        day_num += 1
        if day_num > 31:
            break; 
    print("\n")
#calendar()
