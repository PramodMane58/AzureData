import numpy as np 
a = np.array([5,2,6,2,7,5,6,8,2,9]) 

print('First array:')
print(a)
print('\n')

print 'Unique values of first array:' 
u = np.unique(a) 

u,indices = np.unique(a, return_index = True) 
print(indices)

print 'Indices of unique array:' 
u,indices = np.unique(a,return_inverse = True) 
print (indices)


print 'Indices are:' 
print indices 
print '\n'  

print 'Reconstruct the original array using indices:' 
print u[indices] 
print '\n'  

print 'Return the count of repetitions of unique elements:' 
u,indices = np.unique(a,return_counts = True) 
print u 
print indices