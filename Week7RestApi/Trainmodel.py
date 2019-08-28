# Databricks notebook source
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LinearRegression
import pickle
from azure.storage.blob import BlockBlobService

data = pd.read_csv("https://twitterfilesa.blob.core.windows.net/twitterblob/train.csv")
nltk.download('stopwords')

corpus = []

for i in range(0,len(data)):
    wordData = re.sub('\W+',' ',data['SentimentText'][i]).lower().split()
    wordData = [PorterStemmer().stem(word) for word in wordData if not word in set(stopwords.words('english'))]
    wordData = ' '.join(wordData)
    corpus.append(wordData)

cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
Y = data.iloc[:, 1].values

regressor = LinearRegression()
regressor.fit(X,Y)

filename = 'TwitterModel.sav'
pickle.dump(regressor, open(filename, 'wb'))

block_blob_service = BlockBlobService(account_name='pramodsa18', account_key='SkzWJEkw53nJdb6MlVfeFEdteJ6n99LK/UoNiWKQdGCDpVUh/dbVWStp5tt38DquJt4YE58DRN0gpF4VR/bOdQ==')
block_blob_service.create_blob_from_path('twitter','TwitterTrainedModel.sav',filename)