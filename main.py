import numpy as np
import copy
import math


def funca(s):
    n = copy.deepcopy(s)
    for j in range(1, N - 1):
        for i in range(1, j):
            n[j][i] = (1-w)*s[j][i]+(w/(2*(a+b)))*(a*n[j-1][i]+b*n[j][i-1]+a*s[j+1][i]+b*s[j][i+1]+(h**2)*F[j][i])
    return n


def prod(s1, s2):
    prsum = 0
    for j in range(N):
        for i in range(j+1):
            prsum += h*h * s1[j][i] * s2[j][i]
    return prsum


def norm(s):
    return math.sqrt(prod(s, s))


def mdif(s1, s2):
    n = copy.deepcopy(s1)
    for j in range(N):
        for i in range(j+1):
            n[j][i] -= s2[j][i]
    return n



N = 6
h = 1 / (N-1)
a = 1
b = 1.2
d = 1/10**6
w = 1.1
S = [[(np.sign(i * (j - i) * (N - j - 1))) for i in range(j + 1)] for j in range(N)]
F = [[0.2*math.exp(h*i)*math.cos(h*j) for i in range(j + 1)] for j in range(N)]
Fi = [[math.exp(h*i)*math.cos(h*j) for i in range(j + 1)] for j in range(N)]
for j in range(0, N-1):
    S[j][0] = math.cos(h*j)
    S[j][j] = math.exp(h*j)*math.cos(h*j)
for i in range(0, N):
    S[N-1][i] = math.exp(h * i) * math.cos(h * (N-1))

k = 1
FM = copy.deepcopy(S)
SM = funca(FM)
while norm(mdif(SM, FM)) > d:
    k += 1
    SM, FM = funca(SM), SM

print(k)
print(norm(mdif(Fi,SM)))
