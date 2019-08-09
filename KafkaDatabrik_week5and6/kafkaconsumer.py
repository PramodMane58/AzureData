
import numpy as np
import pandas as pd
import json
from kafka import KafkaConsumer
import pickle
from azure.storage.blob import BlockBlobService
import azure.cosmos.cosmos_client as cosmos_client 

consumer = KafkaConsumer('test',bootstrap_servers=bootstrap_servers=['10.1.0.7','10.1.0.5','10.1.0.6'],api_version=(0,10))

block_blob_service = BlockBlobService(account_name='sakafkademo', 
account_key='')


filename= "TestSP.sav"
block_blob_service.get_blob_to_path('kafkacondemo','pickleName2.sav',filename)
loaded_model = pickle.load(open(filename, 'rb'))

client = cosmos_client.CosmosClient(url_connection='',auth={'masterKey': ''})

database_link = dbs/KafkaDB
#db1 = client.ReadDatabase('dbs/KafkaDB')
db1 = client.CreatDatabase({'id':'KafkaDB'})
options = {'offerThroughput': 400}

container_definition = {
   'id':"KafkaDBRCont"
}

collection_link = database_link + '/colls/{0}'.format('KafkaDBRCont')
container = client.ReadContainer(collection_link,options)

# Create a container
#container = client.CreateContainer(db1['_self'],container_definition,options)


for message in consumer:
    dt =eval(message.value)
    #kafkalis.append(val)
    kafkalist =[]
    kafkalist.append(float(dt['1. open']))
    kafkalist.append(float(dt['2. high']))
    kafkalist.append(float(dt['3. low']))
    print("input = "+str(kafkalist))
    output=loaded_model.predict(np.array([kafkalist]))
    print("Prediced values ="+str(output))
    print("Original values ="+str(float(dt['4. close'])))

    item1 = client.CreateItem(container['_self'], {
             'id': str(i),
             'Open': str(float(dt['1. open'])),
             'High': str(float(dt['2. high'])),
             'Low':  str(float(dt['3. low'])),
             'ClosingPred': str(output)
             }
       )






