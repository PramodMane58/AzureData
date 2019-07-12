import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import
from sklearn.svm import SVR
dataset = pd.read_csv('/home/admininistrator/Downloads/bike_sharing.csv')

X = dataset[['temp']].values #np.array(pd.DataFrame(dataset,columns=['temp']))
y = dataset[['cnt']].values#np.array(pd.DataFrame(dataset,columns=['cnt']))

from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
X = sc_x.fit_transform(X)
y = sc_y.fit_transform(y)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=0)




#Fitting Simple Linear Regression to the Training set

regressor = SVR(kernel='rbf')
regressor.fit(X, y)


pickle_out = open("/home/admininistrator/Downloads/svr2.pickle","wb")
pickle.dump(regressor, pickle_out)
pickle_out.close()

plt.scatter(X_train,y_train, color='red')
plt.plot(X_test, regressor.predict(X_test), color='blue')
plt.title('temp VS count')
plt.xlabel('salary')
plt.ylabel('postion level')
plt.show()

pickle_in = open("/home/admininistrator/Downloads/svr2.pickle","rb")
example_dict = pickle.load(pickle_in)
print(example_dict.predict([[4]]))