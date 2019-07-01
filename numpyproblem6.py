import numpy as np
x = np.ones(9).reshape(3, 3)
print("Original array:")
print(x)
print("\n")
x = np.pad(x, pad_width=1, mode='constant', constant_values=0)
print(x)