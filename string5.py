num = int(input("enter num : "))
list1 = []
for i in range(0,num):
    list1.append(input("enter string : "))
print(max(list1, key=len))