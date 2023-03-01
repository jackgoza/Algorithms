import numpy as np
import pandas as pd

p_i = [0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14]
q_i = [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05]
n = len(p_i)


p = pd.Series(p_i, index=range(1, n + 1))
q = pd.Series(q_i)

e = pd.DataFrame(np.diag(q), index=range(1, n + 2))
w = pd.DataFrame(np.diag(q), index=range(1, n + 2))
root = pd.DataFrame(np.zeros((n, n)), index=range(1, n + 1), columns=range(1, n + 1))

for l in range(1, n + 1):
    for i in range(1, n - l + 2):
        j = i + l - 1
        e.at[i, j] = np.inf
        w.at[i, j] = w.at[i, j - 1] + p[j] + q[j]
        for r in range(i, j + 1):
            t = e.at[i, r - 1] + e.at[r + 1, j] + w.at[i, j]
            if t < e.at[i, j]:
                e.at[i, j] = t
                root.at[i, j] = r

print("\n-----------------------------------")
print("e")
print("-----------------------------------")
print(e)
print("\n-----------------------------------")
print("w")
print("-----------------------------------")
print(w)
print("\n-----------------------------------")
print("root")
print("-----------------------------------")
print(root)

# -----------------------------------
# e
# -----------------------------------
#       0     1     2     3     4     5     6     7
# 1  0.06  0.28  0.62  1.02  1.34  1.83  2.44  3.12
# 2  0.00  0.06  0.30  0.68  0.93  1.41  1.96  2.61
# 3  0.00  0.00  0.06  0.32  0.57  1.04  1.48  2.13
# 4  0.00  0.00  0.00  0.06  0.24  0.57  1.01  1.55
# 5  0.00  0.00  0.00  0.00  0.05  0.30  0.72  1.20
# 6  0.00  0.00  0.00  0.00  0.00  0.05  0.32  0.78
# 7  0.00  0.00  0.00  0.00  0.00  0.00  0.05  0.34
# 8  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.05
#
# -----------------------------------
# w
# -----------------------------------
#       0     1     2     3     4     5     6     7
# 1  0.06  0.16  0.28  0.42  0.49  0.64  0.81  1.00
# 2  0.00  0.06  0.18  0.32  0.39  0.54  0.71  0.90
# 3  0.00  0.00  0.06  0.20  0.27  0.42  0.59  0.78
# 4  0.00  0.00  0.00  0.06  0.13  0.28  0.45  0.64
# 5  0.00  0.00  0.00  0.00  0.05  0.20  0.37  0.56
# 6  0.00  0.00  0.00  0.00  0.00  0.05  0.22  0.41
# 7  0.00  0.00  0.00  0.00  0.00  0.00  0.05  0.24
# 8  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.05
#
# -----------------------------------
# root
# -----------------------------------
#      1    2    3    4    5    6    7
# 1  1.0  2.0  2.0  2.0  3.0  3.0  5.0
# 2  0.0  2.0  3.0  3.0  3.0  5.0  5.0
# 3  0.0  0.0  3.0  3.0  4.0  5.0  5.0
# 4  0.0  0.0  0.0  4.0  5.0  5.0  6.0
# 5  0.0  0.0  0.0  0.0  5.0  6.0  6.0
# 6  0.0  0.0  0.0  0.0  0.0  6.0  7.0
# 7  0.0  0.0  0.0  0.0  0.0  0.0  7.0
