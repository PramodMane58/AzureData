import numpy
import pandas as pd
import pickle
import json
from azure.storage.blob import BlockBlobService
import azure.cosmos.cosmos_client as cosmos_client 

block_blob_service = BlockBlobService(account_name='samstoragenew', account_key='6LfiZw6I0vdxfHOBQK9JjVSlNWtky8OZa52zb8LpGoJtAIG1buAPTyHWCDunYcbuO8hYcim3drWPYDzwdWv7Gg==')
filename= "TestSP.sav"
block_blob_service.get_blob_to_path('storagecontainer','ContainerSPTrainedModel.sav',filename)
loaded_model = pickle.load(open(filename, 'rb'))
# output=loaded_model.predict(X_Test)
output=loaded_model.predict(numpy.array([223.2,232,233.2]))

client = cosmos_client.CosmosClient(url_connection='https://samcosmosdb.documents.azure.com:443/', auth={'masterKey': '8T2ueEuMFOFQE5exKfwB3k0minrqYxRk69SUxjpe0qLIZjvWXtOlBeje6HhsBTGy5tUfuX9v7gSAupGQksb5dg=='})

database_link = 'dbs/SPTestdb'
db1 = client.ReadDatabase(database_link)
# collection_link = database_link + '/colls/{0}'.format('SPTestdbContainer')
# container = client.ReadContainer(collection_link,options)
# db1 = client.CreateDatabase({ 'id': 'SPTestdb'})
options = {'offerThroughput': 400}

container_definition = {
    'id': dbutils.widgets.get("containerName")
}

# Create a container
container = client.CreateContainer(db1['_self'],container_definition,options)
for i in range(0,len(output)):
  X = X_Test[i].tolist()
  item1 = client.CreateItem(container['_self'], {
      'id': str(i+1),     
      'Open': X[0],
      'High':X[1],
      'Low':X[2],
      'ClosingPred': output[i]
      }
)

query = {'query': 'SELECT * FROM c'}

options = {}
options['enableCrossPartitionQuery'] = True
options['maxItemCount'] = 2

result_iterable = client.QueryItems(container['_self'], query, options)
for item in iter(result_iterable):
    print(item['Open'],item['ClosingPred'])
