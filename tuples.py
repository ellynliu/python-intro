# Create a tuple and unpack it
my_tuple = (9, 10)
(a, b) = my_tuple
print(a)
print(b)

# Given two values, create a tuple
def make_tuple(x, y):
    return (x,y)

print(make_tuple(4, 5))

# Sum the values in the tuple
def sum_tuple(tuple):
    total = 0
    for i in range(len(tuple)):
        total = total + tuple[i]
    return total

tup = (8, 7, 6, 5, 4)
print(sum_tuple(tup))

# Create a new tuple with the first two elements of the given tuple
def first_two(tuple):
    return (tuple[0],tuple[1])

t = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print(first_two(t))

# Iterating over a list of tuples using a for loop
tuple_list = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

for (a, b) in tuple_list:
    print(a)

for (x, y) in tuple_list:
    print(y)

for (x, y) in tuple_list:
    print(f"{x} -- {y}")

# Given a list of baseball inning scores, calculate the total score
def baseball_scores(scores):
    team1_total = 0
    team2_total = 0
    for (t1, t2) in scores:
        team1_total += t1
        team2_total += t2
    return (team1_total, team2_total)

scores = [(0,1),(3,1),(1,0),(0,0),(0,1),(1,1),(4,2),(0,0),(1,0)]
t1, t2 = baseball_scores(scores)
print(t1)
print(t2)

# Add two tuples by summing the first values and the second values
# Unpack the tuples and add them
def add_tuples(tuple1, tuple2):
    a, b = tuple1
    c, d = tuple2
    return (a + c, b + d)

print(add_tuples((1, 2), (3, 4)))

# Alternative way to sum tuples using indexing
def add_tuples1(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])

print(add_tuples1((1, 2), (3, 4)))