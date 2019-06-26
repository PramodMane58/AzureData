s=('HHH','THH','HHT','THT','HTH','TTH','TTT')
total_Occurance = 0
#for x in s:
# if s.count('H') == 3:
# total_Occurance += 1
print("A :")
print(s.count('HHH')/ len(s).__round__(2))
countonehead= 0
counttwohead= 0
for i in s:
    if i.count('H') == 1:
        countonehead +=1
    elif i.count('H') >= 2:
        counttwohead +=1
print("B :")
print(countonehead / len(s).__round__(2))
print("C :")
print(counttwohead / len(s).__round__(2))

