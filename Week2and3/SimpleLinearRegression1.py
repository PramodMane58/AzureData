
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('/home/admininistrator/Downloads/Salary_Data.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

pickle_out = open("/home/admininistrator/Downloads/slr1.pickle","wb")
pickle.dump(regressor, pickle_out)
pickle_out.close()


y_pred = regressor.predict(X_test)


# Visualizing the Test set results
viz_test = plt
viz_test.scatter(X_test, y_test, color='red')
viz_test.plot(X_train, regressor.predict(X_train), color='blue')
viz_test.title('Salary VS Experience (Test set)')
viz_test.xlabel('Year of Experience')
viz_test.ylabel('Salary')
viz_test.show()


pickle_in = open("/home/admininistrator/Downloads/slr1.pickle","rb")
example_dict = pickle.load(pickle_in)
print(example_dict.predict([[4]]))

accuracy = regressor.score(X_test,y_test)
print(accuracy*100,'%')