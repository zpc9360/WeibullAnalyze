import numpy as np
while (True):
    x = int(input('please input rows： '))
    y = int(input('please input columns： '))
    if x <= 0:
        print("rows <= 0")
    if y <= 0:
        print("columns <= 0")
    else:
        break
matrix = np.mat([[int(input()) for col in range(y)] for row in range(x)])
matrix_np = np.mat(matrix)
print('The original matrix：')
# 原矩阵
print(matrix_np)
transposed_matrix = [[row[col] for row in matrix] for col in range(len(matrix[0]))]
print('The transposed matrix：')
#  矩阵的转置：mat.T
print(matrix_np.T)
 # 矩阵的逆：mat.I
print(matrix_np.I)

print(matrix_np.T.I)