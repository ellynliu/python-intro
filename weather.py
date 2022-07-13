may_june = [59, 55, 52, 56, 54, 54, 75, 79, 85, 92, 91, 95, 94, 79, 80, 65, 63, 88, 89, 63, 64, 62, 67, 83, 79, 63, 76, 87, 91, 90, 79, 79, 83, 81, 76, 71, 72, 80, 82, 75, 74, 92, 100, 100, 97, 88, 75, 88, 96, 101, 92, 85, 93, 81, 82, 81, 88, 89, 93, 86, 87, 89, 95]

# Find the highest (or maximum) temperature in the list 
def high_temp(temps):
    high_temp = 0
    for t in temps:
        if t > high_temp:
            high_temp = t
    return high_temp

print(high_temp(may_june))

# Find the lowest (or minimum) temperature in the list
def low_temp(temps):
    low_temp = 200
    for t in temps:
        if t < low_temp:
            low_temp = t
    return low_temp

print(low_temp(may_june))

# Find the average temperature of the values in the list
def avg_temp(temps):
    total = 0
    for t in temps:
        total = total + t
    return total/len(temps)

print(avg_temp(may_june))

# Challenge: Find the greatest temperature difference between two consecutive days
def greatest_diff(temps):
    curr_max = 0
    idx1 = 0
    idx2 = 0
    for i in range(len(temps)-1):
        check = abs(temps[i+1] - temps[i])
        if check > curr_max:
            curr_max = check
            idx1 = i
            idx2 = i+1
    return curr_max, idx1, idx2

print(greatest_diff(may_june))
print(may_june[18], may_june[19])