import numpy as np

# 創建矩陣
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# 矩陣加法
C = A + B
print("矩陣相加的結果：")
print(C)

# 矩陣減法
D = A - B
print("\n矩陣相減的結果：")
print(D)

# 矩陣乘法
E = np.dot(A, B)
print("\n矩陣相乘的結果：")
print(E)

# 轉置矩陣
A_transpose = A.T
print("\nA的轉置矩陣：")
print(A_transpose)

# 矩陣的元素-wise 乘法
F = A * B
print("\n矩陣的元素-wise 乘法的結果：")
print(F)

# 矩陣的元素-wise 除法
G = A / B
print("\n矩陣的元素-wise 除法的結果：")
print(G)
