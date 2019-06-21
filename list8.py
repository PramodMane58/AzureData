listcolour = ['Green', 'White', 'Black','White']
num = int(input('enter number : '))
newlist = []
for i in listcolour:
    if listcolour.count(i) == num:
        if i not in newlist:
            newlist.append(i)
print(newlist)