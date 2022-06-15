from math import sqrt

N, K = map(int, input().split())

A = list(map(int, input().split()))

p = [[0, 0]]
for i in range(N):
    X, Y = map(int, input().split())
    p.append([X, Y])

dist = [[0] * (N + 1) for i in range(K)]


