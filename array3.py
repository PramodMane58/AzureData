import array as arr
a = arr.array('i', [2, 2, 6, 8])
list = []
for i in a:
    if i in list:
        continue
    else:
        list.append(i)
        print('element '+str(i)+' count =' + str(a.count(i)))