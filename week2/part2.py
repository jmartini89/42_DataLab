import numpy as np
import matplotlib.pyplot as plt

#1
print(
    "1. random matrix\n",
    np.random.rand(2, 3)
)

#2
print(
    "2. 1x1 to 4x3 conversion\n",
    np.arange(0, 12).reshape(4, 3)
)

#3
def incrementalArray(n):
  return np.linspace(0, 1, n).reshape(1, n)

arr = incrementalArray(5)
print(
    "3. incremental array\n",
    arr, "\n",
    arr.shape
)

#4
arr = np.random.randint(1000, size=(10, 12))
print(
    "4. [0:4, 8:12] from 10x12\n",
    arr, "\n",
    arr[0:4, 8:12]
)

#5
m = 10
n = 5
arr = np.empty((n))
for x in range(m):
    arr = np.vstack((arr, incrementalArray(n)))
print(
    "5. m x n\n",
    arr
)
plt.imshow(arr)
plt.show()

#6
matrix = np.random.randint(50, size=(n, m))
res = np.matmul(arr, matrix)
print(
    "6. product\n",
    res
)
plt.imshow(res)
plt.show()