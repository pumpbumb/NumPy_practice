import numpy as np

a = np.array([[56, 70, 31, 82],
              [471, 614, 741, 58],
              [59, 78, 12, 133]])

c = a.view()
print(f"c is a ? {c is a} \n id(c): {id(c)} \n id(a): {id(a)}\n")
print(f"c.base is a ? {c.base is a}")  # c is a view of the data owned by a

c = c.reshape(2, 6)  # a's shape doesn't change
print('\n', 'a.shape:', a.shape, '\n')

c[0, 4] = 6666
print('a', a, sep='\n')  # changing c, a's data changes

# Slicing an array returns a view of it
s = a[:, 1:3]
s[:] = 10
print('\n', a)
