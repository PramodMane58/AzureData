listcolour = ['Green', 'White', 'Black','White']
listcolour1 = ['Green', 'Whites', 'Blacks','Whites']
result = False
for x in listcolour:
    for y in listcolour1:
        if x == y:
            result = True
            break

print(result)