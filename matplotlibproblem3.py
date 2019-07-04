import matplotlib.pyplot as plt
import numpy as np
with open("/home/admininistrator/test.txt") as f:
    data = f.read()
data = data.split('\n')
x = [int(row.split(' ')[0]) for row in data if row != '']
y = [int(row.split(' ')[1]) for row in data if row != '']
plt.plot(x, y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Sample graph!')
plt.show()