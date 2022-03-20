from collections import deque

import itertools

N, M, K, S, T, X = map(int, input().split())

adjacent_check = list([0] * (N + 1) for _ in range(N + 1))

for _ in range(M):
	U, V = map(int, input().split())
	adjacent_check[U][U] = 1
	adjacent_check[U][V] = 1
	adjacent_check[V][U] = 1
	adjacent_check[V][V] = 1

itertools.product(range(1, N + 1), repeat=(K - 1))
