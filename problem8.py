def histogram(*items):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

print('Enter list of integers')
list = input().split(',')
print(list)
#histogram(list)