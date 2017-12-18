import csv
from pymongo import MongoClient

cdpath = 'C://Users//rafae//Desktop//Udacity//Project 1 - Explore Weather Trends//city_data.csv'

csvfile = open(cdpath)
reader = csv.DictReader(csvfile)
