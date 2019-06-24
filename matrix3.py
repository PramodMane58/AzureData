X = [[ 5, 1 ,3], [ 1, 1 ,1], [ 1, 2 ,1]]
Y = [1, 2, 3]

result =[]
for i in range(len(X)):
    sum = 0
    for j in range(len(X[0])):
        sum = sum + (X[i][j] * Y[j])
    result.append(sum)

print(result)