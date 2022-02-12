import requests
import json
import pandas as pd
import pymongo
from pymongo import MongoClient
import urllib3
urllib3.disable_warnings()

url = 'mongodb+srv://admin:g9L5dcEuO0Dhyv6X@cluster0.u0pgh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

client = pymongo.MongoClient(url)

mydb = client['demo']
collection = mydb.demoMovieCollection

# list = [{'Name': 'The Shawshank Redemption', 'year': 1994, 'Rating': 9.4, 'Parental Guide': 'R'},
#         {'Name': 'The Dark Knight', 'year': 2008,
#             'Rating': 9.0, 'Parental Guide': 'PG-13'},
#         {'Name': 'Toy Story', 'year': 1995, 'Rating': 8.3, 'Parental Guide': 'G'},
#         {'Name': 'John Wick', 'year': 2014, 'Rating': 7.4, 'Parental Guide': 'R'},
#         {'Name': 'Pulp Fiction', 'year': 1994,
#             'Rating': 8.9, 'Parental Guide': 'R'},
#         {'Name': '1917', 'year': 2019, 'Rating': 8.3, 'Parental Guide': 'R'}]

# collection.insert_many(list)

# for x in collection.find({"key1": "value1"}):
#     print(x)


# for x in collection.find({"key1": {"$eq": "value1"}}):
#     print(x)

def byName(name, queryList):
    # for x in collection.find({"Name": {"$eq": name}}):
    #     print(x)
    queryList.append({"Name": {"$eq": name}})
    return queryList


def byYear(year, query):
    # for x in collection.find({"year": {"$gt": year}}):
    #     print(x)
    queryList.append({"year": {"$gt": year}})
    return queryList


def byRating(rating, queryList):
    # for x in collection.find({"Rating": {"$gt": rating}}):
    #     print(x)
    queryList.append({"Rating": {"$gt": rating}})
    return queryList


def byPg(pg, query):
    # for x in collection.find({"Parental Guide": {"$ne": pg}}):
    #     print(x)
    queryList.append({"Parental Guide": {"$ne": pg}})
    return queryList


print("What category do you want your search to be based on\n1.Movie Name\n2.Year of Release\n3.Rating\n4.Exclude R rated Movies\n5.Execute Search")
option = any
queryList = []
while(option != "5"):
    option = input("Enter option : ")
    if(option == "1"):
        name = input("Enter Movie Name : ")
        queryList = byName(name, queryList)
    if(option == "2"):
        year = int(input("Enter Year : "))
        queryList = byYear(year, queryList)
    if(option == "3"):
        rating = float(input("Enter minimum rating : "))
        queryList = byRating(rating, queryList)
    if(option == "4"):
        pg = input("Enter PG rating to exclude : ")
        queryList = byPg(pg, queryList)


print("Displaying list\n", queryList)

if(len(queryList) == 1):
    for x in collection.find({"$and": [
        queryList[0]
    ]
    }):
        print(x)

if(len(queryList) == 2):
    for x in collection.find({"$and": [
        queryList[0],
        queryList[1],
    ]
    }):
        print(x)

if(len(queryList) == 3):
    for x in collection.find({"$and": [
        queryList[0],
        queryList[1],
        queryList[2]
    ]
    }):
        print(x)

if(len(queryList) == 4):
    for x in collection.find({"$and": [
        queryList[0],
        queryList[1],
        queryList[2],
        queryList[3]
    ]
    }):
        print(x)

if(len(queryList) == 5):
    for x in collection.find({"$and": [
        queryList[0],
        queryList[1],
        queryList[2],
        queryList[3],
        queryList[4]
    ]
    }):
        print(x)
