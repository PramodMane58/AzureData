import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
import pickle
from azure.storage.blob import BlockBlobService
import azure.cosmos.cosmos_client as cosmos_client
nltk.download('stopwords')
dataTest = pd.read_csv("https://twitterfilesa.blob.core.windows.net/twitterblob/test.csv")

corpus = []

for i in range(0,1000):
    wordData = re.sub('[^A-Za-z]',' ',dataTest['SentimentText'][i]).lower().split()
    wordData = [PorterStemmer().stem(word) for word in wordData if not word in set(stopwords.words('english'))]
    wordData = ' '.join(wordData)
    corpus.append(wordData)

print(corpus[0])

cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()

block_blob_service = BlockBlobService(account_name='pramodsa18', account_key='ye5m/GZky5bYmCYEeqbNUJ05eIWW7Wvp1X9Fl1iq2DQjGaGdS3KA3+ZBvO3SiIptSPQckToeIdLL3V985fba+Q==')
filename= "TestTwitterModel.sav"
block_blob_service.get_blob_to_path('twitter','TwitterTrainedModel.sav',filename)
loaded_model = pickle.load(open(filename, 'rb'))
# output=loaded_model.predict(X_Test)
output=loaded_model.predict(X)
print((output))

client = cosmos_client.CosmosClient(url_connection='https://pramodcosmosdb.documents.azure.com:443/', auth={'masterKey': 'hG0iLFvYmaFBkuTkkje97FW2L2ZQZabsVZJYT90n93ju5m2P6x0nUQHA26vUIAS3D4Fl5tXdjSKzQc7DKXEosg=='})

database_link = 'dbs/SPTestdb'
#db1 = client.ReadDatabase(database_link)
# collection_link = database_link + '/colls/{0}'.format('SPTestdbContainer')
# container = client.ReadContainer(collection_link,options)
db1 = client.CreateDatabase({ 'id': 'SPTestdb'})
options = {'offerThroughput': 400}

container_definition = {
    'id': "containerName"
}

# Create a container
container = client.CreateContainer(db1['_self'],container_definition,options)

for i in range(0,1000):
 item1 = client.CreateItem(container['_self'], {
     'id': str(i+1),
     'Sentiment':str(dataTest['SentimentText'][i]),
     'ClosingPred': round(output[i])
     }
)