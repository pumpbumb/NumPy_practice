import numpy as np

a = np.array([5, 4, 7, 9])
b = a[:2].copy()
b += 1
print('a = ', a, '\n', 'b = ', b, '\n')

A = np.ones((2, 2))
print(A, '\n')
B = np.eye(2, 2)
print(B, '\n')
C = np.zeros((2, 2))
print(C, '\n')
D = np.diag((-3, -4))
print(D, '\n')
print(np.block([[A, B], [C, D]]))
