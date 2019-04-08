import numpy as np
import copy
import math


def funca(s):
    n = copy.deepcopy(s)
    for j in range(1, N - 1):
        for i in range(1, j):
            print(0)
    return n







N = 5
h = 1 / (N-1)
a = 1
b = 1.2
d = 1 / 10 ** 6
S = [[(np.sign(i * (j - i) * (N - j - 1))) for i in range(j + 1)] for j in range(N)]
F = [[0.2*math.exp(h*i)*math.cos(h*j) for i in range(j + 1)] for j in range(N)]
for j in range(0, N-1):
    S[j][0] = math.cos(h*j)
    S[j][j] = math.exp(h*j)*math.cos(h*j)
for i in range(0, N):
    S[N-1][i] = math.exp(h * i) * math.cos(h * (N-1))

print(S)
print(F)
