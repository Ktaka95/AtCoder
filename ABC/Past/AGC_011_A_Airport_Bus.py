N, C, K = map(int, input().split())
passenger = 0
bus = 0
T = list()
for i in range(N):
	T.append(int(input()))
T = sorted(T, reverse=True)
i = 0
while i < N:
	departure = T[i]
	while T[i] >= departure - K and passenger < C:
		passenger += 1
		if i != N - 1:
			i += 1
		else:
			i += 1
			break
	passenger = 0
	bus += 1
print(bus)
