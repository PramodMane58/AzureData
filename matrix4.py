X = [[12,7,3],[4 ,5,6],[7 ,8,9]]
Y = [[5,8,1],[6,7,3],[4,5,9]]

result =[]
for i in range(len(X)):
    newlist = []
    for j in range(len(Y[0])):
        sum = 0
        for k in range(len(Y)):
            sum += (X[i][k] * Y[k][j])
        newlist.append(sum)
    result.append(newlist)

print(result)