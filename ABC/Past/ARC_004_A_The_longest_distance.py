import math

N = int(input())

dot = [list(map(int, input().split())) for _ in range(N)]
distance_set = set()
for i in range(N - 1):
	for j in range(i + 1, N):
		distance = math.sqrt((dot[i][0] - dot[j][0]) ** 2 + (dot[i][1] - dot[j][1]) ** 2)
		distance_set.add(distance)
print(max(distance_set))
