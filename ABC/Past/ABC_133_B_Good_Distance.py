import math

N, D = map(int, input().split())
point_list = list()
count = 0
for i in range(N):
	x = list(map(int, input().split()))
	point_list.append(x)
for i in range(N - 1):
	for j in range(i + 1, N):
		point1 = point_list[i]
		point2 = point_list[j]
		distance_pow = 0
		for k in range(D):
			distance_pow += (point1[k] - point2[k]) ** 2
		distance = math.sqrt(distance_pow)
		if distance.is_integer() == True:
			count += 1
print(count)
