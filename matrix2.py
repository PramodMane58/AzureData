X = [[12,7,3],[4 ,5,6],[7 ,8,9]]
Y = 9
result =[]
for i in range(len(X)):
    newlist = []
    for j in range(len(X[0])):
        newlist.append(X[i][j] * Y)
    result.append(newlist)

print(result)