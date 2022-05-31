# Delivery-5

Descrition of files:

File.py - Inserting information into an SQL database from a csv file

File2.py - Retreiving information from an SQL database into a csv file

File3.py - Inserting information into a NOSQL database from a csv file

File4.py - Retreiving information from a NOSQL database into a csv file

receiveDeliv5.py - Establishing a receiver for messages sent by the other scripts

try.csv - Sample csv data file used for insertion of data

data/NOSQL_Customer_data.csv - Output file for the data collected from a MongoDB database (created by file4.py)

data/SQL_Customer_data.csv - Output file for the data collected from an Azure Database for MySQL single server database (created by file2.py)

Additionally please read the requirments.txt

In order to see the full functionallity of the code (as shown in the report), please install Erlang and RabbitMQ in accordance with this guide:
https://kea.officegeek.dk/4sem/09-IT_architecture_Microservice/Rabbitmq.html

Once the conditions have been met, run the receiveDeliv5.py on a a separate terminal, from where you will be running the data insertion/collection scripts (file.py, file2.py, file3.py, file4.py).
