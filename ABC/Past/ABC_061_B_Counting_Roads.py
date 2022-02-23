N, M = map(int, input().split())

road = [0] * (N + 1)
for _ in range(M):
	a, b = map(int, input().split())
	road[a] += 1
	road[b] += 1
for i in range(1, N + 1):
	print(road[i])

