str1 = 'restart'
s = str1[0]
print(s + str1[str1.index(s)+1:].replace(s, '$'))



