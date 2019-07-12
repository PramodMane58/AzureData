
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle
from sklearn.tree import DecisionTreeRegressor

dataset = pd.read_csv('/home/admininistrator/Downloads/Position_Salaries.csv')
x = dataset.iloc[:,1:2].values #get a copy of dataset exclude last column
y = dataset.iloc[:,2].values #get array of dataset in column 1st
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(x, y)

pickle_out = open("/home/admininistrator/Downloads/dtr1.pickle","wb")
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

pickle_in = open("/home/admininistrator/Downloads/dtr1.pickle","rb")
example_dict = pickle.load(pickle_in)
print(example_dict.predict([[6]]))
