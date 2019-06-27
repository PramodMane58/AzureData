def histogram(*items):
    for n in items:
        output = ''
        times = int(n)
        while(times > 0 ):
          output += '*'
          times = times - 1
        print(output)

print('Enter list of integers')
list = input().split(',')
histogram(list)