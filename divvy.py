# Download data from https://divvy-tripdata.s3.amazonaws.com/202206-divvy-tripdata.zip

# If you are working with a CSV file with commas as
# part of the fields, then a regular string split 
# with a comma delimiter wil not be sufficient. 
# In this case, open the file as a CSV file.
'''
import csv

def analyze():
    with open("AgeDataset-V1.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        for fields in reader:
            #your code here
'''

'''
Column 0: ride_id
Column 1: rideable_type
Column 2: started_at
Column 3: ended_at
Column 4: start_station_name
Column 5: start_station_id
Column 6: end_station_name
Column 7: end_station_id
Column 8: start_lat
Column 9: start_lng
Column 10: end_lat
Column 11: end_lng
Column 12: member_casual
'''

# Count the number of classic and electric bike rides in the dataset.
def analyze():
    f = open("202206-divvy-tripdata/202206-divvy-tripdata.csv")
    f.readline()
    classic_bike_total = 0
    electric_bike_total = 0
    for line in f.readlines():
        fields = line.split(",")
        bike_type = fields[1]
        if bike_type == "classic_bike":
            classic_bike_total += 1
        elif bike_type == "electric_bike":
            electric_bike_total += 1
    return (classic_bike_total, electric_bike_total)
  
# Count the number of round trips, AKA when a bike started and ended at the same station.
def round_trips():
    f = open("202206-divvy-tripdata/202206-divvy-tripdata.csv")
    count = 0
    for line in f.readlines():
        fields = line.split(",")
        start_station = fields[4]
        end_station = fields[6]
        if start_station == end_station:
            count += 1
    return count
  
# Get all of the unique divvy stations.
def unique_stations():
    f = open("202206-divvy-tripdata/202206-divvy-tripdata.csv")
    stations = set()

    f.readline()
    for line in f.readlines():
        fields = line.split(",")
        start_station = fields[4]
        end_station = fields[6]
        stations.add(start_station)
        stations.add(end_station)

    print(len(stations))
    sorted_stations = sorted(list(stations))
    return sorted_stations

  
