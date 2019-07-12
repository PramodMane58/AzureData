
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('/home/admininistrator/Downloads/bike_sharing.csv')

X = pd.DataFrame(dataset,columns=['temp'])
y = pd.DataFrame(dataset,columns=['cnt'])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)


pickle_out = open("/home/admininistrator/Downloads/slr2.pickle","wb")
pickle.dump(regressor, pickle_out)
pickle_out.close()

y_pred = regressor.predict(X_test)


plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('temp VS count')
plt.xlabel('temp')
plt.ylabel('count')
plt.show()


pickle_in = open("/home/admininistrator/Downloads/slr2.pickle","rb")
example_dict = pickle.load(pickle_in)
print(example_dict.predict([[4]]))