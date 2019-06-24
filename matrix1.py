X = [[12,7,3],[4 ,5,6],[7 ,8,9]]
Y = [[5,8,1],[6,7,3],[4,5,9]]

result =[]
for i in range(len(X)):
    newlist = []
    for j in range(len(X[0])):
        newlist.append(X[i][j] + Y[i][j])
    result.append(newlist)

print(result)