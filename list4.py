list =['abc', 'xyz', 'aba', '1221']
count = 0
for i in list:
    if len(i) > 1:
        if i[0] == i[-1]:
            count += 1
print(count)