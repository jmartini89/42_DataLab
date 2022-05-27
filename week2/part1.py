import numpy as np

#1
print(
    "1. ten zeros\n",
    np.zeros(10))

#2
print(
    "2. ten ones\n",
    np.ones(10)
)

#3
print(
    "3. from 10 to 50\n",
    np.arange(10, 51)
)

#4
print(
    "4. even from 10 to 50\n",
    np.arange(10, 51, 2)
)

#5
print(
    "5. 3x3 identity matrix\n",
    np.eye(3)
)

#6
print(
    "6. random between 0 and 1\n",
    np.random.random()
)

#7
print(
    "7. linear space\n",
    np.linspace(0, 1, 10)
)
