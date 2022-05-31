# Imports
import mysql.connector as mc
import pika
import pandas as pd
# Reading the csv from customer
df = pd.read_csv(r"C:\Users\archd\Desktop\demo\try.csv", index_col=False, delimiter = ';')
# Connecting to the databse
try:
    connection = mc.connect(host='dp-base.mysql.database.azure.com',
                                         database='db_test',
                                         user='archdemon32@dp-base',
                                         password='Pepega321998')
# Inserting the values from the csv
    for i,row in df.iterrows():
        sql="INSERT INTO all_csv_files VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor = connection.cursor()
        cursor.execute(sql, tuple(row))
        connection.commit()
# Error excption
except mc.Error as error:
    print("Failed to insert record into all_csv_files table {}".format(error))
# Using rabitMQ to send a message if the conncetion was sucessfull
finally:
    if connection.is_connected():
        connection1 = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection1.channel()

        channel.queue_declare(queue='data')

        channel.basic_publish(exchange='', routing_key='data', body=("Records inserted successfully into all_csv_files table"))
        connection.close()
        cursor.close()
