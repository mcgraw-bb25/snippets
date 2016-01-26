#!/usr/bin/python3
'''
processes data 
appends total years to dataset 
saves to csv 
'''

import csv

new_player_list = []
columns = ["player_id", "year_id", "AB", "2B", "3B", "HR", "total_years"]
new_player_list.append(columns)

with open("../db/batting_data.csv", newline="") as data:
    reader = csv.reader(data)
    counter = 0 # used to skip first row
    year_counter = 1
    previous_row = []
    for player in reader:    
        if counter != 0:
            if player[0] == previous_player[0]:
                year_counter = year_counter + 1
                player.append(year_counter)
            else:
                year_counter = 1
                player.append(year_counter)
        else:
            player.append(year_counter)
        counter = counter + 1
        previous_player = player
        # print (player)
        new_player_list.append(player)

with open("new_batting.csv", "w", newline="") as output:
    writer = csv.writer(output)
    writer.writerows(new_player_list)
