import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#Handling missing data
df = pd.read_csv("/home/admininistrator/Downloads/data_preprocessing.csv")
values = {'Age': df['Age'].mean(), 'Salary': df['Salary'].mean()}
df.fillna(value=values, inplace=True)


#Handling categorical data
df = pd.concat([df, pd.get_dummies(df['Country'])], axis=1);
print(df)

df.drop(['Country'], axis=1)

x = pd.DataFrame(df,columns=['France','Germany','Spain','Age','Salary'])
y = pd.DataFrame(df,columns=['Purchased'])
#print(x)
#print(y)

#Split the dataset into a training set and test set

#train, validate, test = np.split(df.sample(frac=1), [int(.6*len(df)), int(.8*len(df))])
from sklearn.model_selection import train_test_split
x_tarin,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)
print(x_tarin)
print(x_test)


#Feature scaling
from sklearn.priprocessing import StandarScaler
sc_x= StandarScaler()
x_tarin = sc_x.fit_transfrom(x_tarin)
x_test = sc_x.transfrom(x_test)

