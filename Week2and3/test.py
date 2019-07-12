from sklearn.preprocessing import StandardScaler
data = [[0, 0], [0, 0], [1, 1], [1, 1]]
scaler = StandardScaler()
print(scaler.get_params(deep=True))
data = scaler.transform(data)
print(data)
'''StandardScaler(copy=True, with_mean=True, with_std=True)
print('/n')
print(scaler.mean_)
print('/n')
print(scaler.transform(data))
print('/n')
print(scaler.transform([[2, 2]]))'''

