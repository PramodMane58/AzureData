import array as arr
a = arr.array('i', [2, 6,8,2,8,2,1])
ele = input('Please enter element')
a.remove(int(ele))
print(a)