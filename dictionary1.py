
d = {0: 2, 1: 4, 2: 3,3:1}
print('Original dictionary : ',d)
sorted_d = sorted(d.values())
print('Dictionary in ascending order by value : ',sorted_d)
sorted_a = sorted(d.values(),reverse=True)
print('Dictionary in descending order by value : ',sorted_a)