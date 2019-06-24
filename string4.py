str1 = input("enter string : ")
if len(str1) > 2:
    if 'ing' in str1[len(str1)-3:len(str1)].lower():
        str1 =str1+'ly'
    else:
        str1 = str1 + 'ing'
print('Result : ' +str1)

