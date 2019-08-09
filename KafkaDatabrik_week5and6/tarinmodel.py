import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings

dataset_train = pd.read_csv('https://sapramod.blob.core.windows.net/cpramod/Google_Stock_Price_Train.csv')
X = dataset_train.iloc[:,1:4].values
Y = dataset_train.iloc[:,4].str.replace(',','').astype(float)
regressor = LinearRegression()
regressor.fit(X,Y)
filename = 'TrainedSP.sav'
pickle.dump(regressor, open(filename, 'wb'))
block_blob_service = BlockBlobService(account_name='samstoragenew', account_key='6LfiZw6I0vdxfHOBQK9JjVSlNWtky8OZa52zb8LpGoJtAIG1buAPTyHWCDunYcbuO8hYcim3drWPYDzwdWv7Gg==')
#block_blob_service.create_container('cpramod')

#Upload the CSV file to Azure cloud
block_blob_service.create_blob_from_path('storagecontainer',dbutils.widgets.get('pickleName'),'TrainedSP.sav')
