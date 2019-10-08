from numpy import *

while (True):
    x = int(input('please input rows： '))
    y = int(input('please input columns： '))
    if x <= 0:
        print("rows <= 0")
    if y <= 0:
        print("columns <= 0")
    else:
        break

# 矩阵的创建
matrix_np=mat([[int(input()) for col in range(x)] for row in range(y)])
# 原矩阵
print('The original matrix：')
print(matrix_np)
# 矩阵的转置：mat.T
print('The transposed matrix：')
print(matrix_np.T)
# 矩阵的逆：mat.I
print('The inversed matrix：')
print(matrix_np.I)
