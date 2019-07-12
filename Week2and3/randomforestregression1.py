
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor

dataset = pd.read_csv('/home/admininistrator/Downloads/Position_Salaries.csv')

x = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values

#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=0)

regressor = RandomForestRegressor(n_estimators = 1000, random_state = 42)
regressor.fit(x, y)

pickle_out = open("/home/admininistrator/Downloads/rft1.pickle","wb")
pickle.dump(regressor, pickle_out)
pickle_out.close()

X_grid = np.arange(x.min(),x.max(),0.1)
X_grid = X_grid.reshape(len(X_grid),1)
plt.scatter(x,y,color='maroon')
plt.plot(X_grid,regressor.predict(X_grid),color = 'red')
plt.title('temp VS count')
plt.xlabel('salary')
plt.ylabel('postion level')
plt.show()

pickle_in = open("/home/admininistrator/Downloads/rft1.pickle","rb")
example_dict = pickle.load(pickle_in)
print(example_dict.predict([[1]]))