print('Please enter frist name and last name : ')
name = input()
namelist = name.split(' ')
print(" ".join(namelist[::-1]))