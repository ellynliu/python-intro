import matplotlib.pyplot as plt
import datetime as dt
import math
import numpy as np
import csv

# Download the CSV files from our course website.

def time_dist():
  f = open("202206-divvy-tripdata.csv")
  f.readline()

  classic_time = []
  electric_time = []

  classic_distance = []
  electric_distance = []

  for line in f.readlines():
    fields = line.split(',')
    
    start_time = dt.datetime.strptime(fields[2], '%Y-%m-%d %H:%M:%S')
    end_time = dt.datetime.strptime(fields[3], '%Y-%m-%d %H:%M:%S')
    delta = end_time - start_time
    delta_seconds = delta.total_seconds()

    lat1 = fields[8]
    long1 = fields[9]
    lat2 = fields[10]
    long2 = fields[11]
    if lat1 != "" and lat2 != "" and long1 != "" and long2 != "" and delta_seconds > 0:
      dist = abs(float(lat2) - float(lat1))*69 + abs(float(long2) - float(long1))*54.8

      if fields[1] == 'classic_bike':
        classic_time.append(delta_seconds)
        classic_distance.append(dist)
      elif fields[1] == 'electric_bike':
        electric_time.append(delta_seconds)
        electric_distance.append(dist)
    
  return classic_time, electric_time, classic_distance, electric_distance
    
classic_time, electric_time, classic_distance, electric_distance = time_dist()

plt.scatter(classic_time, classic_distance, alpha=0.4)
plt.scatter(electric_time, electric_distance, alpha=0.4)
plt.show()

import csv

def analyze():
  death_ages = []
  birth_years = []
  with open("AgeDataset-V1.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    for fields in reader:
      birth_year = fields[6]
      death_age = fields[9]
      if birth_year.isnumeric() and death_age.isnumeric():
        death_ages.append(int(death_age))
        birth_years.append(int(birth_year))
  return death_ages, birth_years

death_ages, birth_years = analyze()

plt.scatter(birth_years, death_ages, alpha=1)
plt.xticks(np.arange(min(birth_years), max(birth_years), 250))
plt.yticks(np.arange(min(death_ages), max(death_ages), 10))
plt.show()

def rides_dict():
  f = open('202206-divvy-tripdata.csv')
  f.readline()

  start_dict = {}
  end_dict = {}
  journey_dict = {}

  for line in f.readlines():
    fields = line.split(',')
    start_station = fields[4]
    end_station = fields[6]

    if start_station not in start_dict:
      start_dict[start_station] = 1
    else:
      start_dict[start_station] += 1

    if end_station not in end_dict:
      end_dict[end_station] = 1
    else:
      end_dict[end_station] += 1

    if (start_station, end_station) not in journey_dict:
      journey_dict[(start_station, end_station)] = 1
    else:
      journey_dict[(start_station, end_station)] += 1

  start_dict.pop('')
  end_dict.pop('')
  journey_dict.pop(('', ''))

  sorted_start_dict = sorted(start_dict.items(), key=lambda x: x[1], reverse=True)
  sorted_end_dict = sorted(end_dict.items(), key=lambda x: x[1], reverse=True)
  sorted_journey_dict = sorted(journey_dict.items(), key=lambda x: x[1], reverse=True)

  return sorted_start_dict[:10], sorted_end_dict[:10]
  #print(sorted_journey_dict[:10])
    
origin_dict, end_dict = rides_dict()

start_stations = []
start_values = []
end_stations = []
end_values = []
for s, n in origin_dict:
  start_stations.append(s)
  start_values.append(n)

for s, n in end_dict:
  end_stations.append(s)
  end_values.append(n)
plt.barh(start_stations, start_values)
#plt.barh(end_stations, end_values, alpha=0.3)

plt.show()

'''
0: Country
1: Year
2: Life expectancy
3: GDP per capita
4: Population (historical estimates)
5: Continent
'''
def is_float(element) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False

def world_data():
  le_list = []
  gdp_list = []
  with open('Life Expectancy vs GDP 1950-2018.csv', "r") as f:
    reader = csv.reader(f, delimiter=",")
    for fields in reader:
      le = fields[2]
      gdp = fields[3]
      #print(le)
      #print(gdp)
      if le != "" and is_float(le) and gdp != "" and is_float(gdp):
        #print(le, gdp)
        le_list.append(float(le))
        gdp_list.append(float(gdp))
  return le_list, gdp_list

le_list, gdp_list = world_data()

plt.scatter(le_list, gdp_list, alpha = 0.3)
plt.show()
