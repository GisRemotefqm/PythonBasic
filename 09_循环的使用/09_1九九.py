import numpy as np


row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d * %d = %d" % (col, row, row * col), end="\t")
        col += 1
    print("")
    row += 1
a = np.array([1, 2, 3, 4, 1])

b = np.sum(a == 1)
print(b)