import pandas as pd
import csv


#read into a list


#Reac to dictionary
teams = []
with open("team.csv", "r") as data:
    for item in csv.DictReader(data):
        teams.append(item)

print(teams)