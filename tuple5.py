tup1 = ('physics', 'chemistry', 1997, 2000,'physics',2000)
new_list = []
for i in tup1:
    if tup1.count(i) > 1:
        if i not in new_list:
            new_list.append(i)

print(new_list)
