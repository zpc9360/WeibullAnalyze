import numpy as np
nodes = [[1, 0],[0, 1]]
values = [['x', 'x'],['y','y']]
res = np.array([[cond in vals for vals in values] for cond in nodes], dtype=int)
print(res)