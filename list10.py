list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
item_list = ['item', 5, 'foo', 3.14, True]
new_list = []
for i in range(0,len(list)):
    if i not in (0,4,5):
        new_list.append(list[i])
print(new_list)

