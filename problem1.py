print('Please enter frist name and last name : ')
name = input()
namelist = name.split(' ')
result = ''
for n in range(len(namelist)-1,-1,-1):
    result += namelist[n]
    result += ' '
print(result)