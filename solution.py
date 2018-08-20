import numpy as np
from scipy.optimize import linprog

A = np.array([[-1, 2], [3,2], [1, -1], [-1, 0], [0, -1]])
b = np.array([4, 14, 3, 0, 0])
c = np.array([2,-3])

res = linprog(c, A_ub=A, b_ub=b,bounds=(0, None))

print('Optimal value:', res.fun, '\nX:', res.x)
