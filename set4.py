x = {"apple", "banana", "cherry"}
print("original set")
print(x)
num = int(input('Number of item remove : '))
if len(x) < num:
    print('only '+str(len(x)) + ' items in set')
else:
    for i in range(0,num,1):
        item = input("enter remove item : ")
        if item in x:
            x.remove(item)
    print(x)