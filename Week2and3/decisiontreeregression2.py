import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

dataset = pd.read_csv('/home/admininistrator/Downloads/bike_sharing.csv')

X = dataset[['temp']].values
y = dataset[['cnt']].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=0)

regressor = DecisionTreeRegressor()
regressor.fit(X, y)

pickle_out = open("/home/admininistrator/Downloads/dtr2.pickle","wb")
pickle.dump(regressor, pickle_out)
pickle_out.close()

X_grid = np.arange(X.min(),X.max(),0.1)
X_grid = X_grid.reshape(len(X_grid),1)
plt.scatter(X,y,color='maroon')
plt.plot(X_grid,regressor.predict(X_grid),color = 'red')
plt.title('temp VS count')
plt.xlabel('salary')
plt.ylabel('postion level')
plt.show()

pickle_in = open("/home/admininistrator/Downloads/dtr2.pickle","rb")
example_dict = pickle.load(pickle_in)
print(example_dict.predict([[30]]))