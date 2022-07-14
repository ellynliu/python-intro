red_line = ["Howard", "Jarvis", "Morse", "Loyola", "Granville", "Thorndale", "Bryn Mawr", "Argyle", "Wilson", "Sheridan", "Addison", "Belmont", "Fullerton", "North/Clybourn", "Clark/Division", "Chicago", "Grand", "Lake", "Monroe", "Jackson", "Harrison", "Roosevelt", "Cermak-Chinatown", "Sox-35th", "47th", "Garfield", "63rd", "69th", "79th", "87th", "95th/Dan Ryan"]
green_line = ["Oak Park (Green)","Harlem/Lake","Ridgeland","Austin (Green)","Central (Green)","Laramie","Cicero (Green)","Pulaski (Green)","Conservatory-Central Park Drive","Kedzie-Green","California-Green","Ashland-Lake","Morgan-Lake","Clinton (Green/Pink)","Clark/Lake","State/Lake","Washington/Wabash","Adams/Wabash","Roosevelt","Cermak-Mccormick Place","35th-Bronzeville-Iit","Indiana","43rd","47th (Green)","51st","Garfield (Green)","King Drive","East 63rd-Cottage Grove"]

# Find the index where the station is found in the list
# to_find: the station that you want to find
# lst: the list of all the stations
def find_position(to_find, lst):
    for i in range(len(lst)):
        if lst[i] == to_find:
            return i
    return None

# Calculate the distance, or the number of stations to stop by
# in order to reach the destination from station1 to station2
def calc_distance(station1, station2, line):
    return abs(find_position(station1, line) - find_position(station2, line))

# Print out all the train stops in between two stations
def enumerate(station_1, station_2, train_line):
  idx_1 = find_position(station_1, train_line)
  idx_2 = find_position(station_2, train_line)
  step = 1
  if idx_1 > idx_2:
    step = -1
  for i in range(idx_1, idx_2+step, step):
    print(train_line[i])

# Take in user input for two stations and print out the distance
# If the user provides a station name that does not exist, restart the function
def run(train_line):
    station1_name = input("Enter station number 1: ")
    if station1_name not in train_line:
        print(f"{station1_name} is not a valid station.")
        run(train_line)

    station2_name = input("Enter station number 2: ")
    if station2_name not in train_line:
        print(f"{station2_name} is not a valid station. Restart.")
        run(train_line)

    dist = calc_distance(station1_name, station2_name, red_line)
 
    print(f"The distance between {station1_name} and {station2_name} is {dist}.") 
    enumerate(station1_name, station2_name, train_line)
    run(train_line)

run(red_line)