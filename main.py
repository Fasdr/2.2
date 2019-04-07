import numpy as np
import copy
import math


def funca(s):
    n = copy.deepcopy(s)
    for j in range(1, N - 1):
        for i in range(1, j):
            n[j][i] = (-a * (s[j][i - 1] - 2 * s[j][i] + s[j][i + 1]) - b * (
                        s[j - 1][i] - 2 * s[j][i] + s[j + 1][i])) / (h ** 2)
    return n


def funcb(s, l):
    n = copy.deepcopy(s)
    for j in range(1, N - 1):
        for i in range(1, j):
            n[j][i] = l * s[j][i] - (-a * (s[j][i - 1] - 2 * s[j][i] + s[j][i + 1]) - b * (
                        s[j - 1][i] - 2 * s[j][i] + s[j + 1][i])) / (h ** 2)
    return n


def prod(s1, s2):
    prsum = 0
    for j in range(N - 1):
        for i in range(j + 1):
            prsum += s1[j][i] * s2[j][i]
    return prsum


def norm(s):
    return math.sqrt(prod(s, s))


def normal(s):
    n = copy.deepcopy(s)
    normn = norm(n)
    for j in range(1, N - 1):
        for i in range(1, j):
            n[j][i] = n[j][i] / normn
    return n


N = 40
h = 1 / N
a = 1
b = 1.2
d = 1 / 10 ** 6
S = [[np.sign(i * (j - i) * (N - j - 1)) for i in range(j + 1)] for j in range(N)]
n = 0
m = 0

S1 = [S, funca(normal(S))]
lamax = [prod(normal(S1[0]), S1[1])]

while True:
    n += 1
    S1.append(funca(normal(S1[n])))
    lamax.append(prod(normal(S1[n]), S1[n + 1]))
    if abs(lamax[n] - lamax[n - 1]) / lamax[n - 1] < d:
        break

print(n)
S2 = [S, funcb(normal(S), lamax[n])]
lamin = [prod(normal(S2[0]), S2[1])]

while True:
    m += 1
    S2.append(funcb(normal(S2[m]), lamax[n]))
    lamin.append(prod(normal(S2[m]), S2[m + 1]))
    if abs(lamin[m] - lamin[m - 1]) / (lamax[n] - lamin[m - 1]) < d:
        break
print(m)

print(lamax[n], lamax[n] - lamin[m])