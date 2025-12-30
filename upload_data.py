from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri="mongodb+srv://pwskills1:nFYBDuO3sA6xzbPh@cluster01.tucy0.mongodb.net/?appName=Cluster01"

#create a new client and connect to server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME="sensor"
COLLECTION_NAME="faultdetect"

df=pd.read_csv("/Users/ankurpal/Desktop/Ankur Record/Projects/Project1.0/sensorprojects/notebook/wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)