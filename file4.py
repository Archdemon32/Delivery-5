# Imports
import pika
import pandas as pd
from pymongo import MongoClient
import pymongo
# Defining a connection function
def get_database():
    client = MongoClient("mongodb://localhost:27017/Deliv5")
    return client['Deliv5']
if __name__ == "__main__":
    dbname = get_database()
# Finding all the items inside the collection
collection_name = dbname["Deliv5"]
item_details = collection_name.find()
# Writing all the found data into a csv
for item in item_details:
    with open('Customer_Data.csv','a+') as l:
        l.write(str(item))
        l.write('\n')
# Using rabitMQ to send a message
connection1 = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection1.channel()

channel.queue_declare(queue='data')

channel.basic_publish(exchange='', routing_key='data', body=("Records retrieved successfully from Deliv5"))
