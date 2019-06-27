Y = [[5,8,1],[6,7,3],[4,5,9]]

result =[]
for i in range(len(Y[0])):
    newlist = []
    for j in range(len(Y)):
        newlist.append(Y[j][i])
    result.append(newlist)

print(result)